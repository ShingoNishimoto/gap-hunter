"""
Quiz generation.

Owner: Person B
Goal: Given a concept, generate one short-answer recall question via RAG.

Hour 0:30–3:00 deliverable.
"""
from pathlib import Path
from typing import List

from contracts import Concept, Question

PROMPT_PATH = Path(__file__).parent.parent / "prompts" / "generate_question.txt"


def generate_question(concept: Concept) -> Question:
    """
    Generate one short-answer recall question for a concept.

    Pipeline:
        1. Retrieve k=4 chunks via lib.store.retrieve(concept.name).
        2. Format chunks with `[<source> p.<page>]` prefix.
        3. Render prompts/generate_question.txt with concept + chunks.
        4. Call Claude (MODEL_SONNET) and parse the JSON response.
        5. Build a Question with key_points and source_chunk_ids.
    """
    # TODO Person B: implement.
    raise NotImplementedError("Person B: implement generate_question")


def generate_today(concepts: List[Concept], n: int = 3) -> List[Question]:
    """
    Generate today's `n` questions.

    Concept selection (which `n` to pick) is owned by lib.state.select_today_concepts.
    This function only generates a Question for each chosen concept.
    """
    return [generate_question(c) for c in concepts[:n]]
