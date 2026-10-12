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
17:34:10 · run · the run: .venv/bin/python experiments/01-docs-per-case/scripts/01_measure.py
17:34:21 · gate · runlog warns: 5 packages deviate from requirements.lock → inspect run dir and pip freeze
17:34:21 · read · runs/<id>/ files, pip freeze vs requirements.lock
17:34:29 · edit · requirements.lock refrozen (pip freeze) — drift was pytest + deps named in requirements.txt
17:34:30 · run · rerun 01_measure.py against the refrozen lock (the rerun is the instrument check)
17:34:45 · edit · PROTOCOL: Answer, Raw output, Result, Limits, Next step, Runs line (run 2026-10-12T17-34-30_cb32)
17:34:45 · run · finalize experiments/01-docs-per-case; 01_measure.py --check
17:34:59 · edit · README state boxes ticked
17:34:59 · unsure · CLAUDE.md lane seconds names --show 2 and --probe; the seconds skeleton has neither flag — skipped both
17:34:59 · unsure · C1 for a plain count: no threshold exists, registered as 'the mean over exactly the listed cases'
17:34:59 · run · git commit (number, runs/, output/, lock, log.md) then git push -u origin probe-count
