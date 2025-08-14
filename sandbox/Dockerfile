# sandbox/Dockerfile
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 1) сначала зависимости — быстрее билды
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) а потом код
COPY . /app

EXPOSE 8000

# По умолчанию — runserver (можно переопределить в compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
