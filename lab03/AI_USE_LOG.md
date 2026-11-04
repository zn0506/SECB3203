# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 3 – Loops and Algorithms for Sequence Quality Control
- Student name: WONG ZI NING
- Matric no: A24CS0313
- Group ID: N/A
- AI level: 1
- Tools cited: OpenAI. (2026). *ChatGPT (GPT-6)* [Large language model]. Retrieved 4 November 2026 from [https://chatgpt.com/](https://chatgpt.com/)

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1 

- Date: 03/11/2026 10:14PM
- Tool: OpenAI. (2026). ChatGPT (GPT-6) [Large language model]. Accessed 3 November 2026 from https://chatgpt.com/
- Purpose: explain
- Prompt: "YES, guide ME through Lab 3 step by step, one action at a time"
- Output: Explained the Lab 3 workflow, project structure, and requirements for T1–T5.
- Verified by: Compared the guidance with the Lab 3 student brief.
- My change: Created the `design` folder and `qc_design.md` file, then began documenting the algorithm.
- Used in: `design/qc_design.md`

## Entry 2 

- Date: 03/11/2026 10:53PM
- Tool: OpenAI. (2026). ChatGPT (GPT-6) [Large language model]. Accessed 3 November 2026 from https://chatgpt.com/
- Purpose: review
- Prompt: "i think i have left sth, can yo review once again the lab3 docx, about the problem,did i state all"
- Output: Identified missing requirements for `qc_summary()` and edge cases for `trim_low_quality()`.
- Verified by: Cross-checked the recommendations against T2, T3, and T4 in the student brief.
- My change: Revised the Problem section to describe inputs, outputs, thresholds, rule priorities, empty inputs and restrictions on modifying records.
- Used in: `design/qc_design.md` — Problem

## Entry 3 

- Date: 03/11/2026 11:12PM
- Tool: OpenAI. (2026). ChatGPT (GPT-6) [Large language model]. Accessed 3 November 2026 from https://chatgpt.com/
- Purpose: review
- Prompt: "check #Pseudocode section first, if there is no wrong, guide me through the flowchart"
- Output: Reviewed the classification and trimming algorithms and confirmed their decision order and boundary conditions.
- Verified by: Compared the pseudocode against the Lab 3 requirements and Week 3 lecture slides.
- My change: Finalized pseudocode using named thresholds, conditional statements, early returns and a bounded trimming loop.
- Used in: `design/qc_design.md` — Pseudocode

## Entry 4 

- Date: 03/11/2026 12:01AM
- Tool: OpenAI. (2026). ChatGPT (GPT-6) [Large language model]. Accessed 3 November 2026 from https://chatgpt.com/
- Purpose: review
- Prompt: "can help me check my flowchart?"
- Output: Suggested simplifying the second classification decision label and checked the trimming loop's flow.
- Verified by: Compared the flowcharts with my pseudocode and the required algorithm order.
- My change: Simplified the Mermaid decision label while keeping the existing branches and loop logic.
- Used in: `design/qc_design.md` — Flowchart

## Entry 5 

- Date: 04/11/2026 10:32AM
- Tool: OpenAI. (2026). ChatGPT (GPT-6) [Large language model]. Accessed 4 November 2026 from https://chatgpt.com/
- Purpose: debug
- Prompt: Shared pytest output showing two failures with `KeyError: 'gc'`.
- Output: Explained that the CSV uses `gc_percent` rather than `gc`, and that CSV text values require numeric conversion.
- Verified by: Compared the CSV column names with the code and reran pytest after corrections.
- My change: Changed the GC field lookup to `record["gc_percent"]` and used `int()` and `float()` for numeric conversions.
- Used in: `src/qc.py` — `qc_summary()`

## Entry 6 

- Date: 04/11/2026 10:54AM
- Tool: OpenAI. (2026). ChatGPT (GPT-6) [Large language model]. Accessed 4 November 2026 from https://chatgpt.com/
- Purpose: review
- Prompt: Shared my `qc_summary()` implementation for checking after correcting the CSV conversions.
- Output: Suggested removing unnecessary `record.get(...)` threshold overrides because `classify_read()` already defines the default thresholds.
- Verified by: Reran `python -m pytest -q tests/test_visible.py` and obtained 7 passing tests.
- My change: Removed the three `record.get(...)` overrides from the `classify_read()` call.
- Used in: `src/qc.py` — `qc_summary()`

## Entry 7 

- Date: 04/11/2026 11:36AM
- Tool: OpenAI. (2026). ChatGPT (GPT-6) [Large language model]. Accessed 4 November 2026 from https://chatgpt.com/
- Purpose: debug / explain
- Prompt: Shared my original `trim_low_quality()` function that used `for i, qual in enumerate(quals)`.
- Output: Explained that checking from left to right incorrectly stops at internal low-quality scores. Guided me through implementing a right-to-left `while` loop.
- Verified by: Checked the algorithm against the Lab 3 examples and ran pytest.
- My change: Replaced the forward scan with a bounded while-loop that decreases `end` while the trailing scores are below the threshold.
- Used in: `src/qc.py` — `trim_low_quality()`

## Entry 8 

- Date: 04/11/2026 11:43AM
- Tool: OpenAI. (2026). ChatGPT (GPT-6) [Large language model]. Accessed 4 November 2026 from https://chatgpt.com/
- Purpose: review / debug
- Prompt: Shared my `test_length_boundary()`, `test_n_count_boundary()`, and `test_trim_low_quality()` test functions for checking.
- Output: Identified an incorrect expected classification for a read with GC 10.0 and explained the correct review decision. Also checked the N-count and trimming tests.
- Verified by: Executed `python -m pytest -q` and obtained 10 passing tests.
- My change: Corrected the expected classification, completed the N-count boundary test, added trimming tests, and imported both required functions.
- Used in: `tests/test_lab03_own.py`

## Entry 9 

- Date: 04/11/2026 12:01PM
- Tool: OpenAI. (2026). ChatGPT (GPT-6) [Large language model]. Accessed 4 November 2026 from https://chatgpt.com/
- Purpose: explain
- Prompt: Shared my terminal error after entering "All checks passed!" as a PowerShell command.
- Output: Explained the difference between a terminal command and its expected output and identified the correct Ruff command.
- Verified by: Executed `ruff check src` and received "All checks passed!".
- My change: Correctly ran the Ruff code-style check.
- Used in: Lab 3 code-quality verification

