FROM python:3.11-slim

WORKDIR /app

ENV PYTHONPATH=/app

# Копіюємо весь lesson_29 у контейнер
COPY . /app

# Встановлюємо залежності
RUN pip install --no-cache-dir sqlalchemy psycopg2-binary pytest

# За замовчуванням запускаємо тести
CMD ["pytest", "-v"]
