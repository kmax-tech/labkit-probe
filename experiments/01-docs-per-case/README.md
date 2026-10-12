# Experiment 01: docs-per-case

*Self-contained: data, scripts, output and this description live here.*

**The one question.** How many input documents does a case carry on average over the cases in `data/raw/cases.jsonl`?

<!-- labkit:route -->
**Trace it.**
- Contract and reported answer: `PROTOCOL-docs-per-case.md`
- Runs and provenance: `runlog .`
- Effective values: `labkit-params .`
- Where the ids are decided: `scripts/01_measure.py:evaluate_rows`
- Immutable record: `config.json` of the chosen run under `runs/`
<!-- /labkit:route -->

## Contract

**What `evaluate_rows()` returns.** <the number under `METRIC_KEY` and per
registered promise its key — from the protocol's [[promise]] sentences: [C1]
c1_pass …, [A1] a1_pass …>. The formula lives once, in `scripts/01_measure.py`;
`--check` and the test call it, `intent-check` and `finalize` hold the ids to
these keys.

**The gates, in order.** `code-check` after every code change · at
`minutes`/`hours`: `preflight` + the preflight audit, then freeze · the run
through `runlog` · `finalize` · number + run_id into the protocol · `01_measure.py --check`.

## State

- [ ] Registration written in the protocol (**before** the first run)
- [ ] the area test green (`.venv/bin/python -m pytest tests/test_01_docs-per-case.py`)
- [ ] Run, `finalize` green, number + run_id in the protocol
