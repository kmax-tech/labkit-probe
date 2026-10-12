# Experiment protocol: docs-per-case

## Summary (after the run, for a person)

- **Result:** A case carries 3.5 input documents on average (12 cases, 42 documents; between 2 and 6 per case). Every listed case had a directory with at least one document, so the count is over the whole list.
- **Limits:** A fixture of 12 cases, counted once; file count only — nothing about what the documents contain or whether a file is a usable document.
- **Next step:** none — a descriptive count; the agent audit falls due when the number goes into a note or steers a decision.

## Intent (before the run)

- **Terms of this protocol:** case (one application, a line of `cases.jsonl`) · Fall · `case_id`; document (one visible file under `<inputs>/<case_id>/`) · Dokument · `doc_count` per case; the kept number · mean docs per case · `mean_docs_per_case`
- **Question / hypothesis:** How many input documents does a case carry on average over the cases in `data/raw/cases.jsonl`? No expectation registered — a descriptive count.
- **Success / failure criterion:** [C1] `mean_docs_per_case` is one finite number over exactly the cases the source lists (rows == ids); nothing more is promised for a plain count (→ LAB-003, LAB-004).
- **Admissibility condition:** [A1] every listed case has a directory with at least one visible document — a missing or empty case would make the mean a number over a different population than the file lists, so the script refuses instead of counting 0.

## Result (after the run — write back, don't go quiet)

- **Answer to the question:** run 2026-10-12T18-19-07_7d0d — `mean_docs_per_case` = 3.5 over `n_cases` = 12 cases (42 documents); [C1] `c1_pass` = true, [A1] `a1_pass` = true. Per case (`doc_count`): antrag-01 4 · 02 4 · 03 3 · 04 4 · 05 4 · 06 3 · 07 2 · 08 3 · 09 4 · 10 3 · 11 2 · 12 6 — from `output/docs-per-case.jsonl`, held by `01_measure.py --check`.

## Setup

- **Data / scope:** `data/raw/cases.jsonl` (N = 12 cases, field `inputs` names the directory relative to the repo root), documents under `data/raw/inputs/<case_id>/`; fixture shipped with the repo, no producer script; no pilot subset — one deterministic pass over all cases.
- **Exclusions / filters:** hidden entries (names starting with `.`) and nested directories are not documents (`visible()`); nothing else is dropped; no gate labels — no model in the loop.
- **Unit:** one document = one regular, non-hidden file directly under `<inputs>/<case_id>/`; not counted: hidden files, nested directories and their contents; an empty or missing case directory is a refusal, never a 0.

## Runs (documented runs — via `runlog`, cite run_ids instead of retyping numbers)

- 2026-10-12T18-18-42_ba22 — first pass, same number; lock hash had drift:1 (labkit commit in the lock differed from the installed one), superseded.
- 2026-10-12T18-19-07_7d0d — the reported run: all 12 cases counted after the lock was refrozen, drift:0.

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
