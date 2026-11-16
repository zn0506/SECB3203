from panel import Variant
from panel import sort_variants, sorted_copy
from lookup import kmer_counts, safe_expression


def test_sorted_copy():
    genes = ["BRCA1", "TP53", "EGFR", "KRAS"]
    assert sorted_copy(genes) == ["BRCA1", "EGFR", "KRAS", "TP53"]
    assert genes == ["BRCA1", "TP53", "EGFR", "KRAS"]

def test_chromosome_order():
    variants = [
    Variant("M", 100, "A", "G"),
    Variant("10", 200, "C", "T"),
    Variant("X", 300, "G", "A"),
    Variant("2", 400, "T", "C"),
]
    sorted_variants = sort_variants(variants)
    expected_order = [
        Variant("2", 400, "T", "C"),
        Variant("10", 200, "C", "T"),
        Variant("X", 300, "G", "A"),
        Variant("M", 100, "A", "G"),
    ]
    assert sorted_variants == expected_order    

def test_kmer_boundary():
    assert kmer_counts("ACGT", 5) == {}
    assert kmer_counts("", 2) == {}

def test_safe_expression():
    expression = {"BRCA1": 2.5, "TP53": 0.0}
    assert safe_expression(expression, "TP53") == 0.0
    assert safe_expression(expression, "EGFR") is None
    assert "EGFR" not in expression