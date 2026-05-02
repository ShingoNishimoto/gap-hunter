# Gap-Hunter

A web-based active-recall study tool for struggling ANU students.
Three short-answer questions a day. From your own course materials. With a streak.

> Built in 5 hours by 4 people. ANU AI Buildathon · May 2026.

## Quick start (local dev)

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
streamlit run app.py
```

Drop your course PDFs in `seed_materials/`, then run:

```bash
python bootstrap.py
```

…to populate the local Chroma + SQLite databases. Then `streamlit run app.py` again.

## Project layout

```
gap-hunter/
├── app.py                # Streamlit entrypoint              (Person C owns)
├── bootstrap.py          # Cold-start ingestion              (Person D owns)
├── contracts.py          # SHARED — locked in kickoff
├── lib/
│   ├── claude.py         # Anthropic client wrapper          (shared)
│   ├── pdf.py            # PyMuPDF chunking                  (Person A)
│   ├── store.py          # Chroma + retrieval                (Person A)
│   ├── concepts.py       # Concept extraction                (Person A)
│   ├── quiz.py           # Question generation               (Person B)
│   ├── grader.py         # Grading + grounded explanation    (Person B)
│   ├── ui.py             # Streamlit screens + components    (Person C)
│   ├── db.py             # SQLite wrapper                    (Person D)
│   └── state.py          # Streak/XP + daily concept picker  (Person D)
├── prompts/              # LLM prompt templates
├── seed_materials/       # PDFs the deployed app re-ingests on cold start
└── data/                 # Chroma + SQLite (gitignored)
```

## See also

- `BUILD_PLAN.md` (in the parent folder) — the full 5-hour plan
- `KICKOFF.md` — the first 30-minute meeting agenda
