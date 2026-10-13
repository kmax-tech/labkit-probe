# Experiment protocol: docs-per-case

## Summary (after the run, for a person)

- **Result:** mean_docs_per_case = 3.5 (run 2026-10-13T08-30-13_be11)

## Intent (before the run)

- **Terms of this protocol:** *case* — one line of `data/raw/cases.jsonl` (`case_id`, `inputs`); *input document* — one visible regular file directly under `<inputs>/<case_id>/` (no hidden entries, no nested directories); *mean_docs_per_case* — the kept key in metrics.json: total input documents over all cases divided by the number of cases the source lists.
- **Question / hypothesis:** How many input documents does a case have on average — the mean number of input documents per case over the cases in `data/raw/cases.jsonl`? Descriptive count, no expectation registered.

## Result (after the run — write back, don't go quiet)

- **Answer to the question:** mean_docs_per_case = 3.5 (run 2026-10-13T08-30-13_be11)

## Setup

- **Data / scope:** `data/raw/cases.jsonl` (N = 12 cases, all of them — no pilot subset at cost seconds); documents are the files under `data/raw/inputs/<case_id>/` as the `inputs` field names them; producer `scripts/01_measure.py`, one row per case in `output/docs-per-case.jsonl`.
- **Exclusions / filters:** Hidden entries (names starting with `.`) and nested directories under a case directory are not counted (`visible()`); a case listed in the source with no directory or no documents is a refusal, not a dropped row. Nothing else is filtered.
- **Unit:** one input document = one visible regular file directly under `<inputs>/<case_id>/`; the number is averaged over cases (denominator = the source's case list).

## Runs (documented runs — via `runlog`, cite run_ids instead of retyping numbers)

- 2026-10-13T08-30-13_be11 — the kept run; its metrics.json is the number

## Head (read by the checks)



*How to fill each field, the cuts by tier and the intent ids:
`protocol-field-guide.md` (`protocol-check --guide`); which fields this
protocol's `cost` owes, and which fall due after a documented run:
`protocol-check --contract` — the one list, never retyped here; fill by
label with `protocol-fill PROTOCOL-<name>.md "<label>" "<value>"`.*

```toml
[protocol]
standard = "0.19"
id = "p-21ad4c89905e4020"
type = "exploratory"
cost = "seconds"
frozen = false
preflight_audit = ""
