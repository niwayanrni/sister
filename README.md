# Aggregator FastAPI


Run locally:


1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. export DEDUP_DB=./data/dedup.db
5. uvicorn src.main:app --host 0.0.0.0 --port 8080


Build Docker:


docker build -t aggregator .
docker run -p 8080:8080 -v $(pwd)/data:/app/data -e DEDUP_DB=/app/data/dedup.db aggregator


Run tests:
pytest -q