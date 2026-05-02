"""
Vector store wrapper.

Owner: Person A
Goal: Persist chunks to Chroma; support semantic retrieval and id lookup.

Hour 0:30–2:00 deliverable.
"""
from pathlib import Path
from typing import List

from contracts import Chunk

CHROMA_DIR = Path(__file__).parent.parent / "data" / "chroma"
COLLECTION_NAME = "gap_hunter_chunks"


def _client():
    """Lazy chromadb client."""
    import chromadb

    CHROMA_DIR.mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=str(CHROMA_DIR))


def collection_size() -> int:
    """How many chunks are currently in the store. Used by bootstrap.py."""
    # TODO Person A: client.get_or_create_collection(...).count()
    raise NotImplementedError("Person A: implement collection_size")


def add_chunks(chunks: List[Chunk]) -> None:
    """Embed and persist chunks to Chroma. Idempotent on chunk_id."""
    # TODO Person A:
    # collection = client.get_or_create_collection(COLLECTION_NAME)
    # collection.upsert(
    #     ids=[c.chunk_id for c in chunks],
    #     documents=[c.text for c in chunks],
    #     metadatas=[{"source": c.source, "page": c.page} for c in chunks],
    # )
    raise NotImplementedError("Person A: implement add_chunks")


def retrieve(query: str, k: int = 5) -> List[Chunk]:
    """Return top-k chunks most relevant to the query."""
    # TODO Person A: collection.query(query_texts=[query], n_results=k)
    # Reconstruct Chunk objects from results.
    raise NotImplementedError("Person A: implement retrieve")


def get_chunks_by_ids(chunk_ids: List[str]) -> List[Chunk]:
    """
    Look up specific chunks by id.

    Used by the grader to reconstruct source citations from a Question's
    `source_chunk_ids` field.
    """
    # TODO Person A: collection.get(ids=chunk_ids)
    raise NotImplementedError("Person A: implement get_chunks_by_ids")
