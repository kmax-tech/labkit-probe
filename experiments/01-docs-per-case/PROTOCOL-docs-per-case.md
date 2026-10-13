# Experiment protocol: docs-per-case

## Summary (after the run, for a person)

- **Result:** <the answer to the question above, in at most two plain sentences…>

## Intent (before the run)

- **Terms of this protocol:** <first, because the question uses them…>
- **Question / hypothesis:** <the one question — what do we expect?>

## Result (after the run — write back, don't go quiet)

- **Answer to the question:** <per registered id its verdict, and the run_id…>

## Setup

- **Data / scope:** <source, N, producer script; pilot subset first>
- **Exclusions / filters:** <what is dropped from the data or output and why…>
- **Unit:** <what one counted or judged thing is…>

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
id = "p-21ad4c89905e4020"
type = "<exploratory | confirmatory>"
cost = "seconds"
frozen = false
preflight_audit = ""
