import requests
import uuid
import random
import time

URL = "http://localhost:8080/publish"

TOTAL_EVENTS = 5000
DUPLICATE_RATIO = 0.2

events = [
    {
        "topic": random.choice(["user.signup", "user.login", "order.create"]),
        "event_id": str(uuid.uuid4()),
        "timestamp": "2025-10-24T15:00:00Z",
        "source": random.choice(["webapp", "mobile"]),
        "payload": {"user": f"user_{i}"}
    }
    for i in range(int(TOTAL_EVENTS * (1 - DUPLICATE_RATIO)))
]

duplicates = random.choices(events, k=int(TOTAL_EVENTS * DUPLICATE_RATIO))
all_events = events + duplicates
random.shuffle(all_events)

print(f"🚀 Mengirim {len(all_events)} event (dengan {int(TOTAL_EVENTS * DUPLICATE_RATIO)} duplikat)...")

start = time.time()
response = requests.post(URL, json=all_events)
end = time.time()

print("Status:", response.status_code)
print("Response:", response.json())
print(f"⏱️ Waktu eksekusi: {round(end - start, 2)} detik")
