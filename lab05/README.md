# SECB3203 Lab 5 - Functions and modules: sequence_utils.py and normalize.py

Student: Wong Zi Ning, A24CS0313

## Setup
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
    pip install -r requirements.txt

## Run
    python -m pytest                 # all tests
    ruff check src                   # style check

## What is in this repository
- `src/sequence_utils.py` : clean_sequence, is_valid_dna, gc_content, reverse_complement, find_motif
- `src/normalize.py` : proportions, cpm (never change the caller's data)
- `tests/` : visible tests and my own tests (test_lab05_own.py)
- `AI_USE_LOG.md` : my AI prompt log (or nil return)

## Design decisions
### Question 1: Why raise ValueError?
When the total is zero, calculating count/total would cause division by zero. Returning a list of zeros instead could also be misleading because it might look like valid normalized data.

### Question 2: How do you prevent side effects?
```
return [count / total for count in counts]
```
This list comprehension creates a new list rather than modifying the existing counts list.