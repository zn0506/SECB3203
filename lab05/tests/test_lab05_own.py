import pytest

from sequence_utils import clean_sequence
from normalize import cpm, proportions

def test_clean_sequence():
    assert clean_sequence("aT 12gcN") == "ATGCN"

def test_proportions_input_unchanged():
    raw = [120, 80, 40]
    proportions(raw)
    assert raw == [120, 80, 40]

def test_proportions_total_zero():
    with pytest.raises(ValueError):
        proportions([0, 0, 0])

def test_cpm_explicit_library_size():
    counts = [10, 20]
    library_size = 100
    expected = [100000.0, 200000.0]
    assert cpm(counts, library_size) == expected