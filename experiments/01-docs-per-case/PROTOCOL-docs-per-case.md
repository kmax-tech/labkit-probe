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

- **Terms of this protocol:** case (one application, one line of `data/raw/cases.jsonl`) · Fall · `case_id`; input document (one visible regular file under `<inputs>/<case_id>/`) · Eingabedokument · `doc_count` per case; the number · mean documents per case · `mean_docs_per_case`; `n_cases` = the number of cases the source lists (the denominator).
- **Question / hypothesis:** How many input documents does a case carry on average over the cases `data/raw/cases.jsonl` lists? A descriptive count — no expectation beyond "at least one per case".
- **Success / failure criterion:** [C1] `mean_docs_per_case` is one finite number over exactly the `n_cases` cases the source lists, every case counted (`c1_pass`); there is no threshold, the number is the answer.
- **Admissibility condition:** [A1] every listed case has its directory `<inputs>/<case_id>/` with at least one visible document (`a1_pass`) — a case without documents has no "documents per case", and a missing directory would mean the source and the files disagree, so the mean would describe the wrong set.

## Result (after the run — write back, don't go quiet)

- **Answer to the question:** <per registered id its verdict, and the
  run_id; numbers as a small table below the label (one row per arm or
  condition), produced by `analysis/<note>.py --check`, never retyped>
- **Raw output:** <one real prompt+answer pair per finding>

## Setup

- **Data / scope:** `data/raw/cases.jsonl` (N = 12 cases, `antrag-01` … `antrag-12`, each naming `inputs = data/raw/inputs`) and the files under `data/raw/inputs/<case_id>/`; counted by `scripts/01_measure.py`; the whole set in one run, no pilot subset (seconds).
- **Exclusions / filters:** hidden entries (names starting with `.`) and nested directories under a case directory are not counted (`visible()`); nothing else is dropped; no gate labels — no model output.
- **Unit:** one counted thing is one regular, non-hidden file directly under `<inputs>/<case_id>/`, whatever its name or extension; not counted: hidden files, subdirectories and their contents; an empty or missing case directory is a refusal, never a zero.

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
id = "p-3da58c4a121d4883"
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
sentence = "mean_docs_per_case is one finite number over exactly the n_cases cases the source lists, every case counted"
scope = ["scripts/01_measure.py"]
# constants = { <name> = <value> }  # every threshold the sentence names, read with promises.all_constants() — none for a plain count

[[promise]]
id = "A1"
key = "a1_pass"
sentence = "every listed case has its directory <inputs>/<case_id>/ with at least one visible document"
scope = ["scripts/01_measure.py"]
# constants = { <name> = <value> }  # every threshold the sentence names, read with promises.all_constants() — none for a plain count
