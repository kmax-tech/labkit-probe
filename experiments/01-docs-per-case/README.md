# Experiment 01: docs-per-case

*Self-contained: data, scripts, output and this description live here.*

**The one question.** How many input documents does a case in `data/raw/cases.jsonl` carry on average?

<!-- labkit:route -->
**Trace it.**
- Contract and reported answer: `PROTOCOL-docs-per-case.md`
- Runs and provenance: `runlog .`
- Effective values: `labkit-params .`
- Where the ids are decided: `scripts/01_measure.py:evaluate_rows`
- Immutable record: `config.json` of the chosen run under `runs/`
<!-- /labkit:route -->

## Contract

**What `evaluate_rows()` returns.** `{"mean_docs_per_case": <sum of per-case document counts / number of cases>}` — no ids registered, a plain count. The formula lives once, in `scripts/01_measure.py`;
`--check` and the test call it, `intent-check` and `finalize` hold the ids to
these keys.

**The gates, in order.** `code-check` after every code change · at
`minutes`/`hours`: `preflight` + the preflight audit, then freeze · the run
through `runlog` · `finalize` · number + run_id into the protocol · `01_measure.py --check`.

## State

- [x] Registration written in the protocol (**before** the first run)
- [x] the area test green (`.venv/bin/python -m pytest tests/test_01_docs-per-case.py`)
- [x] Run, `finalize` green, number + run_id in the protocol
