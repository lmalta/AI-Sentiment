FROM python:3.12-slim

WORKDIR /app

COPY ai.py .

RUN pip install --no-cache-dir fastapi "uvicorn[standard]" transformers torch

EXPOSE 9000

CMD ["uvicorn", "ai:app", "--host", "0.0.0.0", "--port", "9000"]
