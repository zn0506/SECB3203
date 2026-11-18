"""Week 6 extension - batch processing, logging, FASTQ and a command-line tool."""
import argparse
import logging
import sys
from collections.abc import Iterator
from pathlib import Path

from bio_io import FastaFormatError, read_fasta, write_csv

LOG = logging.getLogger("batch")


class FastqFormatError(ValueError):
    """Raised when a FASTQ file is malformed."""


def process_directory(in_dir, out_csv, log_path=None) -> dict[str, int]:
    """Read every *.fasta file in in_dir; one bad file never stops the batch.

    Writes one row per file (file, records, status, reason) to out_csv and
    returns {'processed': ..., 'rejected': ..., 'records': ...}.
    """
    handler = None
    if log_path is not None:
        Path(log_path).parent.mkdir(
            parents=True, exist_ok=True)
        handler = logging.FileHandler(
            log_path, mode="w", encoding="utf-8")
        handler.setFormatter(
            logging.Formatter("%(levelname)s %(message)s"))
        LOG.addHandler(handler)
        LOG.setLevel(logging.INFO)
    rows: list[dict] = []
    summary = {"processed": 0, "rejected": 0, "records": 0}
    
    fasta_files = sorted(Path(in_dir).glob("*.fasta"))

    try:
        for fasta_path in fasta_files:
            try:
                count = len(list(read_fasta(fasta_path)))
                if count == 0:
                    summary["rejected"] += 1
                    rows.append(
                        {
                            "file": fasta_path.name,
                            "records": 0,
                            "status": "rejected",
                            "reason": "empty file",
                        }
                    )
                    LOG.warning(f"{fasta_path.name}: empty file")
                else:
                    summary["processed"] += 1
                    summary["records"] += count
                    rows.append(
                        {
                            "file": fasta_path.name,
                            "records": count,
                            "status": "processed",
                            "reason": "",
                        }
                    )
                    LOG.info(f"{fasta_path.name}: processed {count} records")
            except (OSError, UnicodeDecodeError, FastaFormatError) as exc:
                summary["rejected"] += 1
                rows.append(
                    {
                        "file": fasta_path.name,
                        "records": 0,
                        "status": "rejected",
                        "reason": str(exc),
                    }
                )
                LOG.warning(f"{fasta_path.name}: {exc}")

        write_csv(rows, out_csv, ["file", "records", "status", "reason"])
    finally:
        if handler is not None:
            LOG.removeHandler(handler)
            handler.close()

    return summary

def read_fastq(path) -> Iterator[tuple[str, str, str]]:
    """Yield (read_id, sequence, quality) for each 4-line FASTQ record."""
    with Path(path).open(encoding="utf-8") as handle:
        while True:
            header = handle.readline()
            if not header:
                break
            if not header.strip():
                continue
            seq = handle.readline()
            plus = handle.readline()
            qual = handle.readline()
            if not (seq and plus and qual):
                raise FastqFormatError(f"Incomplete record in {path}")
            if not header.startswith("@"):
                raise FastqFormatError(f"Header does not start with @ in {path}")
            if not plus.startswith("+"):
                raise FastqFormatError(f"Missing + line in {path}")
            if len(seq.strip()) != len(qual.strip()):
                raise FastqFormatError(f"Sequence and quality lengths differ in {path}")
            header_text = header[1:].strip()
            if not header_text:
                raise FastqFormatError(f"Empty read ID in {path}")
            read_id = header_text.split()[0]
            yield read_id, seq.strip(), qual.strip()


def mean_phred(quality: str, offset: int = 33) -> float:
    """Mean Phred score of a quality string (Phred+33 by default)."""
    if not quality:
        raise ValueError("Quality string cannot be empty")
    return sum(ord(c) - offset for c in quality) / len(quality)


def main(argv: list[str] | None = None) -> int:
    """Command-line entry point. Exit code 0 = all good, 1 = some files rejected, 2 = bad input."""
    parser = argparse.ArgumentParser(
        description="Batch process FASTA files in a directory."
    )
    parser.add_argument("in_dir", help="Input directory containing FASTA files")
    parser.add_argument(
        "--out",
        default="results",
        help="Output directory for results (default: results)",
    )
    args = parser.parse_args(argv)

    in_dir = Path(args.in_dir)
    if not in_dir.is_dir():
        print(f"Error: {in_dir} is not a directory", file=sys.stderr)
        return 2

    out_dir = Path(args.out)
    out_csv = out_dir / "processing_log.csv"
    log_path = out_dir / "batch.log"

    summary = process_directory(in_dir, out_csv, log_path=log_path)
    print(f"processed={summary['processed']} rejected={summary['rejected']} records={summary['records']}")

    if summary["rejected"] > 0:
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
