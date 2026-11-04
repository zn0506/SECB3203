"""Lab 2 - biological sequences as strings (becomes sequence_utils.py in Week 5)."""

DNA_BASES = frozenset("ACGT")


def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    clean = ""

    for char in raw:
        if char.isalpha():
            clean += char.upper()

    return clean

def is_valid_dna(seq: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (and N when allowed)."""
    seq = clean_sequence(seq)
    if not seq:
        return False

    allow_n = bool(allow_n)
    
    if allow_n:
        return all(char in DNA_BASES or char == "N" for char in seq)
    
    return all(char in DNA_BASES for char in seq)


def gc_content(seq: str) -> float:
    """Return GC percentage (0-100); ValueError if empty or not A/C/G/T."""
    seq = seq.upper()

    if not is_valid_dna(seq) or any(char not in DNA_BASES for char in seq):
        raise ValueError("Invalid DNA sequence")

    gc_count = seq.count("G") + seq.count("C")
    return (gc_count / len(seq)) * 100


def transcribe(dna: str) -> str:
    """Return the RNA copy of a DNA sequence (T becomes U)."""
    dna = clean_sequence(dna)

    if not is_valid_dna(dna):
        raise ValueError("Invalid DNA sequence")

    return dna.replace("T", "U")


def find_motif(seq: str, motif: str) -> list[int]:
    """Return every 0-based start of motif in seq (overlaps allowed)."""
    positions = []
    seq = clean_sequence(seq)
    motif = clean_sequence(motif)

    if not motif:
        raise ValueError("Motif cannot be empty")

    for i in range(len(seq) - len(motif) + 1):
        if seq[i:i + len(motif)] == motif:
            positions.append(i)

    return positions

