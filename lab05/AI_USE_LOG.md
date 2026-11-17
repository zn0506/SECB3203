# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 5
- Student name: Wong Zi Ning
- Matric no: A24CS0313
- Group ID: n/a
- AI level: 1
- Tools cited: OpenAI (2026). ChatGPT (GPT-6) [Large language model]. Accessed 16 November 2026 from https://chatgpt.com/

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 16 November 2026 11:18AM
- Tool: OpenAI (2026). ChatGPT (GPT-6) [Large language model]. Accessed 16 November 2026 from https://chatgpt.com/
- Purpose: explain
- Prompt: EXPLAIN THE LAB INSTRUCTION
- Output: ChatGPT explained the Lab 05 objectives, requirements for Tasks T1–T5, and the expected project structure. It also outlined a step-by-step workflow covering Python environment setup, function implementation, testing, documentation, and submission.
- Verified by: Compared ChatGPT's explanation with the official SECB3203 Lab 05 student brief and checked the starter files to confirm the required functions and tasks.
- My change: I used the explanation to understand the lab requirements and organize my work into smaller steps. I followed the lecturer's task order and implemented the Python functions myself.
- Used in: Lab 05 project setup and planning for Tasks T1–T5, including src/sequence_utils.py, src/normalize.py, and tests/test_lab05_own.py.

## Entry 2

- Date: 16 November 2026 12:13PM
- Tool: OpenAI (2026). ChatGPT (GPT-6) [Large language model]. Accessed 16 November 2026 from https://chatgpt.com/
- Purpose: review
- Prompt:
def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    return "".join(c for c in raw.upper() if c in DNA_BASES and c.isalpha() and not c.isdigit() and not c.isspace())
- Output: ChatGPT identified that the condition c in DNA_BASES incorrectly removed alphabetic characters such as N and X. It explained that .isalpha() was sufficient to retain letters while excluding digits and whitespace.
- Verified by: Reviewed the Lab 05 function requirements, corrected the implementation, and ran the lecturer's visible pytest test to verify that clean_sequence() worked correctly.
- My change: I removed the unnecessary c in DNA_BASES, not c.isdigit(), and not c.isspace() conditions, keeping .isalpha() to filter the characters.
- Used in: src/sequence_utils.py — clean_sequence() function.

## Entry 3
- Date: 16 November 2026 5:40PM
- Tool: OpenAI (2026). ChatGPT (GPT-6) [Large language model]. Accessed 16 November 2026 from https://chatgpt.com/
- Purpose: explain
- Prompt: EXPLAIN THE CONCEPT OF CPM
- Output: ChatGPT explained that CPM (Counts Per Million) is a normalization method used in bioinformatics to adjust raw counts according to library size. It described the formula CPM = (count / library_size) × 1,000,000 and explained how it allows counts from samples with different library sizes to be compared.
- Verified by: Compared the CPM formula and example calculations with the Lab 05 instructions and tested the cpm() function using Python.
- My change: I used the explanation to understand how CPM normalization works and applied the formula in my own implementation. I also included validation to raise ValueError when the library size is zero or negative.
- Used in: src/normalize.py — cpm() function.
<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry 3 ... -->
