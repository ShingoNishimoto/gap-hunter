"""
Grading + grounded explanation.

Owner: Person B
Goal: Judge a student answer; produce a citation-backed explanation for misses.

Plain Python. NO LangGraph. Single LLM call per grade.

Hour 2:00–4:00 deliverable.
"""
import random
from pathlib import Path

from contracts import GraderOutput, Question

PROMPT_PATH = Path(__file__).parent.parent / "prompts" / "explain_miss.txt"

# Encouragement copy templates — picked here so the grader returns
# a fully-rendered GraderOutput. Person C may move these to lib/ui.py
# if they prefer; if so, expose a function and import it.
ENCOURAGEMENT_CORRECT = [
    "🔥 Nailed it.",
    "Boom. On the board.",
    "Good recall.",
    "You knew that one.",
    "Exactly right.",
]
ENCOURAGEMENT_PARTIAL = [
    "Close. Keep going.",
    "Half there.",
    "On the right track.",
    "Almost — read the explanation.",
]
ENCOURAGEMENT_WRONG = [
    "That's okay — read the explanation.",
    "Tomorrow you'll get this one.",
    "Mistakes are how recall sticks.",
    "Don't sweat it. Now you know.",
]


def grade(question: Question, student_answer: str) -> GraderOutput:
    """
    Grade a student answer and return a feedback markdown block.

    Pipeline:
        1. Pull source chunks via lib.store.get_chunks_by_ids(question.source_chunk_ids).
        2. Render prompts/explain_miss.txt with question, expected_answer, key_points,
           student_answer, and chunks (formatted with `[<source> p.<page>]` prefix).
        3. Call Claude (MODEL_SONNET) and parse JSON: {verdict, explanation_md, covered_key_points}.
        4. Map verdict -> XP: correct=10, partial=5, wrong=0.
        5. Pick an encouragement template based on verdict.
        6. Return GraderOutput.

    On JSON parse failure, fall back to verdict="wrong", xp=0, with a
    generic apology in explanation_md so the demo never crashes mid-quiz.
    """
    # TODO Person B: implement.
    raise NotImplementedError("Person B: implement grade")


def _encouragement_for(verdict: str) -> str:
    bag = {
        "correct": ENCOURAGEMENT_CORRECT,
        "partial": ENCOURAGEMENT_PARTIAL,
        "wrong": ENCOURAGEMENT_WRONG,
    }[verdict]
    return random.choice(bag)
