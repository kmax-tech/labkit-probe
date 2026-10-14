# Experiment protocol: docs-per-case

## Summary (after the run, for a person)

- **Result:** pending run

## Intent (before the run)

- **Terms of this protocol:** n/a — no coinage
- **Question / hypothesis:** What is the mean number of input documents per case over the 12 cases in data/raw/cases.jsonl?

## Result (after the run — write back, don't go quiet)

- **Answer to the question:** pending run

## Setup

- **Data / scope:** data/raw/cases.jsonl (12 cases); documents under data/raw/inputs/<case_id>/; script scripts/01_measure.py
- **Exclusions / filters:** none; hidden files and nested directories are not counted (visible())
- **Unit:** one regular, non-hidden file directly under a case directory

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
id = "p-60c41e7be92544d3"
type = "exploratory"
cost = "seconds"
frozen = false
preflight_audit = ""
