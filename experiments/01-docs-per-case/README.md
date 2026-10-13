# Experiment 01: docs-per-case

*Self-contained: data, scripts, output and this description live here.*

**The one question.** What is the mean number of input documents per case over
the cases in `data/raw/cases.jsonl`?

<!-- labkit:route -->
**Trace it.**
- Contract and reported answer: `PROTOCOL-docs-per-case.md`
- Runs and provenance: `runlog .`
- Effective values: `labkit-params .`
- Where the ids are decided: `scripts/01_measure.py:evaluate_rows`
- Immutable record: `config.json` of the chosen run under `runs/`
<!-- /labkit:route -->

## Contract

**What `evaluate_rows()` returns.** One key, `mean_docs_per_case`: the sum of
the per-case document counts (`n_docs`) divided by the number of cases the
source lists; no ids are registered. The formula lives once, in `scripts/01_measure.py`;
`--check` and the test call it, `intent-check` and `finalize` hold the ids to
these keys.

**The gates, in order.** `code-check` after every code change · at
`minutes`/`hours`: `preflight` + the preflight audit, then freeze · the run
through `runlog` · `finalize` · `protocol-fill --from-run` writes the number back · `01_measure.py --check`.

## State

- [x] Registration written in the protocol (**before** the first run)
- [x] the area test green (`.venv/bin/python -m pytest tests/test_01_docs-per-case.py`)
- [x] Run, `protocol-fill --from-run`, `finalize` green
