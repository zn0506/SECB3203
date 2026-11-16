"""Lab 4 - dictionaries and sets for biological lookup."""

import itertools
from collections import Counter

_BASES = "TCAG"
_AMINO = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODON_TABLE: dict[str, str] = {
    "".join(codon): aa for codon, aa in zip(itertools.product(_BASES, repeat=3), _AMINO)
}


def count_bases(seq: str) -> dict[str, int]:
    """Count each character in seq (upper-cased), sorted by key."""
    return dict(sorted(Counter(seq.upper()).items()))


def kmer_counts(seq: str, k: int) -> dict[str, int]:
    """Count overlapping k-mers, sorted by key. ValueError if k < 1."""
    if k < 1:
        raise ValueError("k must be at least 1")
    seq = seq.upper()
    kmers = (seq[i : i + k] for i in range(len(seq) - k + 1))
    return dict(sorted(Counter(kmers).items()))


def shared_genes(panel: set[str], detected: set[str]) -> set[str]:
    """Genes that are both on the panel and detected."""
    return panel & detected


def safe_expression(expression: dict[str, float], gene: str) -> float | None:
    """Return the expression value, or None when the gene is missing."""
    return expression.get(gene)


def translate(dna: str) -> str:
    """Translate DNA to a protein string ('*' marks a stop codon).

    Raises:
        ValueError: if the length is not a multiple of 3 or a codon is invalid.
    """
    dna = dna.upper()
    if len(dna) % 3 != 0:
        raise ValueError("DNA length must be a multiple of 3")
    protein = []
    for i in range(0, len(dna), 3):
        codon = dna[i : i + 3]
        if codon not in CODON_TABLE:
            raise ValueError(f"Invalid codon: {codon!r} at position {i}")
        protein.append(CODON_TABLE[codon])
    return "".join(protein)
