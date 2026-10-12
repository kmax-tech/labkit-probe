# Experiment protocol: docs-per-case

## Summary (after the run, for a person)

- **Result:** <the answer to the question above, in at most two plain sentences…>

## Intent (before the run)

- **Terms of this protocol:** A *case* is one line of `data/raw/cases.jsonl` (its `case_id`); its *input documents* are the visible regular files directly under `<inputs>/<case_id>/`, where `inputs` is the field of that line, relative to the repo root; *docs per case* is that file count, `mean_docs_per_case` its arithmetic mean over all cases.
- **Question / hypothesis:** How many input documents does a case carry on average — the mean number of files under `<inputs>/<case_id>/` over the cases listed in `data/raw/cases.jsonl`? Exploratory count, no expectation registered.

## Result (after the run — write back, don't go quiet)

- **Answer to the question:** <per registered id its verdict, and the run_id…>

## Setup

- **Data / scope:** `data/raw/cases.jsonl` (12 cases, antrag-01 … antrag-12, all with `inputs = data/raw/inputs`) and the directories `data/raw/inputs/<case_id>/`; read by `scripts/01_measure.py`, no pilot subset — the whole source is one run of seconds.
- **Exclusions / filters:** Hidden entries (names starting with `.`) and nested directories under a case directory are not documents (`visible()`). [A1] Every listed case has a directory with at least one document; a case without one aborts the run instead of counting as 0 (`a1_pass`).
- **Unit:** One document = one visible regular file directly under `<inputs>/<case_id>/`; one row = one case with its `doc_count`; the kept number is the mean of `doc_count` over the cases the source lists (N from the source, never from the rows produced).

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

[[promise]]
id = "A1"
key = "a1_pass"
sentence = "every case listed in data/raw/cases.jsonl has an input directory with at least one visible document — coverage 12 of 12, else no mean is issued"
scope = ["scripts/01_measure.py:rows", "scripts/01_measure.py:evaluate_rows"]
