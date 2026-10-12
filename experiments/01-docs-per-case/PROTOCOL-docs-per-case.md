# Experiment protocol: docs-per-case

## Summary (after the run, for a person)

- **Result:** <the answer to the question above, in at most two plain sentences…>

## Intent (before the run)

- **Terms of this protocol:** *case* — one line of `data/raw/cases.jsonl` (its `case_id`, here `antrag-01`…`antrag-12`); *document* — one visible regular file directly under `<inputs>/<case_id>/` (`inputs` is the case's field, relative to the repo root; `scripts/01_measure.py:visible` is the one reader); *mean_docs_per_case* — the key in metrics.json: total documents over all listed cases divided by the number of listed cases.
- **Question / hypothesis:** How many input documents does a case carry on average? Exploratory: a descriptive number, no expectation registered — the cases visibly carry 2–6 files, so a mean of about 3–4.

## Result (after the run — write back, don't go quiet)

- **Answer to the question:** <per registered id its verdict, and the run_id…>

## Setup

- **Data / scope:** `data/raw/cases.jsonl` (N = 12 cases, all of them, no pilot subset) and the directories `data/raw/inputs/<case_id>/`; produced by `scripts/01_measure.py`, kept through `runlog`, rows in `output/docs-per-case.jsonl`.
- **Exclusions / filters:** Hidden entries (names starting with `.`) and nested directories under a case directory are not documents (`visible()`); nothing else is dropped. A case with no directory or no document is a refusal of the whole run, not a zero.
- **Unit:** One document = one visible regular file directly under `<inputs>/<case_id>/`, whatever its name or size; the number is the arithmetic mean of documents per case over the cases listed in `cases.jsonl`.

## Runs (documented runs — via `runlog`, cite run_ids instead of retyping numbers)

- <run_id> — <one sentence: what this run was>

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
