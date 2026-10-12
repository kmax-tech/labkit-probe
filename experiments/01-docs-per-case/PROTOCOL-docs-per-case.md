# Experiment protocol: docs-per-case

## Summary (after the run, for a person)

- **Result:** <the answer to the question above, in at most two
  plain sentences: whether the bar set before the run was met ("Yes — the
  class descriptions kept the cable set out of the framework class in all
  five cases, as required") — or that no verdict was possible because an
  admissibility condition failed, and what was still read descriptively;
  the result, not the procedure; no intent ids, metric keys or run_ids,
  they are below>
- **Limits:** <how far it holds, one sentence — the sample, a
  single run, what was not tested; a deviation after the freeze that
  touches the verdict is named here too>
- **Next step:** <what follows — a decision, the next experiment,
  or "none">

## Intent (before the run)

- **Terms of this protocol:** case (one application, a line of `cases.jsonl`) · Fall · `case_id`; document (one visible file under `<inputs>/<case_id>/`) · Dokument · `doc_count` per case; the kept number · mean docs per case · `mean_docs_per_case`
- **Question / hypothesis:** How many input documents does a case carry on average over the cases in `data/raw/cases.jsonl`? No expectation registered — a descriptive count.
- **Success / failure criterion:** [C1] `mean_docs_per_case` is one finite number over exactly the cases the source lists (rows == ids); nothing more is promised for a plain count (→ LAB-003, LAB-004).
- **Admissibility condition:** [A1] every listed case has a directory with at least one visible document — a missing or empty case would make the mean a number over a different population than the file lists, so the script refuses instead of counting 0.

## Result (after the run — write back, don't go quiet)

- **Answer to the question:** <per registered id its verdict, and the
  run_id; numbers as a small table below the label (one row per arm or
  condition), produced by `analysis/<note>.py --check`, never retyped>

## Setup

- **Data / scope:** `data/raw/cases.jsonl` (N = 12 cases, field `inputs` names the directory relative to the repo root), documents under `data/raw/inputs/<case_id>/`; fixture shipped with the repo, no producer script; no pilot subset — one deterministic pass over all cases.
- **Exclusions / filters:** hidden entries (names starting with `.`) and nested directories are not documents (`visible()`); nothing else is dropped; no gate labels — no model in the loop.
- **Unit:** one document = one regular, non-hidden file directly under `<inputs>/<case_id>/`; not counted: hidden files, nested directories and their contents; an empty or missing case directory is a refusal, never a 0.

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
id = "p-8628e8dab57a4552"
type = "exploratory"
cost = "seconds"
frozen = false
preflight_audit = ""

# The promises as data (labkit 0.71): one table per id — the key the run
# reports, the sentence (the same as the Intent field), the code region, and
# the constants the script reads with promises.all_constants(). A constant is
# named like the config key (lowercase) and stands in exactly one table;
# `frozen = true` owes these tables, and no run starts whose config lacks a
# constant or carries another value.
[[promise]]
id = "C1"
key = "c1_pass"
sentence = "mean_docs_per_case is one finite number over exactly the cases cases.jsonl lists (rows == ids) — a plain count, no threshold"
scope = ["scripts/01_measure.py"]
# constants = { <name> = <value> }  # every threshold the sentence names, read with promises.all_constants() — none for a plain count

[[promise]]
id = "A1"
key = "a1_pass"
sentence = "every listed case has a directory with at least one visible document; a missing or empty case is a refusal, not a 0 in the mean"
scope = ["scripts/01_measure.py"]
# constants = { <name> = <value> }  # every threshold the sentence names, read with promises.all_constants() — none for a plain count
