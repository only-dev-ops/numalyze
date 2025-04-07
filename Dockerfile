FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

ENV PORT=5000
EXPOSE 5000

CMD gunicorn analysis:app --bind 0.0.0.0:$PORT
