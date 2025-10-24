import sqlite3
import os
import logging

logging.basicConfig(level=logging.INFO)

# Tentukan folder penyimpanan database
DATA_DIR = "/app/data"  # aman untuk container
os.makedirs(DATA_DIR, exist_ok=True)  # pastikan folder ada

DB_PATH = os.path.join(DATA_DIR, "dedup_store.db")

class DedupStore:
    def __init__(self):
        try:
            self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
            self.create_table()
            logging.info(f"Connected to SQLite database at {DB_PATH}")
        except Exception as e:
            logging.error(f"Failed to connect to database: {e}")
            raise

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS processed_events (
            topic TEXT,
            event_id TEXT,
            PRIMARY KEY (topic, event_id)
        )
        """)
        self.conn.commit()
        logging.info("Ensured table 'processed_events' exists")

    def exists(self, topic: str, event_id: str) -> bool:
        cursor = self.conn.execute(
            "SELECT 1 FROM processed_events WHERE topic=? AND event_id=?",
            (topic, event_id),
        )
        return cursor.fetchone() is not None

    def add(self, topic: str, event_id: str):
        self.conn.execute(
            "INSERT OR IGNORE INTO processed_events (topic, event_id) VALUES (?, ?)",
            (topic, event_id),
        )
        self.conn.commit()
        logging.info(f"Stored event: topic={topic}, event_id={event_id}")

    def close(self):
        self.conn.close()
        logging.info("Database connection closed")
