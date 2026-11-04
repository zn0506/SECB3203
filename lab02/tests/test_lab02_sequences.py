import pytest

from lab02_sequences import find_motif

def test_find_motif():
    sequence = "ATCGATCGATCG"
    motif = "CGA"
    assert find_motif(sequence, motif) == [2, 6]

def test_find_motif_overlapping():
    sequence = "AAAA"
    motif = "AA"
    assert find_motif(sequence, motif) == [0, 1, 2]

def test_find_motif_empty_motif():
    sequence = "ATCG"
    motif = ""
    with pytest.raises(ValueError):
        find_motif(sequence, motif)