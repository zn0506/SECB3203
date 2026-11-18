import pytest

from bio_io import FastaFormatError, read_fasta
from batch import process_directory

def test_empty_fasta(tmp_path):
    empty_fasta = tmp_path / "empty.fasta"
    empty_fasta.write_text("")
    records = list(read_fasta(empty_fasta))
    assert records == []

def test_missing_fasta(tmp_path):
    missing_fasta = tmp_path / "missing.fasta"
    with pytest.raises(FileNotFoundError):
        list(read_fasta(missing_fasta))

def test_fasta_without_sequence(tmp_path):
    bad_fasta = tmp_path / "bad.fasta"
    bad_fasta.write_text(">geneA\n")
    with pytest.raises(FastaFormatError):
        list(read_fasta(bad_fasta))

def test_empty_directory(tmp_path):
    empty_dir = tmp_path / "empty_folder"
    empty_dir.mkdir()
    summary = process_directory(empty_dir, tmp_path / "output.csv")
    assert summary == {"processed": 0, "rejected": 0, "records": 0}