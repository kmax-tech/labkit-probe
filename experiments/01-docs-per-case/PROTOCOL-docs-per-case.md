# Experiment protocol: docs-per-case

## Summary (after the run, for a person)

- **Result:** <the answer to the question above, in at most two plain sentences…>

## Intent (before the run)

- **Terms of this protocol:** a *case* is one line of `data/raw/cases.jsonl` (fields `case_id`, `inputs`); a case's *documents* are the visible regular files directly under `<inputs>/<case_id>/` (`inputs` relative to the repo root); `mean_docs_per_case` is the arithmetic mean of the per-case document count over all listed cases.
- **Question / hypothesis:** What is the mean number of input documents per case over the cases in `data/raw/cases.jsonl`? A descriptive count, no expectation registered.
- **Success / failure criterion:** n/a — a descriptive count with no hypothesis; the number is the answer whatever its value, no verdict is issued.
- **Admissibility condition:** every case listed in `data/raw/cases.jsonl` has a directory `<inputs>/<case_id>/` with at least one visible document; a missing or empty one aborts the run (`rows()` refuses), because then the denominator would no longer be the source's case list and the mean would be over a different population.

## Result (after the run — write back, don't go quiet)

- **Answer to the question:** <per registered id its verdict, and the run_id…>

## Setup

- **Data / scope:** `data/raw/cases.jsonl` (N = 12 cases, all of them, ids antrag-01…antrag-12) and the directories `data/raw/inputs/<case_id>/`; producer `scripts/01_measure.py`, no pilot subset (seconds, one deterministic pass).
- **Exclusions / filters:** hidden entries (names starting with `.`) and nested directories under a case directory are not counted (`visible()`); a case without a directory or with zero documents aborts the run instead of being dropped.
- **Unit:** one counted thing is one visible regular file directly under `<inputs>/<case_id>/`, whatever its extension or content; the number is the mean of these counts per case.

## Runs (documented runs — via `runlog`, cite run_ids instead of retyping numbers)

- <run_id> — <one sentence: what this run was>

## Head (read by the checks)



*How to fill each field, the cuts by tier and the intent ids:
`protocol-field-guide.md` (`protocol-check --guide`); which fields this
protocol's `cost` owes, and which fall due after a documented run:
`protocol-check --contract` — the one list, never retyped here; fill by
label with `protocol-fill PROTOCOL-<name>.md "<label>" "<value>"`.*

```toml
# A plain count registers no promise (field guide: a count without a model
# registers no promise and no criterion) — the tables are declared, and empty.
promise = []

[protocol]
standard = "0.19"
id = "p-cff1eb3cd1d84ea3"
type = "exploratory"
cost = "seconds"
frozen = false
preflight_audit = ""
