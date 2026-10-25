"""Lab 1 - Python fundamentals for biological calculations."""


def gc_percent(a: int, c: int, g: int, t: int) -> float:
    """Return the GC percentage from the four base counts.

    Raises:
        ValueError: if any count is negative or the total is zero.
    """
    if any(count < 0 for count in (a, c, g, t)):
        raise ValueError("Counts must be non-negative integers.")
    total = a + c + g + t
    if total == 0:
        raise ValueError("Total count must be greater than zero.")
    gc_count = g + c
    return (gc_count / total) * 100


def format_report(sample: str, length: int, gc: float) -> str:
    """Return a one-line report with units, e.g. 'S1: 60 bases, GC 46.7%'."""
    return f"{sample}: {length} bases, GC {gc:.1f}%"


def parse_counts(text: str) -> tuple[int, int, int, int]:
    """Parse 'A C G T' counts separated by spaces or commas.

    Raises:
        ValueError: if there are not exactly four non-negative integers.
    """
    # Replace commas with spaces and split the string into parts
    parts = text.replace(',', ' ').split()
    if (len(parts) != 4):
        raise ValueError("Input must contain exactly four counts.")
    try:
        counts = tuple(int(part) for part in parts)
    except ValueError:
        raise ValueError("All counts must be integers.")
    if any(count < 0 for count in counts):
        raise ValueError("Counts must be non-negative integers.")
    return counts
