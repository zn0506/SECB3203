import pytest

from models import BiologicalSample, DNASequence, SampleCollection


def test_sample_results_copy():
    dna = DNASequence("D01", "ATGC")
    sample = BiologicalSample("S01", "case", dna)

    sample.add_result("qc", "pass")

    copied_results = sample.results
    copied_results["qc"] = "fail"

    assert sample.results == {"qc": "pass"}


def test_empty_collection():
    collection = SampleCollection()

    assert len(collection) == 0
    assert collection.summary() == {}
    assert collection.by_group("case") == []
    assert list(collection) == []


def test_duplicate_sample_id():
    collection = SampleCollection()

    dna1 = DNASequence("D01", "ATGC")
    dna2 = DNASequence("D02", "GGCC")

    sample1 = BiologicalSample("S01", "case", dna1)
    sample2 = BiologicalSample("S01", "control", dna2)

    collection.add(sample1)

    with pytest.raises(ValueError):
        collection.add(sample2)

    assert len(collection) == 1
