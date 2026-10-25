# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: <e.g. Lab 4>
- Student name: <full name>
- Matric no: <matric>
- Group ID: <group work only, else n/a>
- AI level: <0, 1 or 2 - see the assessment brief>
- Tools cited: <UTM format, e.g. OpenAI (2026). ChatGPT (GPT-5). Retrieved 12 October 2026 from https://chat.openai.com>

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [/] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: <Date and time of the interaction>
- Tool: <Tool name, version, access date and URL (UTM citation format)>
- Purpose: <One of: explain, hint, review, debug, generate-code, generate-text, tests-plan, other>
- Prompt: <The exact prompt you typed (paste it)>
- Output: <What the AI gave back, in 1 to 3 lines (attach the full text if you used it)>
- Verified by: <How you checked it: ran pytest, read the docs, compared with data, asked lecturer>
- My change: <What you accepted, rejected or rewrote, and why>
- Used in: <File and function, or report section, where it ended up (or 'not used')>

<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry 3 ... -->


## Entry 1 

- Date: 23 October 2026, 17:28 MYT
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 23 October 2026. https://chatgpt.com/
- Purpose: explain
- Prompt: "Based on the document instructions, break down the tasks step by step and tell me what I need to do."
- Output: AI explained the Lab 1 file structure, task sequence, Python environment setup, and testing requirements.
- Verified by: Reviewing the assignment instructions and following the project setup steps.
- My change: I carried out the setup steps myself.
- Used in: T1 project setup and repository preparation.

## Entry 2 

- Date: 23 October 2026, 21:27 MYT
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 23 October 2026. https://chatgpt.com/
- Purpose: explain, debug
- Prompt: "I successfully created .venv, but I am unsure how to activate it."
- Output: AI explained virtual environment activation and how to recognize an active environment from the (.venv) terminal prefix.
- Verified by: Checking that (.venv) appeared in the terminal.
- My change: I activated the virtual environment and proceeded with dependency installation.
- Used in: .venv and T1 environment setup.

## Entry 3 
- Date: 23 October 2026
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 23 October 2026. https://chatgpt.com/
- Purpose: explain, hint
- Prompt: "I am starting the README.md section of T1. After completing it, I will initialize Git, but I do not understand git status."
- Output: AI explained Git status, ignore rules, staging and committing, including git check-ignore .venv/ results/, git add ., git status, and git commit -m "Complete T1 repository setup".
- Verified by: Successfully creating the first Git commit.
- My change: I executed the Git commands and checked the repository status myself.
- Used in: README.md, .gitignore, and Git commit 9e7bf8a.

## Entry 4 
- Date: 24 October 2026, 00:52 MYT
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 24 October 2026. https://chatgpt.com/
- Purpose: explain, review
- Prompt: "Explain metadata.version(), None, and PackageNotFoundError so I can complete the lecturer-provided package_version() function."
- Output: AI explained package metadata lookup and missing-package exception handling. It reviewed the student's try/except structure, return values, and indentation.
- Verified by: Testing package_version() with installed and missing package names.
- My change: I implemented the function using the imported metadata module.
- Used in: src/env_check.py, package_version().

## Entry 5 
- Date: 24 October 2026, 00:59 MYT
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 24 October 2026. https://chatgpt.com/
- Purpose: debug
- Prompt: "My T2 package_version() test did not display a result for NumPy, while the missing-package test returned True."
- Output: AI helped diagnose the missing NumPy package metadata and explained the PackageNotFoundError message.
- Verified by: Inspecting the error No package metadata was found for numpy.
- My change: I checked the installed dependencies rather than changing the function unnecessarily.
- Used in: T2 environment debugging

## Entry 6
- Date: 24 October 2026, 01:13 MYT
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 24 October 2026. https://chatgpt.com/
- Purpose: debug, hint
- Prompt: "The .venv environment is correct, but NumPy is not installed. Reinstall the dependencies using the lecturer's requirements.txt."
- Output: AI guided the use of python -m pip install -r requirements.txt and python -c "from importlib import metadata; print(metadata.version('numpy'))".
- Verified by: Successfully checking the installed NumPy version.
- My change: I installed the dependencies and verified the package installation myself.
- Used in: .venv, requirements.txt, and T2 package verification.

## Entry 7 
- Date: 25 October 2026, 08:19 MYT
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 25 October 2026. https://chatgpt.com/
- Purpose: debug
- Prompt: "Ruff Import Errors"
- Reported errors: I001, F401, and unused imports.
- Output: AI explained import ordering, unused imports, and the distinction between Ruff and Pytest errors.
- Verified by: Running Ruff again; All checks passed!.
- My change: I corrected the import section myself.
- Used in: tests/test_lab01_own.py.