from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Director, Genre, Movie


class UserMeSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True, slug_field="name", read_only=True
    )
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "groups", "permissions"]

    def get_permissions(self, obj):
        perms = obj.get_all_permissions()
        return list(perms)


class DirectorSerializer(serializers.ModelSerializer):
    """Serializer для режисера"""
    class Meta:
        model = Director
        fields = ['id', 'name']


class GenreSerializer(serializers.ModelSerializer):
    """Serializer для жанру"""
    class Meta:
        model = Genre
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    genre_name = serializers.CharField(source='genre.name', read_only=True)
    director_name = serializers.CharField(source='director.name', read_only=True)

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'description', 'year',
            'genre', 'genre_name',
            'director', 'director_name',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class MovieListSerializer(serializers.ModelSerializer):
    genre_name = serializers.CharField(source='genre.name', read_only=True)
    director_name = serializers.CharField(source='director.name', read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'genre_name', 'director_name']
