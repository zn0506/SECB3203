import pytest

from basics import gc_percent, parse_counts


def test_gc_boundary_zero():
     result = gc_percent(8, 0, 0, 12)
     assert result == pytest.approx(0.0, abs=1e-3)

def test_gc_boundary_one_hundred():
    result = gc_percent(0, 10, 10, 0)
    assert result == pytest.approx(100.0, abs=1e-3)

def test_gc_zero_total_raises():
    # When all counts are 0, the total length is 0, should raise a ValueError
    with pytest.raises(ValueError):
        gc_percent(0, 0, 0, 0)

def test_parse_counts_with_non_integer_values():
    # Verify parse_counts rejects invalid input with non-integer values
    with pytest.raises(ValueError):
        parse_counts("10 20 abc 40")  # Contains a non-integer value