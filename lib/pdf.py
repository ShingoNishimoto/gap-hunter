"""
PDF parsing.

Owner: Person A
Goal: Turn a PDF file into a list of Chunks with (source, page) metadata.

Hour 0:30–2:00 deliverable.
"""
import hashlib
from pathlib import Path
from typing import List

from contracts import Chunk


def chunk_id_for(text: str, source: str, page: int) -> str:
    """Deterministic short id so re-ingest is idempotent."""
    h = hashlib.sha1(f"{source}|{page}|{text}".encode()).hexdigest()
    return h[:12]


def parse_pdf(path: Path, chunk_size_chars: int = 800) -> List[Chunk]:
    """
    Parse a PDF into Chunks.

    Each Chunk must carry the source filename and 1-indexed page number.
    Use `page.get_text("blocks")` and join into ~`chunk_size_chars`-character chunks,
    keeping each chunk inside a single page so page metadata stays accurate.

    Args:
        path: filesystem path to the PDF.
        chunk_size_chars: target chunk size; do not split mid-page.

    Returns:
        List of Chunks with stable chunk_id (use `chunk_id_for(...)`).
    """
    # TODO Person A: implement with PyMuPDF (`fitz`).
    # import fitz
    # doc = fitz.open(path)
    # for page_idx, page in enumerate(doc, start=1):
    #     blocks = page.get_text("blocks")
    #     # join blocks until chunk_size_chars; emit Chunk; continue on same page
    raise NotImplementedError("Person A: implement parse_pdf")
