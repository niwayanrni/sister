from src.database import DedupStore

def test_dedup_store():
    store = DedupStore()
    topic, event_id = "test_topic", "123"

    assert not store.exists(topic, event_id)
    store.add(topic, event_id)
    assert store.exists(topic, event_id)
