from rest_framework import viewsets, permissions, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book, Author, Genre
from . import serializers
from .permissions import IsAuthorOrReadOnly


class BookViewSet(viewsets.ModelViewSet):
    """Вывод списка книг и книги"""

    queryset = Book.objects.filter(draft=False)
    serializer_class = serializers.BookSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ["author_by", "genre"]
    search_fields = ["author_by__first_name", "author_by__last_name", "title"]
    ordering_fields = ["title"]
    permission_classes = (IsAuthorOrReadOnly,)


class BookCreateViewSet(viewsets.ModelViewSet):
    """Добавление книги"""

    queryset = Book.objects.filter(draft=False)
    serializer_class = serializers.BookCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class AuthorViewSet(viewsets.ModelViewSet):
    """Вывод авторов и автора"""

    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """Вывод жанров и жанра"""

    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer
