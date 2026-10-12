17:32:31 · read · TASK.md (already read), CLAUDE.md in context; starting
17:32:31 · run · git checkout -b probe-count
17:32:31 · run · check .venv works (labkit version)
17:32:36 · read · experiments/01-docs-per-case/ tree, README, protocol, scripts; data/raw/cases.jsonl head; .githooks; tests/
17:32:41 · read · PROTOCOL-docs-per-case.md (103), scripts/01_measure.py (97), tests/test_01_docs_per_case.py, .githooks/pre-commit, .claude/settings.json, cases.jsonl full
17:32:48 · run · protocol-check --contract; git hooksPath; protocol-fill --help
17:33:31 · edit · scripts/01_measure.py: SOURCE, COUNT_FIELD, METRIC_KEY, expected_ids, rows, evaluate_rows
17:33:31 · run · pytest tests/test_01_docs_per_case.py + code-check .
17:33:47 · run · protocol-fill --list
17:33:48 · edit · PROTOCOL: Terms, Question, Criterion, Admissibility, Data/scope, Exclusions, Unit via protocol-fill
17:33:56 · gate · post-change hook: [protocol] type missing, runs line still template → fill head + promise sentences
17:33:56 · edit · PROTOCOL head: type = exploratory, [[promise]] sentences C1/A1
17:34:06 · edit · README.md of the area: the one question, contract line
17:34:06 · run · git commit (area filled, before the run)
