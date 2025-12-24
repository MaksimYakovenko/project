from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ім'я режисера")

    class Meta:
        verbose_name = "Режисер"
        verbose_name_plural = "Режисери"
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва жанру")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"
        ordering = ['name']

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва фільму")
    description = models.TextField(verbose_name="Опис")
    year = models.IntegerField(verbose_name="Рік виходу")
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name='movies',
        verbose_name="Жанр"
    )
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name='movies',
        verbose_name="Режисер"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")

    class Meta:
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"
        ordering = ['-year', 'title']

    def __str__(self):
        return f"{self.title} ({self.year})"
