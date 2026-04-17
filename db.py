import os
import psycopg2

DB_HOST = os.environ.get("DB_HOST", "postgresql")
DB_NAME = os.environ.get("DB_NAME", "demo")
DB_USER = os.environ.get("DB_USER", "demo")
DB_PASS = os.environ.get("DB_PASS", "demo")


def get_conn():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )


def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            text VARCHAR(255)
        )
    """)

    conn.commit()
    cur.close()
    conn.close()


def add_message(text):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("INSERT INTO messages (text) VALUES (%s)", (text,))

    conn.commit()
    cur.close()
    conn.close()


def get_messages():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, text FROM messages ORDER BY id DESC")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [{"id": r[0], "text": r[1]} for r in rows]
