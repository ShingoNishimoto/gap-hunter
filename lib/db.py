"""
SQLite wrapper.

Owner: Person D
Goal: One file, three tables. Concepts, history, key-value state.

Hour 0:30–2:00 deliverable.
"""
import sqlite3
from pathlib import Path
from typing import List, Optional

from contracts import Concept, GraderOutput

DB_PATH = Path(__file__).parent.parent / "data" / "gaphunter.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS concepts (
    concept_id   TEXT PRIMARY KEY,
    name         TEXT NOT NULL,
    definition   TEXT,
    importance   INTEGER,
    source_pages TEXT     -- JSON-encoded list of [source, page] pairs
);

CREATE TABLE IF NOT EXISTS history (
    date        TEXT,
    question_id TEXT,
    concept_id  TEXT,
    verdict     TEXT,
    xp          INTEGER,
    PRIMARY KEY (date, question_id)
);

CREATE TABLE IF NOT EXISTS state (
    key   TEXT PRIMARY KEY,
    value TEXT
);
"""


def _conn() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c


def init_db() -> None:
    """Create tables if they don't exist. Idempotent."""
    # TODO Person D: with _conn() as c: c.executescript(SCHEMA)
    raise NotImplementedError("Person D: implement init_db")


def upsert_concepts(concepts: List[Concept]) -> None:
    """Insert or replace concepts. JSON-encode source_pages."""
    # TODO Person D
    raise NotImplementedError("Person D: implement upsert_concepts")


def list_concepts() -> List[Concept]:
    """All concepts."""
    # TODO Person D: SELECT * FROM concepts; reconstruct objects, json-decode source_pages.
    raise NotImplementedError("Person D: implement list_concepts")


def record_result(date_str: str, question_id: str, concept_id: str, result: GraderOutput) -> None:
    """Append a graded result to history."""
    # TODO Person D: INSERT OR REPLACE INTO history.
    raise NotImplementedError("Person D: implement record_result")


def get_state(key: str) -> Optional[str]:
    """Fetch a value from the kv state table. Returns None if missing."""
    # TODO Person D
    raise NotImplementedError("Person D: implement get_state")


def set_state(key: str, value: str) -> None:
    """Set a value in the kv state table."""
    # TODO Person D: INSERT OR REPLACE INTO state.
    raise NotImplementedError("Person D: implement set_state")
