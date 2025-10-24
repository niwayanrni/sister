import requests
import json

url_publish = "http://localhost:8080/publish"
url_stats = "http://localhost:8080/stats"


event = {
    "topic": "user.signup",
    "event_id": "evt-999",
    "timestamp": "2025-10-24T16:00:00Z",
    "source": "webapp",
    "payload": {"username": "rini"}
}

print("🚀 Mengirim event ke Docker container...")
res = requests.post(url_publish, json=event)
print("Response publish:", res.json())


res_stats = requests.get(url_stats)
print("📊 Stats:", json.dumps(res_stats.json(), indent=2))
