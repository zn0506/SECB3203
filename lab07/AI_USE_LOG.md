# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: LAB 7
- Student name: WONG ZI NING
- Matric no: A24CS0313
- Group ID: n/a
- AI level: 1
- Tools cited: OpenAI (2026). ChatGPT (GPT-6.2). Retrieved 27 November 2026 from https://chat.openai.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 27 November 2026
- Tool: OpenAI (2026). ChatGPT (GPT-6.2). Retrieved 27 November 2026 from https://chat.openai.com
- Purpose: debug
- Prompt: check my T1 output
- Output: Explained that the failed test was caused by the unimplemented len method rather than the T1 implementation. Suggested additional read-only property checks.
- Verified by: Reviewed the pytest traceback and identified the NotImplementedError.
- My change: Kept the T1 implementation unchanged.
- Used in: T1 testing and debugging.

## Entry 2

- Date: 27 November 2026
- Tool: OpenAI (2026). ChatGPT (GPT-6.2). Retrieved 27 November 2026 from https://chat.openai.com
- Purpose: debug
- Prompt: Why am I getting ModuleNotFoundError when testing the read-only properties? Can you explain how to resolve this error?
- Output: Explained the Python module search path and how to configure PYTHONPATH in PowerShell.
- Verified by: Ran the commands in the PowerShell terminal.
- My change: Configured PYTHONPATH without modifying the original imports.
- Used in: Terminal environment configuration.

## Entry 3

- Date: 27 November 2026
- Tool: OpenAI (2026). ChatGPT (GPT-6.2). Retrieved 27 November 2026 from https://chat.openai.com
- Purpose: review
- Prompt: Can you review my T2 pytest results and manual testing outputs to check whether my DNASequence methods behave as expected?
- Output: Confirmed that the GC percentage, reverse complement, motif positions, sequence length and classmethod outputs matched the expected results.
- Verified by: Three visible tests passed, and all five manual testing outputs matched the expected values.
- My change: No further changes were required based on the review.
- Used in: src/models.py — DNASequence methods.

## Entry 4

- Date: 27 November 2026
- Tool: OpenAI (2026). ChatGPT (GPT-6.2). Retrieved 27 November 2026 from https://chat.openai.com
- Purpose: review
- Prompt (paraphrased): Can you check my T3 outputs and explain whether the representation, equality and hashing methods are working correctly?
- Output: Explained how object representation, value equality and consistent hashing allow DNASequence objects to work in sets and dictionaries.
- Verified by: Manual equality, representation, set and dictionary tests, together with pytest.
- My change: No further changes were required based on the review.
- Used in: src/models.py — __repr__(), __eq__() and __hash__().

## Entry 5

- Date: 27 November 2026
- Tool: OpenAI (2026). ChatGPT (GPT-6.2). Retrieved 27 November 2026 from https://chat.openai.com
- Purpose: explain
- Prompt Can you explain the difference between composition and inheritance and why BiologicalSample contains a DNASequence object?
- Output: Explained the has-a relationship, independent result dictionaries, encapsulation and the purpose of returning dictionary copies.
- Verified by: Reviewed the class structure and compared it with the lab requirements.
- My change: Reviewed my understanding of the relationship between the three classes.
- Used in: Understanding BiologicalSample and SampleCollection.

## Entry 6
- Date: 27 November 2026
- Tool: OpenAI (2026). ChatGPT (GPT-6.2). Retrieved 27 November 2026 from https://chat.openai.com
- Purpose: explain
- Prompt: Can you explain the differences between normal, boundary and invalid-input tests, including how pytest.raises works?
- Output: Explained the purpose of different test categories and how expected exceptions are checked using pytest.
- Verified by: Reviewed the test conditions and expected behavior.
- My change: Reviewed the coverage of the test cases.
- Used in: Understanding tests/test_lab07_models.py.


