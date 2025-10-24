from fastapi import FastAPI, Body
from typing import List, Union
from src.models import Event
from src.database import DedupStore
from src.stats import stats
import threading

app = FastAPI(title="Event Aggregator")
store = DedupStore()
events = []
lock = threading.Lock()


@app.post("/publish")
async def publish_event(
    event_input: Union[Event, List[Event]] = Body(
        ...,
        title="Event Input",
        description="Kirim satu event atau list event di sini.",
        examples={
            "single": {
                "summary": "Contoh Single Event",
                "value": {
                    "topic": "user.signup",
                    "source": "webapp",
                    "payload": {"username": "rini"}
                },
            },
            "batch": {
                "summary": "Contoh Batch Event",
                "value": [
                    {
                        "topic": "user.signup",
                        "source": "webapp",
                        "payload": {"username": "rini"}
                    },
                    {
                        "topic": "user.login",
                        "source": "mobile",
                        "payload": {"username": "niwayan"}
                    }
                ],
            },
        },
    )
):
    
    event_list = [event_input] if isinstance(event_input, Event) else event_input

    for event in event_list:
        stats.received += 1
        with lock:
            if store.exists(event.topic, event.event_id):
                stats.duplicate_dropped += 1
                print(f"[DUPLICATE] {event.topic}-{event.event_id}")
                continue

            store.add(event.topic, event.event_id)
            events.append(event.dict())
            stats.unique_processed += 1
            stats.topics[event.topic] += 1

    return {
        "status": "ok",
        "received": len(event_list),
        "unique_processed": stats.unique_processed,
        "duplicates": stats.duplicate_dropped,
    }


@app.get("/events")
def get_events(topic: str = None):
    """
    Endpoint untuk menampilkan daftar event unik yang telah diproses.
    Bisa difilter berdasarkan topic (?topic=nama_topic)
    """
    if topic:
        filtered = [e for e in events if e["topic"] == topic]
        return {"count": len(filtered), "events": filtered}
    return {"count": len(events), "events": events}


@app.get("/stats")
def get_stats():
    """
    Endpoint untuk menampilkan statistik event yang diproses.
    """
    return stats.as_dict()


@app.post("/reset-stats")
def reset_stats():
    """
    Endpoint untuk mereset semua statistik event.
    """
    stats.reset()
    return {"status": "reset", "message": "Semua statistik telah direset."}
