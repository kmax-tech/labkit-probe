# Experiment 01: docs-per-case

*Self-contained: data, scripts, output and this description live here.*

**The one question** is the protocol's Question field (`PROTOCOL-docs-per-case.md`);
a count asks one and reports one number.

<!-- labkit:route -->
**Trace it.**
- Contract and reported answer: `PROTOCOL-docs-per-case.md`
- Runs and provenance: `runlog .`
- Effective values: `labkit-params .`
- Where the ids are decided: `scripts/01_measure.py:evaluate_rows`
- Immutable record: `config.json` of the chosen run under `runs/`
<!-- /labkit:route -->

## Contract

**What `evaluate_rows()` returns.** The number under `METRIC_KEY` of
`scripts/01_measure.py`; a count registers no ids. The formula lives once, there;
`--check` and the test call it, and `finalize` holds the protocol's Answer line
to the run's `metrics.json`.

**The gates, in order.** `code-check` after every code change · at
`minutes`/`hours`: `preflight` + the preflight audit, then freeze · the run
through `runlog` · `finalize` · `protocol-fill --from-run` writes the number back · `01_measure.py --check`.

## State

- [ ] Registration written in the protocol (**before** the first run)
- [ ] the area test green (`.venv/bin/python -m pytest tests/test_01_docs_per_case.py`)
- [ ] Run, `protocol-fill --from-run`, `finalize` green
