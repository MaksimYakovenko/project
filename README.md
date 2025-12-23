# Movie Catalog - Docker Setup

## Опис проєкту

Проєкт Movie Catalog складається з трьох контейнерів:
- **db**: PostgreSQL база даних
- **backend**: Django REST API
- **frontend**: Vue.js фронтенд з Vite

## Вимоги

- Docker
- Docker Compose

## Запуск проєкту

### 1. Побудова та запуск всіх контейнерів

```bash
docker-compose up --build
```

Або запуск у фоновому режимі:

```bash
docker-compose up -d --build
```

### 2. Перевірка статусу контейнерів

```bash
docker-compose ps
```

### 3. Доступ до сервісів

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **PostgreSQL**: localhost:5432

### 4. Зупинка контейнерів

```bash
docker-compose down
```

Для видалення томів (даних БД):

```bash
docker-compose down -v
```

## Корисні команди

### Перегляд логів

```bash
# Всі сервіси
docker-compose logs -f

# Конкретний сервіс
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f db
```

### Виконання команд у контейнері

```bash
# Backend (Django)
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py shell

# Frontend
docker-compose exec frontend npm install
docker-compose exec frontend npm run build

# База даних
docker-compose exec db psql -U postgres -d movie_catalog
```

### Перезапуск окремого сервісу

```bash
docker-compose restart backend
docker-compose restart frontend
```

### Перебудова окремого контейнера

```bash
docker-compose up -d --build backend
docker-compose up -d --build frontend
```

## Структура проєкту

```
.
├── docker-compose.yml       # Конфігурація Docker Compose
├── backend/
│   ├── Dockerfile          # Dockerfile для Django
│   ├── .dockerignore       # Файли, що ігноруються при білді
│   └── ...
├── frontend/
│   ├── Dockerfile          # Dockerfile для Vue.js
│   ├── .dockerignore       # Файли, що ігноруються при білді
│   └── movie-catalog/
│       └── ...
```

## Налаштування

### Змінні оточення

Змінні оточення налаштовані в `docker-compose.yml`:

**База даних:**
- `POSTGRES_DB=movie_catalog`
- `POSTGRES_USER=postgres`
- `POSTGRES_PASSWORD=postgres`

**Backend:**
- `DB_HOST=db`
- `DB_PORT=5432`
- `DJANGO_SETTINGS_MODULE=config.settings`

**Frontend:**
- `VITE_API_URL=http://localhost:8000`

### Персистентність даних

Дані PostgreSQL зберігаються в Docker volume `postgres_data`, що дозволяє зберегти їх після перезапуску контейнерів.

## Режим розробки

Проєкт налаштований для режиму розробки:
- Код монтується як volume, зміни відразу відображаються
- Frontend: hot-reload через Vite
- Backend: автоматичний перезапуск Django dev сервера

## Troubleshooting

### Помилка підключення до БД

Якщо backend не може підключитись до БД, переконайтеся що:
1. Контейнер `db` запущений і здоровий (healthcheck)
2. PostgreSQL готовий приймати з'єднання

### Порт вже використовується

Якщо порти 5173, 8000 або 5432 вже зайняті, змініть їх в `docker-compose.yml`:

```yaml
ports:
  - "NEW_PORT:5173"  # Frontend
  - "NEW_PORT:8000"  # Backend
  - "NEW_PORT:5432"  # PostgreSQL
```

### Очистка Docker ресурсів

```bash
# Видалити всі контейнери, образи та томи проєкту
docker-compose down -v --rmi all

# Видалити невикористовувані Docker ресурси
docker system prune -a
```
