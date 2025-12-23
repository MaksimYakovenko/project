"""
Скрипт для заповнення бази даних тестовими даними
Запуск: docker-compose exec backend python populate_db.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from movies.models import Director, Genre, Movie

def populate():
    # Створюємо режисерів
    directors_data = [
        "Крістофер Нолан",
        "Квентін Тарантіно",
        "Стівен Спілберг",
        "Мартін Скорсезе",
        "Рідлі Скотт",
    ]
    
    directors = {}
    for name in directors_data:
        director, created = Director.objects.get_or_create(name=name)
        directors[name] = director
        print(f"{'Створено' if created else 'Існує'} режисер: {name}")
    
    # Створюємо жанри
    genres_data = [
        "Фантастика",
        "Бойовик",
        "Драма",
        "Трилер",
        "Кримінал",
    ]
    
    genres = {}
    for name in genres_data:
        genre, created = Genre.objects.get_or_create(name=name)
        genres[name] = genre
        print(f"{'Створено' if created else 'Існує'} жанр: {name}")
    
    # Створюємо фільми
    movies_data = [
        {
            "title": "Початок",
            "description": "Злодій, який краде корпоративні секрети через використання технології спільних снів, отримує завдання впровадити ідею в підсвідомість людини.",
            "year": 2010,
            "genre": "Фантастика",
            "director": "Крістофер Нолан"
        },
        {
            "title": "Темний лицар",
            "description": "Коли загроза, відома як Джокер, сіє хаос і безлад серед людей Готема, Бетмен повинен прийняти один з найбільших психологічних та фізичних випробувань.",
            "year": 2008,
            "genre": "Бойовик",
            "director": "Крістофер Нолан"
        },
        {
            "title": "Кримінальне чтиво",
            "description": "Життя двох найманих вбивць мафії, боксера, гангстера та його дружини переплітаються в чотирьох оповіданнях про насильство та викуплення.",
            "year": 1994,
            "genre": "Кримінал",
            "director": "Квентін Тарантіно"
        },
        {
            "title": "Список Шиндлера",
            "description": "В окупованій Польщі під час Другої світової війни, промисловець Оскар Шиндлер поступово стає стурбованим своїми єврейськими працівниками.",
            "year": 1993,
            "genre": "Драма",
            "director": "Стівен Спілберг"
        },
        {
            "title": "Острів проклятих",
            "description": "У 1954 році маршал США розслідує зникнення вбивці, яка втекла з лікарні для душевнохворих злочинців.",
            "year": 2010,
            "genre": "Трилер",
            "director": "Мартін Скорсезе"
        },
        {
            "title": "Гладіатор",
            "description": "Колишній римський генерал прагне помститися корумпованому імператорові, який вбив його сім'ю та відправив його в рабство.",
            "year": 2000,
            "genre": "Бойовик",
            "director": "Рідлі Скотт"
        },
        {
            "title": "Інтерстеллар",
            "description": "Команда дослідників подорожує через червоточину в космосі, намагаючись забезпечити виживання людства.",
            "year": 2014,
            "genre": "Фантастика",
            "director": "Крістофер Нолан"
        },
        {
            "title": "Джанго вільний",
            "description": "За допомогою німецького мисливця за головами звільнений раб вирушає врятувати свою дружину з рук жорстокого власника плантації.",
            "year": 2012,
            "genre": "Бойовик",
            "director": "Квентін Тарантіно"
        },
    ]
    
    for movie_data in movies_data:
        movie, created = Movie.objects.get_or_create(
            title=movie_data["title"],
            defaults={
                "description": movie_data["description"],
                "year": movie_data["year"],
                "genre": genres[movie_data["genre"]],
                "director": directors[movie_data["director"]],
            }
        )
        print(f"{'Створено' if created else 'Існує'} фільм: {movie_data['title']}")
    
    print(f"\n✅ Заповнення бази даних завершено!")
    print(f"   Режисерів: {Director.objects.count()}")
    print(f"   Жанрів: {Genre.objects.count()}")
    print(f"   Фільмів: {Movie.objects.count()}")

if __name__ == '__main__':
    populate()
