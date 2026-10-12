# Experiment protocol: docs-per-case

## Summary (after the run, for a person)

- **Result:** A case carries 3.5 input documents on average over the 12 cases; the bar set before the run (one number over every listed case, every case non-empty) was met.
- **Limits:** Twelve fixture cases in one deterministic run; counts files, not their content, so an empty or duplicate file counts as a document.
- **Next step:** none — the number is kept; the agent audit falls due when it is cited in a note or steers a decision.

## Intent (before the run)

- **Terms of this protocol:** case (one application, a line of `data/raw/cases.jsonl`) · case · `case_id`; input document (a visible regular file directly under `<inputs>/<case_id>/`) · document · `docs` (the per-row count, `COUNT_FIELD`); mean documents per case · the number · `mean_docs_per_case` (`METRIC_KEY`); `inputs` = the directory each case line names, relative to the repo root. Nothing else coined.
- **Question / hypothesis:** How many input documents does a case carry on average — the mean over all cases in `data/raw/cases.jsonl` of the number of files under `<inputs>/<case_id>/`? Descriptive: no expectation beyond "a single positive number over every case".
- **Success / failure criterion:** [C1] `mean_docs_per_case` is one number over exactly the ids `cases.jsonl` lists (every case has a row, the denominator is the source's id list) and is greater than zero. There is no threshold; the number is descriptive and its value is the result.
- **Admissibility condition:** [A1] Every case directory exists and holds at least one visible document — a missing or empty case is refused by `rows()` before any number is written, because a zero from a missing directory would be an instrument failure (a wrong path) indistinguishable from an empty case and would pull the mean down silently.

## Result (after the run — write back, don't go quiet)

- **Answer to the question:** run `2026-10-12T18-05-53_a5bc` — `mean_docs_per_case` = 3.5 over `n_cases` = 12; [C1] `c1_pass` = true (one number over exactly the 12 listed ids, > 0); [A1] `a1_pass` = true (every case directory holds at least one visible document; per-case counts in `output/docs-per-case.jsonl`: 2 to 6).

## Setup

- **Data / scope:** `data/raw/cases.jsonl` (12 cases, `antrag-01` … `antrag-12`, each with `inputs = data/raw/inputs`) and the fixture directories under `data/raw/inputs/<case_id>/`; counted by `scripts/01_measure.py`. Full set at once — no pilot subset at cost seconds.
- **Exclusions / filters:** none from the case list; inside a case directory only visible regular files count (`visible()`): hidden entries (names starting with `.`) and nested directories are not documents. No output gets a gate label — a plain count.
- **Unit:** one counted thing = one visible regular file directly under `<inputs>/<case_id>/`, whatever its name or extension; not counted: hidden files, nested directories and their contents, the case line itself; an empty or missing case directory is a refusal, not a count of 0.

## Runs (documented runs — via `runlog`, cite run_ids instead of retyping numbers)

- `2026-10-12T18-05-53_a5bc` — the one counting run over all 12 cases, at commit 7f1f98a; the reported run.

## Head (read by the checks)



*How to fill each field, the cuts by tier and the intent ids:
`protocol-field-guide.md` (`protocol-check --guide`); which fields this
protocol's `cost` owes, and which fall due after a documented run:
`protocol-check --contract` — the one list, never retyped here; fill by
label with `protocol-fill PROTOCOL-<name>.md "<label>" "<value>"`.*

```toml
[protocol]
standard = "0.19"
id = "p-6528effe1d4e41bd"
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
sentence = "mean_docs_per_case is one number over exactly the ids cases.jsonl lists and is greater than zero"
scope = ["scripts/01_measure.py"]
# constants = { <name> = <value> }  # every threshold the sentence names, read with promises.all_constants() — none for a plain count

[[promise]]
id = "A1"
key = "a1_pass"
sentence = "every case directory exists and holds at least one visible document; a missing or empty case is refused before any number is written"
scope = ["scripts/01_measure.py"]
# constants = { <name> = <value> }  # every threshold the sentence names, read with promises.all_constants() — none for a plain count
