"""
Gap-Hunter — Streamlit web app entrypoint.

Person D: deploy this immediately to Streamlit Community Cloud.
Person C: replace the placeholder content below with the four screens
(dashboard, quiz, feedback, end_of_day) wired via st.session_state.screen.

Run locally:
    pip install -r requirements.txt
    export ANTHROPIC_API_KEY=sk-ant-...
    streamlit run app.py
"""
import streamlit as st

st.set_page_config(
    page_title="Gap-Hunter",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- Session state initialization (Person C: extend as needed) ---
if "screen" not in st.session_state:
    st.session_state.screen = "dashboard"
if "current_q_index" not in st.session_state:
    st.session_state.current_q_index = 0
if "today_results" not in st.session_state:
    st.session_state.today_results = []
if "today_questions" not in st.session_state:
    st.session_state.today_questions = []


# --- Hour-0 deploy placeholder ---
# Person D's job: get THIS rendering on a public URL before any features ship.
# Person C will replace the body below with the four real screens.

st.title("Gap-Hunter 🔥")
st.subheader("Three questions a day. From your own course materials.")
st.write("")
st.info(
    "🚧 Building. Public URL is live. "
    "ANU Buildathon · 4 people · 5 hours."
)

st.divider()

st.caption(
    "**Person C:** replace this with screen routing based on "
    "`st.session_state.screen` — one of `dashboard | quiz | feedback | end_of_day`. "
    "Use the components in `lib/ui.py`."
)

# --- Person C: build the four screens here. ---
#
# from lib import ui, state, quiz, grader
#
# def render_dashboard():
#     ui.render_dashboard(state.get_streak_state())
#
# def render_quiz():
#     qs = st.session_state.today_questions
#     i = st.session_state.current_q_index
#     answer = ui.render_quiz_card(qs[i], i, len(qs))
#     if answer is not None:
#         result = grader.grade(qs[i], answer)
#         st.session_state.today_results.append(result)
#         st.session_state.screen = "feedback"
#         st.rerun()
#
# def render_feedback():
#     last_result = st.session_state.today_results[-1]
#     ui.render_feedback_card(last_result)
#     # Continue button advances current_q_index or routes to end_of_day
#
# def render_end_of_day():
#     new_state = state.update_streak_state(st.session_state.today_results)
#     xp_today = sum(r.xp for r in st.session_state.today_results)
#     ui.render_end_of_day(new_state, xp_today)
#
# screen_map = {
#     "dashboard": render_dashboard,
#     "quiz": render_quiz,
#     "feedback": render_feedback,
#     "end_of_day": render_end_of_day,
# }
# screen_map[st.session_state.screen]()
