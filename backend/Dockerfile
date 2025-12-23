# Використовуємо офіційний Python образ
FROM python:3.12-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Встановлюємо системні залежності
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Копіюємо файл залежностей
COPY requirements.txt .

# Встановлюємо Python залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код проєкту
COPY . .

# Відкриваємо порт
EXPOSE 8000

# Скрипт для запуску
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]