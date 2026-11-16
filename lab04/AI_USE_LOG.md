# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 4
- Student name: Wong Zi Ning
- Matric no: A24CS0313
- Group ID: n/a
- AI level: 1
- Tools cited: OpenAI. (2026). ChatGPT (GPT-6). Retrieved 16 November 2026 from https://chatgpt.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 16 November 2026, 12:10 AM
- Tool: OpenAI. (2026). ChatGPT (GPT-6). Retrieved 16 November 2026 from https://chatgpt.com
- Purpose: explain
- Prompt: Lab 04 T1 Check my answer and guide me through the next action only, following AI Level 1.
- Output: AI explained how filter_panel() selects genes using a priority set while preserving the original order and duplicate genes. It also provided hints about list comprehension.
- Verified by: Reviewed the Week 4 lecture notes and ran python -m pytest -q. All 9 tests passed.
- My change: Used the explanation to understand list comprehension and implemented filter_panel() while preserving duplicates and the original list.
- Used in: src/panel.py — filter_panel()

## Entry 2

- Date: 16 November 2026, 12:43 AM
- Tool: OpenAI. (2026). ChatGPT (GPT-6). Retrieved 16 November 2026 from https://chatgpt.com
- Purpose: tests-plan
- Prompt: Lab 04 T5 Check my answer and guide me through writing Test 3 following AI Level 1.
- Output: AI explained the boundary cases for kmer_counts(), including when k exceeds the DNA sequence length and when the input sequence is empty. It provided guidance on writing pytest assertions with the expected empty dictionary {}.
- Verified by: Ran python -m pytest -q tests/test_lab04_own.py and confirmed that all 4 own tests passed.
- My change: Corrected the test inputs to use DNA strings instead of lists and used {} as the expected result for both boundary cases.
- Used in: tests/test_lab04_own.py — test_kmer_boundary()

## Entry 3

- Date: 16 November 2026, 1:40 AM
- Tool: OpenAI. (2026). ChatGPT (GPT-6). Retrieved 16 November 2026 from https://chatgpt.com
- Purpose: review
- Prompt: Help me check my def test_safe_expression()
- Output: AI reviewed my test and explained how to verify that a missing gene returns None, a real expression value of 0.0 is preserved, and the missing gene is not added to the dictionary.
- Verified by: Ran python -m pytest -q tests/test_lab04_own.py and python -m pytest -q. All 4 own tests and 9 total tests passed.
- My change: Updated the test to check TP53 with a value of 0.0, verify that EGFR returns None, and confirm that EGFR was not added to the dictionary.
- Used in: tests/test_lab04_own.py — test_safe_expression()