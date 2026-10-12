#!/usr/bin/env python3
"""docs-per-case: one question, one number — kept through runlog, rechecked from its rows.

    ../../.venv/bin/python scripts/01_measure.py            # count, keep, print the number + run_id
    ../../.venv/bin/python scripts/01_measure.py --check    # recompute from the kept rows; hold metrics.json and the protocol to it

cost = "seconds" (the protocol head says so) — no freeze, no audit before the run,
the run itself is the instrument check; the one analysis audit comes when
the number is promoted or steers a decision (LAB-017 The number of audits follows the cost tier). The number is produced here, never
retyped (LAB-041 Generate numbers, don't retype them): the protocol's Result line cites it with the run_id, and
`--check` holds that line to the run.

`visible()` is the one reader of a directory, the denominator is the source's
id list (`data/raw/cases.jsonl`), a missing item is a refusal.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from labkit import recheck, runlog

AREA = Path(__file__).resolve().parent.parent
REPO = AREA.parent.parent
PROTOCOL = AREA / "PROTOCOL-docs-per-case.md"
SOURCE = REPO / "data" / "raw" / "cases.jsonl"  # what is counted — one case per line, `inputs` names the root of its documents
OUT = AREA / "output" / "docs-per-case.jsonl"          # one row per item, written by this script
COUNT_FIELD = "doc_count"                       # the per-item number in each row
METRIC_KEY = "mean_docs_per_case"               # the kept number's key in metrics.json; the test reads both names from here


def visible(directory: Path) -> list[Path]:
    """The files that count: regular files, no hidden entries, no nested
    directories. `.DS_Store` once moved a mean by a whole document while
    test and --check stayed green (2026-10-05) — say in the protocol's
    `Unit:` field what one counted thing is, and keep this the only reader."""
    return sorted(p for p in directory.iterdir() if p.is_file() and not p.name.startswith("."))


def cases() -> list[dict]:
    """The lines of SOURCE as dicts — `case_id` and `inputs` (relative to the repo root)."""
    out = []
    for n, line in enumerate(SOURCE.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        for k in ("case_id", "inputs"):
            if not row.get(k):
                raise ValueError(f"{SOURCE.name}:{n}: field {k!r} missing or empty")
        out.append(row)
    return out


def expected_ids() -> list[str]:
    """The ids the number is over, read from SOURCE — the denominator
    comes from the source, never from the rows that happened to be produced."""
    ids = [c["case_id"] for c in cases()]
    if len(set(ids)) != len(ids):
        raise ValueError(f"{SOURCE.name}: duplicate case_id")
    return ids


def rows(ids: list[str]) -> list[dict]:
    """One row per id — the raw material of the number: the count of visible
    files under `<inputs>/<case_id>/`. A missing directory or an empty case is
    a refusal, not a skipped row (the Unit field says what counts)."""
    by_id = {c["case_id"]: c for c in cases()}
    out = []
    for cid in ids:
        directory = REPO / by_id[cid]["inputs"] / cid
        if not directory.is_dir():
            raise FileNotFoundError(f"rows(): case {cid!r}: no directory {directory.relative_to(REPO)}")
        docs = visible(directory)
        if not docs:
            raise ValueError(f"rows(): case {cid!r}: no documents under {directory.relative_to(REPO)}")
        out.append({"id": cid, "inputs": by_id[cid]["inputs"], COUNT_FIELD: len(docs),
                    "documents": [p.name for p in docs]})
    return out


def evaluate_rows(items: list[dict], ids: list[str]) -> dict:
    """The number(s) from the rows, over the ids SOURCE lists, plus one
    key per intent id the protocol registers (`c1_pass`, `a1_pass`) —
    intent-check and finalize hold the ids to these keys. Every key lands in
    metrics.json, and `--check` demands each verbatim in the protocol's
    "Answer to the question" line — keep the dict to what that line carries."""
    if not ids:
        raise ValueError("evaluate_rows(): SOURCE lists no ids — refusing a number over nothing")
    if len(items) != len(ids):
        raise ValueError(f"evaluate_rows(): {len(items)} rows for {len(ids)} ids — a silent loss")
    if sorted(r["id"] for r in items) != sorted(ids):
        raise ValueError("evaluate_rows(): the rows' ids are not the ids SOURCE lists")
    counts = [int(r[COUNT_FIELD]) for r in items]
    # [A1] every listed case contributed a count of at least one document —
    # a case without documents has no "documents per case" to speak of.
    a1_pass = all(c >= 1 for c in counts)
    # [C1] the mean is one finite number over exactly the n_cases cases SOURCE lists.
    mean = sum(counts) / len(counts)
    c1_pass = a1_pass and len(counts) == len(ids)
    return {METRIC_KEY: mean, "n_cases": len(ids), "c1_pass": c1_pass, "a1_pass": a1_pass}


def main() -> None:
    ap = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="recompute from OUT and hold metrics.json and the protocol to it")
    args = ap.parse_args()
    ids = expected_ids()
    if args.check:
        v = recheck.holds(area=AREA, out=OUT, recompute=lambda rs: evaluate_rows(rs, ids),
                          note=PROTOCOL)
        print(f"check: run {v.run_id} — {v.keys_compared} keys identical, "
              f"{PROTOCOL.name} carries them and the run_id"
              + (f"; grown since the run: {v.grown}" if v.grown else ""))
        return
    items = rows(ids)
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in items),
                   encoding="utf-8")
    # data= freezes the source (sha, rows) in the run; `finalize` refuses a
    # run of seconds without it, and one whose source or OUT is not in git.
    with runlog.run("docs-per-case", config={"source": str(SOURCE.relative_to(REPO))},
                    base_dir=AREA, data={"source": SOURCE},
                    long=True, protocol=PROTOCOL.name) as run:
        run.output(OUT)
        metrics = evaluate_rows(items, ids)
        run.metrics(**metrics)
        print(json.dumps(metrics, indent=1))
        print(f"run: {run.run_id}  → cite it in {PROTOCOL.name}, field \"Answer to the question\"")


if __name__ == "__main__":
    main()
