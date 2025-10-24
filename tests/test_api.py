from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_publish_event():
    event = {
        "topic": "sensor",
        "timestamp": "2025-10-24T10:00:00",
        "source": "test_source",
        "payload": {"value": 42}
    }
    response = client.post("/publish", json=event)
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
