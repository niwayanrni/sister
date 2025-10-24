import os
from src.database import DedupStore, DB_PATH

def test_persistence():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    store = DedupStore()
    store.add("persist", "999")

    # Simulasi "restart" (buat koneksi baru)
    new_store = DedupStore()
    assert new_store.exists("persist", "999")
