import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "users.db"


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                username TEXT,
                phone TEXT,
                kit TEXT,
                delivery INTEGER,
                total INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()


def save_order(user_id, username, phone, kit, delivery, total):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO orders (user_id, username, phone, kit, delivery, total) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (user_id, username, phone, kit, int(delivery), total)
        )
        conn.commit()


init_db()