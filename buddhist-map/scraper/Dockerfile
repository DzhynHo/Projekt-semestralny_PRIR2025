# Dockerfile.scraper

FROM python:3.11-slim

WORKDIR /scraper

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY scraper.py .
COPY insert_data.py .

CMD ["python", "insert_data.py"]
