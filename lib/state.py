"""
Streak / XP / daily concept selection.

Owner: Person D
Goal: Streak math, daily concept picker, today-done flag.

Hour 0:45–2:00 deliverable.
"""
from datetime import date, timedelta
from typing import List

from contracts import Concept, GraderOutput, StreakState


def get_streak_state() -> StreakState:
    """Read current streak state from DB. Returns zeroed state if uninitialized."""
    # TODO Person D:
    # - Read 'streak_days', 'total_xp', 'last_completed' from kv state table.
    # - Compute today_done = (last_completed == today).
    # - If last_completed is None or older than yesterday, streak should be considered "broken"
    #   visually (Person C handles the 💔 display); keep streak_days as stored until next update.
    raise NotImplementedError("Person D: implement get_streak_state")


def update_streak_state(today_results: List[GraderOutput]) -> StreakState:
    """
    Called after the student finishes today's quiz.

    Rules:
        - If last_completed == yesterday: streak_days += 1
        - If last_completed is None or < yesterday: streak_days = 1 (reset)
        - If last_completed == today: no change (idempotent, shouldn't happen)
        - total_xp += sum(r.xp for r in today_results)
        - last_completed = today
    """
    # TODO Person D
    raise NotImplementedError("Person D: implement update_streak_state")


def select_today_concepts(n: int = 3) -> List[Concept]:
    """
    Pick today's `n` concepts.

    Day 1 (no history): top n by importance.
    Day 2+: bias toward yesterday's misses, then low-accuracy concepts,
    then new concepts (importance-weighted).

    Keep this simple — for the demo, `top n by importance` is enough.
    """
    # TODO Person D: read concepts from db, simple selection.
    raise NotImplementedError("Person D: implement select_today_concepts")
