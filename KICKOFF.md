# Kickoff (first 30 minutes — do not skip)

## Agenda

**0:00–0:05 — Roll call**
Confirm who is A / B / C / D. Each person reads their role brief in `BUILD_PLAN.md`.

**0:05–0:10 — Pick the course**
Decide the ONE course whose materials we'll use. Drop the PDFs in `seed_materials/`.

**0:10–0:15 — Walk through `contracts.py` together**
Open it, read every field aloud. If anyone wants to rename anything, do it now.
After this meeting, contracts are frozen.

**0:15–0:20 — D announces the deploy**
- D pushes the current repo to GitHub.
- D goes to https://share.streamlit.io, creates a new app pointing at this repo's `app.py`.
- D adds `ANTHROPIC_API_KEY` in the app's Secrets.
- Goal: public URL serving "Hello, Gap-Hunter" before this kickoff ends.

**0:20–0:25 — Each person states their hour-0:30-to-2:00 plan in 30 seconds**
- A: "I'll have `parse_pdf` and `retrieve` working by 2:00."
- B: "I'll have `generate_question` working on mock chunks by 2:00."
- C: "I'll have all four screens with mock data wired by 2:00."
- D: "I'll have `init_db`, schema, streak math by 2:00."

**0:25–0:30 — Communications**
- Where does the team chat? (one chat, not three)
- Who owns the merge conflict if two people change `app.py`? **C owns app.py.**
- Sync standups at 1:00, 2:00, 3:00 — 5 minutes max each.

## After kickoff

Everyone: open your stub file. Write the docstring you want to see when you read it tomorrow. Write one assertion against a mock input. Then start the real work.

## Pin this somewhere visible

> **The 3:00 rule.** If end-to-end isn't working at hour 3, **everyone stops adding features and converges on making one happy path run.** Working ugly > beautiful broken.

## What we're explicitly NOT building

(Re-read this list every time someone proposes adding something.)

- A chatbot UI
- An Obsidian plugin (use the deployed web app instead)
- Multi-user accounts / login
- LangGraph
- Push notifications (the dashboard is the reminder)
- SM-2 spaced repetition
- Hearts / lives / leagues / leaderboards
- A separate React frontend
- Anything not on the demo path
