# Experiment protocol: docs-per-case

## Summary (after the run, for a person)

- **Result:** A case carries 3.5 input documents on average over the 12 listed cases, every case with at least one document (range 2 to 6).
- **Limits:** Holds for the 12 cases of `data/raw/cases.jsonl` as of this run and counts files, not their content or readability; a single deterministic run.
- **Next step:** none — the number is kept; an agent audit falls due when it goes into a note or steers a decision.

## Intent (before the run)

- **Terms of this protocol:** case (one application, one line of `data/raw/cases.jsonl`) · Fall · `case_id`; input document (one visible regular file under `<inputs>/<case_id>/`) · Eingabedokument · `doc_count` per case; the number · mean documents per case · `mean_docs_per_case`; `n_cases` = the number of cases the source lists (the denominator).
- **Question / hypothesis:** How many input documents does a case carry on average over the cases `data/raw/cases.jsonl` lists? A descriptive count — no expectation beyond "at least one per case".
- **Success / failure criterion:** [C1] `mean_docs_per_case` is one finite number over exactly the `n_cases` cases the source lists, every case counted (`c1_pass`); there is no threshold, the number is the answer.
- **Admissibility condition:** [A1] every listed case has its directory `<inputs>/<case_id>/` with at least one visible document (`a1_pass`) — a case without documents has no "documents per case", and a missing directory would mean the source and the files disagree, so the mean would describe the wrong set.

## Result (after the run — write back, don't go quiet)

- **Answer to the question:** [C1] c1_pass = true, [A1] a1_pass = true — run 2026-10-12T17-34-30_cb32: mean_docs_per_case = 3.5, n_cases = 12 (from `runs/2026-10-12T17-34-30_cb32/metrics.json`; `scripts/01_measure.py --check` holds this line to it).
- **Raw output:** n/a — no model; the per-case rows are `output/docs-per-case.jsonl` (e.g. `antrag-01`: doc_count 4, document-1.txt … document-4.txt).

## Setup

- **Data / scope:** `data/raw/cases.jsonl` (N = 12 cases, `antrag-01` … `antrag-12`, each naming `inputs = data/raw/inputs`) and the files under `data/raw/inputs/<case_id>/`; counted by `scripts/01_measure.py`; the whole set in one run, no pilot subset (seconds).
- **Exclusions / filters:** hidden entries (names starting with `.`) and nested directories under a case directory are not counted (`visible()`); nothing else is dropped; no gate labels — no model output.
- **Unit:** one counted thing is one regular, non-hidden file directly under `<inputs>/<case_id>/`, whatever its name or extension; not counted: hidden files, subdirectories and their contents; an empty or missing case directory is a refusal, never a zero.

## Runs (documented runs — via `runlog`, cite run_ids instead of retyping numbers)

- 2026-10-12T17-34-11_2cca — first run, same number; runlog warned of lock drift (pytest not in requirements.lock), superseded.
- 2026-10-12T17-34-30_cb32 — the reported run, after refreezing requirements.lock: 12 cases, mean 3.5.

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
