# Experiment protocol: docs-per-case

## Summary (after the run, for a person)

- **Result:** A case carries 3.5 input documents on average (12 cases, 42 documents; run 2026-10-12T20-59-27_6f9d). Counts range from 2 to 6 per case.

## Intent (before the run)

- **Terms of this protocol:** *case* — one line of `data/raw/cases.jsonl` (a `case_id` and an `inputs` root); *document* — one visible regular file directly under `<inputs>/<case_id>/` (no hidden entries, no nested directories); *mean_docs_per_case* — the key in metrics.json: sum of documents over the cases, divided by the number of cases the source lists.
- **Question / hypothesis:** How many input documents does a case carry on average? Exploratory: a descriptive count with no expected value; it is the denominator for later per-document costs.

## Result (after the run — write back, don't go quiet)

- **Answer to the question:** mean_docs_per_case = 3.5 (run 2026-10-12T20-59-27_6f9d; 42 documents over 12 cases, per-case counts 2–6).

## Setup

- **Data / scope:** `data/raw/cases.jsonl` (N = 12 cases, all of them); the documents under `data/raw/inputs/<case_id>/`; counted by `scripts/01_measure.py`; no pilot subset — the full run takes seconds.
- **Exclusions / filters:** Hidden entries (names starting with `.`) and nested directories are not documents (`visible()`); nothing else is dropped. A case whose directory is missing or empty aborts the run instead of counting as 0.
- **Unit:** One case; the per-case count is the number of visible regular files directly under `<inputs>/<case_id>/`.

## Runs (documented runs — via `runlog`, cite run_ids instead of retyping numbers)

- 2026-10-12T20-59-27_6f9d — the one measure run over all 12 cases; its metrics.json carries mean_docs_per_case.

## Head (read by the checks)



*How to fill each field, the cuts by tier and the intent ids:
`protocol-field-guide.md` (`protocol-check --guide`); which fields this
protocol's `cost` owes, and which fall due after a documented run:
`protocol-check --contract` — the one list, never retyped here; fill by
label with `protocol-fill PROTOCOL-<name>.md "<label>" "<value>"`.*

```toml
[protocol]
standard = "0.19"
id = "p-2d9bd6121bde43ad"
type = "exploratory"
cost = "seconds"
frozen = false
preflight_audit = ""
