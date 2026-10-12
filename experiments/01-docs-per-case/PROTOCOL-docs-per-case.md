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

- **Terms of this protocol:** <first, because the question uses
  them: one line per house word — *everyday word · house term · code word*
  ("gap case (a case only an uncovered rule can reject) · Lückenfall ·
  `GAP_CASES`"); look up before coining (the field's established term, then
  `notes/theorie/terms.md`, then the lab standard's vocabulary table);
  "n/a — standard vocabulary" only if nothing is coined>
- **Question / hypothesis:** <the one question — what do we expect?>
- **Success / failure criterion:** <how do we recognise whether it worked?
  One id per conjunct, written `[C…]` with its number in the brackets
  (C1 → the key `c1_pass`), each reappearing as a lowercase key in the reportable
  run's metrics.json; where a number stands, name its constant from the
  [[promise]] table ("in at least `min_draws` = 2 of 3 draws") — the one
  word that links this sentence, the table and the script (a person
  reading German prose and English code found no link, round 15); a
  house term used here for the first time carries its everyday word once
  in parentheses ("over the three draws (passes) of the arm (profile)
  `after`") — Terms below is the home of the definition, this line its
  first use (LAB-092 Term layering)
  (→ LAB-003 No run without an intent paragraph, LAB-004 Identifiers make the intent addressable)>
- **Admissibility condition:** <what must hold in the same run before
  any verdict is issued — yield, coverage, a control showing its expected
  value; one A per condition, each with WHY its failure makes the measurement
  uninterpretable (not merely less likely to succeed — a threshold the
  hypothesis needs is a C, never an A); if one fails, there is no C verdict,
  only the finding that the instrument failed; what is still read
  descriptively is labelled so (→ LAB-004 Identifiers make the intent addressable)>

## Result (after the run — write back, don't go quiet)

- **Answer to the question:** <per registered id its verdict, and the
  run_id; numbers as a small table below the label (one row per arm or
  condition), produced by `analysis/<note>.py --check`, never retyped>
- **Raw output:** <one real prompt+answer pair per finding>

## Setup

- **Data / scope:** <source, N, producer script; pilot subset first>
- **Exclusions / filters:** <what is dropped from the data or output and why;
  which outputs get no gate label — "none" if nothing is excluded>
- **Unit:** <what one counted or judged thing is — and what is not:
  hidden files, nested directories, empty cases, a second answer line>

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
type = "<exploratory | confirmatory>"
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
sentence = "<the criterion in one sentence: registered accuracy >= null accuracy + margin>"
scope = ["scripts/01_measure.py"]
# constants = { <name> = <value> }  # every threshold the sentence names, read with promises.all_constants() — none for a plain count

[[promise]]
id = "A1"
key = "a1_pass"
sentence = "<the yield condition: at most max_empty empty or unreadable answers on the registered lane>"
scope = ["scripts/01_measure.py"]
# constants = { <name> = <value> }  # every threshold the sentence names, read with promises.all_constants() — none for a plain count
