# SECB3203 Lab 1 - Python fundamentals and a reproducible project

Student: WONG ZI NING, A24CS0313

## Setup
Windows PowerShell was used for this project.
### 1. Create the virtual environment
python -m venv .venv
### 2. Activate the virtual environment
.\.venv\Scripts\Activate.ps1
### 3. Install project dependencies
python -m pip install -r requirements.txt
### 4. Record the frozen environment packages
python -m pip freeze > requirements-frozen.txt

### Windows CMD
.venv\Scripts\activate.bat

### Linux/macOS
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip freeze > requirements-frozen.txt

## Run
### Run automated tests
python -m pytest

### Run the code style checker
ruff check src

### Display the environment check report
python src/env_check.py

### Save the environment report to the results folder
python src/env_check.py > results/environment_report.txt

## What is in this repository
src/ — Contains Python source code files (basics.py for DNA base counts, GC percentage, and formatting; env_check.py for checking Python and package versions).

tests/ — Contains automated unit tests.

data/ — Stores read-only input data (qc_records.csv).

results/ — Stores generated output reports and environment logs.

README.md — Provides project setup, usage, and structure documentation.

requirements.txt — Lists required Python package dependencies.

requirements-frozen.txt — Records the exact installed package versions.

pytest.ini — Contains configuration settings for pytest.

.gitignore — Specifies files and folders that Git should ignore.

AI_USE_LOG.md — Records AI usage for the assessment

## What is not committed, and why
The .venv/ and results/ folders are excluded by .gitignore. Committing the virtual environment would tie the repository to machine-specific paths and binaries, whereas committing generated output files is unnecessary since they can be cleanly recreated by running the code.