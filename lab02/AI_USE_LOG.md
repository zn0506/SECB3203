# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 02 - Biological sequences as strings
- Student name: WONG ZI NING
- Matric no: A24CS0313
- Group ID: N/A
- AI level: 1
- Tools cited: OpenAI (2026). ChatGPT (GPT-6). Retrieved 3 November 2026 from https://chatgpt.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1
- Date: 2/11/2026 4:36PM
- Tool: OpenAI (2026). ChatGPT (GPT-6). Retrieved 2 November 2026 from https://chatgpt.com
- Purpose: explain
- Prompt: CAN EXPLAIN THE CONCEPT OF CLEAN SEQUENCE()
- Output: AI explained the purpose of `clean_sequence()`, including how to process a DNA sequence by removing spaces, digits, and newline characters and converting letters to uppercase. It also explained how to use a loop and string methods to implement the function.
- Verified by: I manually tested the function using Python commands in the VS Code terminal:
  ```
  clean_sequence("aT 12gcN")
  clean_sequence("")
  clean_sequence("atg\n c2t")
  ```
  The outputs were `"ATGCN"`, `""`, and `"ATGCT"`, respectively.
- My change: I used the AI explanation to understand the logic and wrote my own implementation using a `for` loop, `.isalpha()` and `.upper()`. I then tested the function with different inputs.
- Used in: `src/lab02_sequences.py` - `clean_sequence()`

## Entry 2
- Date: 3/11/2026 10:38AM
- Tool: OpenAI (2026). ChatGPT (GPT-6). Retrieved 3 November 2026 from https://chatgpt.com
- Purpose: review
- Prompt: EXPLAIN IF BELOW IMPLEMENTATION IS CORRECT OR NOT:
  ```python
  if not motif:
      raise ValueError("Motif cannot be empty")
  ```
- Output: AI explained that raising a `ValueError` for an empty motif is a reasonable design choice because searching for an empty pattern can be ambiguous. 
- Verified by: I manually tested the implementation using the VS Code PowerShell terminal:
  ```powershell
  python -c "from src.lab02_sequences import find_motif; print(find_motif('ATGC', ''))"
  ```
  The program raised `ValueError: Motif cannot be empty`, confirming that the error handling works as implemented.
- My change: I retained the `ValueError` handling because it prevents an empty motif from being processed. I verified that the function raises the intended exception.
- Used in: `src/lab02_sequences.py` - `find_motif()`