import sqlite3

DB_NAME = "sensor.db"

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TEXT NOT NULL,
    temperature REAL NOT NULL,
    humidity REAL NOT NULL,
    co2 REAL NOT NULL
)
"""

ALLOWED_COLUMNS = ["temperature", "humidity", "co2"]


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute(CREATE_TABLE)
    return conn


def add_reading(time, temperature, humidity, co2):
    conn = get_connection()
    conn.execute(
        "INSERT INTO readings (time, temperature, humidity, co2) VALUES (?, ?, ?, ?)",
        (time, temperature, humidity, co2),
    )
    conn.commit()
    conn.close()


def get_column(column):
    if column not in ALLOWED_COLUMNS:
        raise ValueError(f"Unknown column: {column}")
    conn = get_connection()
    rows = conn.execute(f"SELECT {column} FROM readings ORDER BY id").fetchall()
    conn.close()
    return [row[0] for row in rows]


def count_readings():
    conn = get_connection()
    count = conn.execute("SELECT COUNT(*) FROM readings").fetchone()[0]
    conn.close()
    return count


def max_temperature():
    conn = get_connection()
    result = conn.execute("SELECT MAX(temperature) FROM readings").fetchone()[0]
    conn.close()
    return result


def latest_readings(limit=5):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT time, temperature, humidity, co2 FROM readings ORDER BY id DESC LIMIT ?",
        (limit,),
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]