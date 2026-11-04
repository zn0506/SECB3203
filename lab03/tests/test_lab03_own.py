from src.qc import classify_read, trim_low_quality

def test_length_boundary():
    assert classify_read(499, 0, 50.0) == "reject"
    assert classify_read(500, 0, 40.0) == "pass"

def test_n_count_boundary():
    assert classify_read(600, 10, 50.0) == "pass"
    assert classify_read(600, 11, 50.0) == "review"

def test_trim_low_quality():
    assert trim_low_quality([30, 32, 35, 12, 10]) == 3
    assert trim_low_quality([30, 32, 35]) == 3
    assert trim_low_quality([10, 12, 15]) == 0