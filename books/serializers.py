from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Author, Book, Genre


class GenreSerializer(serializers.ModelSerializer):
    """Список жанров"""

    class Meta:
        model = Genre
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    """Список авторов"""

    class Meta:
        model = Author
        fields = "__all__"


class CreatorSerializer(serializers.ModelSerializer):
    """Сериализация автор книги"""

    class Meta:
        model = User
        fields = ('username',)


class BookSerializer(serializers.ModelSerializer):
    """Список книг"""

    author_by = AuthorSerializer()
    genre = GenreSerializer(many=True)
    creator = CreatorSerializer()

    class Meta:
        model = Book
        exclude = ("draft",)


class BookCreateSerializer(serializers.ModelSerializer):
    """Добавление книги"""
    
    class Meta:
        model = Book
        exclude = ("draft", "creator")
