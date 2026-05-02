"""
Cold-start bootstrap.

Streamlit Community Cloud's free tier may evict disk between deploys.
This script re-runs ingestion from `seed_materials/` if the Chroma DB is empty.

Owner: Person D. Wire `bootstrap_if_empty()` into app.py startup once it works.
"""
from pathlib import Path

SEED_DIR = Path(__file__).parent / "seed_materials"
DATA_DIR = Path(__file__).parent / "data"


def bootstrap_if_empty() -> None:
    """If Chroma is empty, ingest every PDF in seed_materials/."""
    # TODO Person D:
    # 1. Check Chroma collection size; return early if non-empty.
    # 2. Iterate PDFs in SEED_DIR.
    # 3. For each: chunks = lib.pdf.parse_pdf(path); lib.store.add_chunks(chunks).
    # 4. Once all chunks are in Chroma, run lib.concepts.extract_concepts(...) per source
    #    and lib.db.upsert_concepts(...).
    # 5. Print progress so it's visible in Streamlit logs.
    raise NotImplementedError("Person D: implement bootstrap_if_empty")


if __name__ == "__main__":
    bootstrap_if_empty()
