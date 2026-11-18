# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 6
- Student name: Wong Zi Ning
- Matric no: A24CS0313
- Group ID: n/a
- AI level: 1
- Tools cited: OpenAI (2026). ChatGPT (GPT-6). Accessed 18 November 2026, https://chatgpt.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 18 November 2026, 12:52AM
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 18 November 2026, https://chatgpt.com
- Purpose: explain
- Prompt: EXPLAIN LAB06 AND GUIDE ME STEP BY STEP
- Output: AI explained the Lab 06 requirements, including FASTA, CSV, FASTQ, exception handling, batch processing, logging, testing and submission procedures.
- Verified by: Compared guidance with the Lab 06 student brief.
- My change: Used the explanations to understand the tasks and organize my implementation process.
- Used in: Lab 06 preparation and planning for T1-T5.

## Entry 2

- Date: 18 November 2026, 1:22AM
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 18 November 2026, https://chatgpt.com
- Purpose: review
- Prompt: Shared my implementations of _finish(), read_fasta(), read_csv_records(), and write_csv() for review.
- Output: AI reviewed my code, explained FASTA header validation, CSV newline handling, and how to use pathlib and custom exceptions.
- Verified by: Ran pytest for FASTA and CSV reading, manually tested CSV writing, and checked code quality using Ruff.
- My change: Corrected empty-header validation, added newline="" for CSV reading, and used Path(path).open() for file handling.
- Used in: src/bio_io.py - T1 and T2.

## Entry 3

- Date: 18 November 2026, 2:59AM
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 18 November 2026, https://chatgpt.com
- Purpose: debug
- Prompt: Shared my process_directory(), read_fastq(), mean_phred(), and main() implementations and their test results for review and debugging.
- Output: AI explained per-file exception handling, logging cleanup, FASTQ validation, Phred calculations, argparse configuration, and command-line exit codes.
- Verified by: Ran the batch-processing command, checked processing_log.csv and batch.log, confirmed exit code 1, and passed the lecturer's visible tests.
- My change: Added FASTQ blank-line handling, sequence-quality length validation, corrected the command-line arguments, and verified batch-processing output.
- Used in: src/batch.py - T3 and T4.

## Entry 4

- Date: 18 November 2026, 12:59AM
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 18 November 2026, https://chatgpt.com
- Purpose: tests-plan
- Prompt: Shared my pytest test functions and terminal results for review while completing T5.
- Output: AI explained the tmp_path fixture, pytest exception testing, test discovery, and how to troubleshoot file-location and Python interpreter issues.
- Verified by: Ran python -m pytest -v with 9 tests passing and ruff check src with all checks passing.
- My change: Created four tests covering an empty FASTA file, a missing FASTA file, a FASTA record without a sequence, and an empty input directory.
- Used in: tests/test_lab06_own.py - T5.
