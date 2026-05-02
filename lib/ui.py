"""
Streamlit screen components.

Owner: Person C
Goal: Render the four screens. Make it feel like a quiz game, not a data dashboard.

Hour 0:30–5:00 deliverable.
"""
from typing import Optional

import streamlit as st

from contracts import GraderOutput, Question, StreakState


# --- Visual helpers ---------------------------------------------------------

def streak_emoji_strip(streak: int, max_show: int = 7) -> str:
    """e.g. streak=4 -> '🔥🔥🔥🔥░░░'"""
    fire = "🔥" * min(streak, max_show)
    empty = "░" * max(0, max_show - streak)
    return fire + empty


def progress_bar_text(done: int, total: int, width: int = 20) -> str:
    """ASCII progress bar for inline display."""
    filled = int(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled) + f" {done}/{total}"


def card_css() -> None:
    """Inject custom CSS for game-feeling cards. Call once near the top of app.py."""
    # TODO Person C: rounded corners, drop shadow, larger button height.
    st.markdown(
        """
        <style>
        .stButton button { height: 3rem; font-size: 1.1rem; border-radius: 0.75rem; }
        .gh-card { padding: 1.5rem; border-radius: 1rem; background: #FAFAFA; box-shadow: 0 2px 6px rgba(0,0,0,.05); }
        .gh-streak { font-size: 3rem; font-weight: 700; }
        </style>
        """,
        unsafe_allow_html=True,
    )


# --- Screens -----------------------------------------------------------------

def render_dashboard(state: StreakState) -> None:
    """The home screen: streak, XP, history strip, big Start button."""
    # TODO Person C: lay out streak, XP, last-7-days strip, Start button that
    # routes to st.session_state.screen = "quiz".
    raise NotImplementedError("Person C: implement render_dashboard")


def render_quiz_card(question: Question, q_index: int, total: int) -> Optional[str]:
    """
    Render one question card with text input + submit button.

    Returns:
        The student's typed answer when they submit, otherwise None.
        Caller is responsible for advancing to the feedback screen.
    """
    # TODO Person C:
    # - Show progress dots (● ○ ○) for q_index / total.
    # - st.text_area for the answer.
    # - "Submit" button. Return value when clicked.
    raise NotImplementedError("Person C: implement render_quiz_card")


def render_feedback_card(result: GraderOutput) -> None:
    """
    Show verdict, grounded explanation_md, encouragement, Continue button.

    On 'correct', call st.balloons() for the win moment.
    On 'wrong', render result.explanation_md (which contains a quoted page citation).
    """
    # TODO Person C:
    # - Big ✅ or ❌ at the top.
    # - st.markdown(result.explanation_md, unsafe_allow_html=False)
    # - st.caption(result.encouragement)
    # - "Continue" button advances current_q_index or routes to end_of_day.
    raise NotImplementedError("Person C: implement render_feedback_card")


def render_end_of_day(state: StreakState, xp_gained: int) -> None:
    """Streak +1 celebration. 'Come back tomorrow.' Disabled Start button."""
    # TODO Person C:
    # - Big "Streak: N 🔥".
    # - "+{xp_gained} XP today" line.
    # - "Come back tomorrow" message.
    # - Disable the Start button (or route back to dashboard with today_done=True).
    raise NotImplementedError("Person C: implement render_end_of_day")
