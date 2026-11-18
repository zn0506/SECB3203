# SECB3203 Lab 6 - Files and exceptions: bio_io.py and batch.py

Student: Wong Zi Ning, A24CS0313

## Setup
    python -m venv .venv
    source .venv/bin/activate        # Windows: .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt

## Run
    python -m pytest                 # all tests
    ruff check src                   # style check
    python src/batch.py data/river --out results/cli      # the command-line tool

## What is in this repository
- `src/bio_io.py` : FastaFormatError, read_fasta, read_csv_records, write_csv
- `src/batch.py` : process_directory, read_fastq, mean_phred, main (command-line tool)
- `tests/` : visible tests and my own tests (test_lab06_own.py)
- `data/` : raw synthetic data, read-only (amplicons.fasta, river/, qc_records.csv, reads.fastq)
- `results/` : files the tool writes (not committed)
- `AI_USE_LOG.md` : my AI prompt log (or nil return)

## Exit codes of batch.py
Exit code 0: All FASTA files were processed successfully, and none of them were rejected.

Exit code 1: The program completed processing, but some FASTA files were rejected due to errors or invalid formats.

Exit code 2: The program could not start processing because the input directory was missing or invalid.