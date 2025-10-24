FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/data /app/src && chmod -R 777 /app

RUN touch /app/src/__init__.py

RUN adduser --disabled-password --gecos '' appuser && chown -R appuser:appuser /app
USER appuser

COPY src/ ./src/
COPY README.md ./

EXPOSE 8080

CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
