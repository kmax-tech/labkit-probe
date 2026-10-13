#!/usr/bin/env python3
"""docs-per-case: one question, one number — kept through runlog, rechecked from its rows.

    ../../.venv/bin/python scripts/01_measure.py            # count, keep, print the number + run_id
    ../../.venv/bin/python scripts/01_measure.py --check    # recompute from the kept rows; hold metrics.json and the protocol to it

cost = "seconds" (the protocol head says so) — no freeze, no audit before the run,
the run itself is the instrument check; the one analysis audit comes when
the number is promoted or steers a decision (LAB-017 The number of audits follows the cost tier). The number is produced here, never
retyped (LAB-041 Generate numbers, don't retype them): the protocol's Result line cites it with the run_id, and
`--check` holds that line to the run.

Fill the constants and the three TODOs: expected_ids(), rows(), evaluate_rows().
Everything else stays — `visible()` is the one reader of a directory, the
denominator is the source's id list, a missing item is a refusal. INPUTS names
what the rows read beyond SOURCE: a count of documents per case reads the case
directories, and only a frozen directory makes the number citable against
their content (three cold agents left them unfrozen, 2026-10-13).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from labkit import recheck, runlog

AREA = Path(__file__).resolve().parent.parent
REPO = AREA.parent.parent
PROTOCOL = AREA / "PROTOCOL-docs-per-case.md"
SOURCE = REPO / "data" / "raw" / "cases.jsonl"  # what is counted — a file or a directory
INPUTS = REPO / "data" / "raw" / "inputs"       # a directory the rows read beyond SOURCE, frozen with it
OUT = AREA / "output" / "docs-per-case.jsonl"          # one row per item, written by this script
COUNT_FIELD = "docs"                            # the per-item number in each row
METRIC_KEY = "mean_docs_per_case"               # the kept number's key in metrics.json; the test reads both names from here


def visible(directory: Path) -> list[Path]:
    """The files that count: regular files, no hidden entries, no nested
    directories. `.DS_Store` once moved a mean by a whole document while
    test and --check stayed green (2026-10-05) — say in the protocol's
    `Unit:` field what one counted thing is, and keep this the only reader."""
    return sorted(p for p in directory.iterdir() if p.is_file() and not p.name.startswith("."))


def cases() -> list[dict]:
    """The case records SOURCE lists, one JSON object per line."""
    return [json.loads(line) for line in SOURCE.read_text(encoding="utf-8").splitlines() if line.strip()]


def expected_ids() -> list[str]:
    """The ids the number is over, read from SOURCE — the denominator
    comes from the source, never from the rows that happened to be produced."""
    return [c["case_id"] for c in cases()]


def rows(ids: list[str]) -> list[dict]:
    """One row per case: the count of visible documents in its directory
    under the case's `inputs` root. A missing or empty directory is a refusal,
    not a skipped row."""
    by_id = {c["case_id"]: c for c in cases()}
    out = []
    for case_id in ids:
        directory = REPO / by_id[case_id]["inputs"] / case_id
        if not directory.is_dir():
            raise FileNotFoundError(f"rows(): no case directory {directory} — refusing a silent loss")
        files = visible(directory)
        if not files:
            raise ValueError(f"rows(): {case_id} has no visible document — refusing a zero row")
        out.append({"id": case_id, COUNT_FIELD: len(files)})
    return out


def evaluate_rows(items: list[dict], ids: list[str]) -> dict:
    """TODO: the number(s) from the rows, over the ids SOURCE lists — and,
    only if the protocol registers ids (a model in the loop), one key per id
    (`c1_pass`); a plain count registers none. Every key lands in
    metrics.json, and `--check` demands each verbatim in the protocol's
    "Answer to the question" line — keep the dict to what that line carries."""
    if not ids:
        raise ValueError("evaluate_rows(): SOURCE lists no ids — refusing a number over nothing")
    if len(items) != len(ids):
        raise ValueError(f"evaluate_rows(): {len(items)} rows for {len(ids)} ids — a silent loss")
    total = sum(r[COUNT_FIELD] for r in items)
    return {METRIC_KEY: total / len(items)}


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
    # data= freezes every input the number reads (sha and rows; a directory:
    # sha over each file) in the run; `finalize` refuses a run of seconds
    # without it, and one whose source or OUT is not in git.
    frozen = {"source": SOURCE, **({"inputs": INPUTS} if INPUTS else {})}
    with runlog.run("docs-per-case", config={k: str(p.relative_to(REPO)) for k, p in frozen.items()},
                    base_dir=AREA, data=frozen,
                    long=True, protocol=PROTOCOL.name) as run:
        # every row names the run that wrote it (`_prov.run`): finalize holds
        # the file to it, and a row from another run is a file of two measurements
        OUT.write_text("".join(json.dumps({**r, "_prov": {"run": run.run_id}},
                                          ensure_ascii=False) + "\n" for r in items),
                       encoding="utf-8")
        run.output(OUT)
        metrics = evaluate_rows(items, ids)
        run.metrics(**metrics)
        print(json.dumps(metrics, indent=1))
        print(f"run: {run.run_id}  → protocol-fill {PROTOCOL.name} --from-run {run.run_id}  "
              f"(writes the Answer, Result and Runs lines from metrics.json)")


if __name__ == "__main__":
    main()
