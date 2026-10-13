08:28:31 · read · TASK.md, git status, ls, .venv/bin listing
08:28:31 · read · experiments/01-docs-per-case tree + files
08:28:39 · read · data/raw/cases.jsonl head, inputs dir listing, .gitignore, tests/
08:28:47 · read · all cases rows, per-case input listing incl. hidden/nested, tests/test_01_docs_per_case.py
08:28:47 · run · protocol-check --contract
08:29:17 · run · git checkout -b probe-count
08:29:17 · edit · scripts/01_measure.py — SOURCE/OUT/COUNT_FIELD/METRIC_KEY + expected_ids, rows, evaluate_rows
08:29:33 · run · pytest tests/test_01_docs_per_case.py
08:29:34 · edit · PROTOCOL head type=exploratory + protocol-fill Terms/Question/Data/Exclusions/Unit
08:29:47 · edit · README.md one-question sentence
08:29:47 · run · code-check experiments/01-docs-per-case ; protocol-check
08:29:55 · run · protocol-check PROTOCOL-docs-per-case.md
08:30:05 · run · git commit registration + script + README (before the run, LAB-010)
08:30:13 · run · 01_measure.py — the run (foreground, instrument check too)
08:30:31 · run · protocol-fill --from-run 2026-10-13T08-30-13_be11 ; inspect runs/ dir
08:30:51 · read · runs/.../uncommitted.patch + git status after the run
08:30:51 · edit · README state checkboxes
08:30:51 · run · git commit output/ runs/ protocol README (finalize wants them in git)
08:31:00 · run · finalize experiments/01-docs-per-case (read the warning)
08:31:11 · gate · finalize warns README.md:19 placeholder — fill the Contract line
08:31:11 · edit · README.md Contract line
08:31:12 · run · 01_measure.py --check
08:31:24 · edit · README last state checkbox
08:31:24 · run · finalize again (warning gone?) + full pytest
08:31:42 · run · final commit incl. git add -f log.md, then push probe-count
