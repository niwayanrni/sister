import time
from collections import defaultdict

class Stats:
    def __init__(self):
        self.start_time = time.monotonic()
        self.received = 0
        self.unique_processed = 0
        self.duplicate_dropped = 0
        self.topics = defaultdict(int)

    def as_dict(self):
        uptime = round(time.monotonic() - self.start_time, 2)
        return {
            "received": self.received,
            "unique_processed": self.unique_processed,
            "duplicate_dropped": self.duplicate_dropped,
            "topics": dict(self.topics),
            "uptime_seconds": uptime,
        }

    def reset(self):
        self.start_time = time.monotonic()
        self.received = 0
        self.unique_processed = 0
        self.duplicate_dropped = 0
        self.topics = defaultdict(int)

stats = Stats()
