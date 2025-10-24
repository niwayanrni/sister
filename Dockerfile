# Gunakan base image ringan
FROM python:3.11-slim

# Tentukan direktori kerja di dalam container
WORKDIR /app

# Salin file requirements lebih awal
COPY requirements.txt ./

# Install dependensi dengan pip
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Buat folder data dan ubah permission agar bisa ditulis oleh non-root user
RUN mkdir -p /app/data && chmod -R 777 /app

# Tambahkan user non-root
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser:appuser /app
USER appuser

# Salin seluruh kode sumber
COPY src/ ./src/
COPY README.md ./

# Buka port 8080 untuk akses FastAPI
EXPOSE 8080

# Jalankan FastAPI via uvicorn
CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
