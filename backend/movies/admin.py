from django.contrib import admin
from .models import Director, Genre, Movie


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'genre', 'director', 'created_at']
    list_filter = ['year', 'genre', 'director']
    search_fields = ['title', 'description']
    date_hierarchy = 'created_at'
    ordering = ['-year', 'title']
