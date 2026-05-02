"""
Concept extraction.

Owner: Person A
Goal: Scan chunks per source and extract atomic concepts via Claude.

Hour 2:00–3:00 deliverable.
"""
import hashlib
import json
from pathlib import Path
from typing import List

from contracts import Chunk, Concept

PROMPT_PATH = Path(__file__).parent.parent / "prompts" / "extract_concepts.txt"


def _concept_id_for(name: str) -> str:
    return hashlib.sha1(name.lower().strip().encode()).hexdigest()[:12]


def extract_concepts(chunks: List[Chunk], source_label: str) -> List[Concept]:
    """
    Extract atomic concepts from a batch of chunks (typically one source at a time).

    Uses prompts/extract_concepts.txt with Claude (use MODEL_HAIKU for cost).
    Returns concepts with importance 1-5 and source_pages metadata.

    Caller is responsible for cross-source dedup via dedup_concepts(...).
    """
    # TODO Person A:
    # 1. Load prompt template.
    # 2. Format chunks as `[page N]\n<text>` joined by blank lines.
    # 3. Replace <SOURCE> and <CHUNKS> placeholders.
    # 4. lib.claude.call_claude(prompt, model=MODEL_HAIKU, max_tokens=4000).
    # 5. Parse JSON array; build Concept objects with stable concept_ids.
    raise NotImplementedError("Person A: implement extract_concepts")


def dedup_concepts(concepts: List[Concept]) -> List[Concept]:
    """
    Merge concepts with identical lowercase names.

    Concatenates source_pages, keeps the highest importance,
    keeps the first definition (or longest — Person A's call).
    """
    # TODO Person A: simple dict[name.lower()] -> Concept merge.
    raise NotImplementedError("Person A: implement dedup_concepts")
