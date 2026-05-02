# Seed materials

Drop the chosen ANU course's PDFs in this folder before pushing to GitHub.
Streamlit Community Cloud's free tier may evict the disk; `bootstrap.py`
re-ingests every PDF in here on cold start so the deployed app always has
a knowledge base.

Recommended:
- One textbook PDF (or a few key chapters)
- Lecture slide PDFs

Keep total size under ~50 MB to stay within free-tier disk limits.
