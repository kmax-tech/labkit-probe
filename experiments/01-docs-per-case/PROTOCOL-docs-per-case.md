# Experiment protocol: docs-per-case

## Summary (after the run, for a person)

- **Result:** On average a case brings 3.5 input documents (run `2026-10-12T18-52-51_d18a`, 12 cases, 42 documents; per case between 2 and 6).
- **Limits:** a document is any visible regular file in the case directory — the count does not look inside files, and nested directories are ignored; N = 12 is the whole list, no sampling.
- **Next step:** none owed for this count; the agent audit falls due when the number goes into a note or steers a decision (LAB-017).

## Intent (before the run)

- **Terms of this protocol:** a *case* is one line of `data/raw/cases.jsonl` (fields `case_id`, `inputs`); a case's *documents* are the visible regular files directly under `<inputs>/<case_id>/` (`inputs` relative to the repo root); `mean_docs_per_case` is the arithmetic mean of the per-case document count over all listed cases.
- **Question / hypothesis:** What is the mean number of input documents per case over the cases in `data/raw/cases.jsonl`? A descriptive count, no expectation registered.
- **Success / failure criterion:** n/a — a descriptive count with no hypothesis; the number is the answer whatever its value, no verdict is issued.
- **Admissibility condition:** every case listed in `data/raw/cases.jsonl` has a directory `<inputs>/<case_id>/` with at least one visible document; a missing or empty one aborts the run (`rows()` refuses), because then the denominator would no longer be the source's case list and the mean would be over a different population.

## Result (after the run — write back, don't go quiet)

- **Answer to the question:** `mean_docs_per_case` = 3.5 — the mean over the 12 cases of `data/raw/cases.jsonl` (42 visible documents in all); run `2026-10-12T18-52-51_d18a`.

## Setup

- **Data / scope:** `data/raw/cases.jsonl` (N = 12 cases, all of them, ids antrag-01…antrag-12) and the directories `data/raw/inputs/<case_id>/`; producer `scripts/01_measure.py`, no pilot subset (seconds, one deterministic pass).
- **Exclusions / filters:** hidden entries (names starting with `.`) and nested directories under a case directory are not counted (`visible()`); a case without a directory or with zero documents aborts the run instead of being dropped.
- **Unit:** one counted thing is one visible regular file directly under `<inputs>/<case_id>/`, whatever its extension or content; the number is the mean of these counts per case.

## Runs (documented runs — via `runlog`, cite run_ids instead of retyping numbers)

- `2026-10-12T18-52-51_d18a` — the one full run of the count over all 12 cases, deterministic, no model.

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
