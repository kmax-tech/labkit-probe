19:11:30 · read · read experiments/01-docs-per-case area files
19:11:33 · read · read PROTOCOL-docs-per-case.md
19:11:33 · read · read area README.md
19:11:33 · read · read measure script
19:11:37 · run · protocol-fill --list to name open fields
19:11:40 · read · read area test file
19:11:41 · read · read cases and inputs for hidden or odd files
19:11:49 · edit · fill protocol head and intent fields by label
19:12:00 · run · code-check on the area
19:12:00 · run · area test file
19:12:05 · run · create branch probe-count
19:12:05 · run · git status before commit
19:12:05 · edit · commit the registration and the measure script
19:12:08 · run · run the count through runlog (01_measure.py)
19:12:11 · edit · write run number back into protocol from metrics.json
19:12:11 · run · recheck the number from kept rows
19:12:14 · run · finalize the area
19:12:34 · edit · commit output, runs and protocol, with the step log
19:12:35 · run · push branch probe-count to origin
19:12:42 · run · push branch probe-count to origin (after amending the last commit with the log)
