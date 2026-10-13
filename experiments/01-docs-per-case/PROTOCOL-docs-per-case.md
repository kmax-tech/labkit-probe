# Experiment protocol: docs-per-case

## Summary (after the run, for a person)

- **Result:** mean_docs_per_case = 3.5 (run 2026-10-13T19-12-08_9a8b)

## Intent (before the run)

- **Terms of this protocol:** n/a — no coinage
- **Question / hypothesis:** How many input documents does each case have, on average, over the 12 cases listed in data/raw/cases.jsonl? A count, no hypothesis: the number is the answer.

## Result (after the run — write back, don't go quiet)

- **Answer to the question:** mean_docs_per_case = 3.5 (run 2026-10-13T19-12-08_9a8b)

## Setup

- **Data / scope:** data/raw/cases.jsonl (12 cases) as the denominator; the documents are the files under data/raw/inputs/<case_id>/ (the inputs field of each case). Producer: scripts/01_measure.py, no model call, seconds. Pilot subset: none, the whole set is 12 cases.
- **Exclusions / filters:** Hidden entries (names starting with a dot, e.g. .DS_Store) and nested directories are not documents: visible() drops them. A case with no visible file is a refusal, not a zero row.
- **Unit:** One document = one regular, non-hidden file directly inside a case directory. Mean = total documents / number of cases in cases.jsonl.

## Runs (documented runs — via `runlog`, cite run_ids instead of retyping numbers)

- 2026-10-13T19-12-08_9a8b — the kept run; its metrics.json is the number

## Head (read by the checks)



*How to fill each field, the cuts by tier and the intent ids:
`protocol-field-guide.md` (`protocol-check --guide`); which fields this
protocol's `cost` owes, and which fall due after a documented run:
`protocol-check --contract` — the one list, never retyped here; fill by
label with `protocol-fill PROTOCOL-<name>.md "<label>" "<value>"`.*

```toml
[protocol]
standard = "0.19"
id = "p-60c41e7be92544d3"
type = "exploratory"
cost = "seconds"
frozen = false
preflight_audit = ""
