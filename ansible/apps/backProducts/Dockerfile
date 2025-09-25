FROM python:3.12-slim

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .

RUN apt-get update && apt-get install -y wait-for-it && \
    pip install --no-cache-dir --upgrade -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
    
COPY . .

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
