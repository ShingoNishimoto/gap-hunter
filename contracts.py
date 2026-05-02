"""
Gap-Hunter shared data contracts.

LOCK THESE IN THE FIRST 30 MINUTES.
Everyone imports from here. No parallel definitions anywhere else.

If you want to change a field, announce in the team chat first
and update this file in a single commit so everyone can pull together.
"""
from dataclasses import dataclass
from datetime import date
from typing import List, Literal, Optional, Tuple


@dataclass
class Chunk:
    """A passage from a source document, with provenance metadata."""

    chunk_id: str          # short stable hash
    text: str
    source: str            # filename, e.g. "Lecture 4.pdf"
    page: int              # 1-indexed


@dataclass
class Concept:
    """An atomic concept extracted from one or more sources."""

    concept_id: str
    name: str              # 1-5 word noun phrase
    definition: str        # one sentence, plain language
    importance: int        # 1-5
    source_pages: List[Tuple[str, int]]   # [("Lecture 4.pdf", 12), ...]


@dataclass
class Question:
    """A short-answer recall question for one concept."""

    question_id: str
    concept_id: str
    question: str
    expected_answer: str
    key_points: List[str]               # used by grader
    source_chunk_ids: List[str]         # for grounding citations


@dataclass
class GraderOutput:
    """Result of grading a student answer."""

    question_id: str
    verdict: Literal["correct", "partial", "wrong"]
    xp: int                # 10 / 5 / 0
    explanation_md: str    # markdown block rendered into the feedback card
    encouragement: str     # short motivation line


@dataclass
class StreakState:
    """The student's current motivation state."""

    streak_days: int
    total_xp: int
    last_completed: Optional[date]
    today_done: bool
