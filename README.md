# Інструкція по запуску проекту "Каталог фільмів"

## ✅ Що вже налаштовано:

### Backend (Django):
- ✅ JWT авторизація через djangorestframework-simplejwt
- ✅ Endpoints для login, logout, refresh токенів
- ✅ Endpoint /api/me/ для отримання даних користувача
- ✅ CORS налаштування для роботи з фронтендом
- ✅ REST API готове до розширення

### Frontend (Vue 3):
- ✅ Pinia store для управління авторизацією
- ✅ Axios interceptors для автоматичного оновлення токенів
- ✅ Vue Router з маршрутами для Home та Login
- ✅ Компоненти Login та Home
- ✅ Proxy налаштування для API запитів

---

## 🚀 Запуск проекту:

### 1. Налаштування Backend:

```cmd
cd C:\Users\Admin\project\backend

# Встановити залежності
pip install -r requirements.txt

# Виконати міграції
python manage.py makemigrations
python manage.py migrate

# Створити суперюзера (для адміністратора)
python manage.py createsuperuser

# Запустити сервер
python manage.py runserver
```

Backend буде доступний на: http://localhost:8000

### 2. Налаштування Frontend:

```cmd
cd C:\Users\Admin\project\frontend\movie-catalog

# Залежності вже встановлені, якщо ні:
npm install

# Запустити dev сервер
npm run dev
```

Frontend буде доступний на: http://localhost:8080

---

## 🔐 Endpoints API:

- `POST /api/token/` - Логін (отримання access токена)
- `POST /api/token/refresh/` - Оновлення access токена
- `POST /api/logout/` - Вихід із системи
- `GET /api/me/` - Отримання даних поточного користувача

---

## 📝 Що потрібно додати далі:

### 1. Моделі для фільмів (backend/movies/models.py):
```python
from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
```

### 2. Serializers для фільмів
### 3. Views для CRUD операцій з фільмами
### 4. Пошук та фільтрація
### 5. Права доступу (тільки адміністратор може створювати/змінювати/видаляти)
### 6. Frontend компоненти для відображення та управління фільмами

---

## 🐳 Docker Compose (буде потрібно налаштувати):

Створити docker-compose.yml для:
- PostgreSQL або MySQL
- Django backend
- Vue frontend (nginx)

---

## 🔧 Налаштування в settings.py що потрібно змінити для продакшена:

1. Змінити SECRET_KEY
2. DEBUG = False
3. Налаштувати ALLOWED_HOSTS
4. Підключити PostgreSQL замість SQLite
5. Змінити secure=False у cookies на secure=True (тільки для HTTPS)

---

## 📚 Структура проекту:

```
project/
├── backend/
│   ├── config/         # Налаштування Django
│   ├── movies/         # Додаток для фільмів + авторизація
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   └── movie-catalog/
│       ├── src/        # Основні компоненти
│       ├── views/      # Сторінки (Home, Login)
│       ├── stores/     # Pinia stores
│       └── utils/      # API та роутер
└── docker-compose.yml  # (Треба створити)
```

---

## ✨ Готові функції авторизації:

1. **Login**: Користувач вводить username/password, отримує JWT токени
2. **Auto-refresh**: Токени автоматично оновлюються через interceptors
3. **Logout**: Видалення токенів та виход із системи
4. **User info**: Отримання даних про користувача (username, groups, permissions)
5. **Protected routes**: Можна легко додати перевірку авторизації для маршрутів

---

## 🎯 Наступні кроки:

1. ✅ Створити міграції та запустити сервери
2. ⏳ Додати моделі для фільмів (Movie, Director, Genre)
3. ⏳ Створити ViewSets для CRUD операцій
4. ⏳ Додати пошук та фільтри
5. ⏳ Створити компоненти Vue для роботи з фільмами
6. ⏳ Налаштувати права доступу
7. ⏳ Створити docker-compose.yml
8. ⏳ Підключити PostgreSQL/MySQL
9. ⏳ Завантажити на GitHub

