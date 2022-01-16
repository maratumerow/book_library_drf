from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Book, Genre, Author


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанр"""

    list_display = ("title",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Автор"""

    list_display = ("id", "last_name", "first_name", "get_image")
    list_display_links = (
        "last_name",
        "first_name",
    )
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="70"')

    get_image.short_description = "Фото"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Книга"""

    list_display = ("title", "author_by", "draft", "get_image")
    list_filter = ("genre", "year", "author_by", "draft")
    list_editable = ("draft",)
    search_fields = ("title", "author_by", "genre")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="70"')

    get_image.short_description = "Обложка"
