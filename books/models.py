from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

from .services import validate_size_image, validate_size_pdf


class Genre(models.Model):
    """Жанр"""

    title = models.CharField("Жанр", max_length=128, help_text="Жанр книги")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Author(models.Model):
    """Автор"""

    first_name = models.CharField(
        "Имя", max_length=128, help_text="Имя автора")
    last_name = models.CharField(
        "Фамилия", max_length=128, help_text="Фамилия автора"
    )
    image = models.ImageField(
        "Фото", upload_to="author/", blank=True, help_text="Фото автора"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    """Книга"""

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец книги"
    )
    author_by = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        verbose_name="Автор",
        related_name="author_by",
        null=True,
    )
    genre = models.ManyToManyField(
        Genre, verbose_name="Жанр", related_name="genre", blank=True
    )
    book_pdf = models.FileField(
        "pdf",
        upload_to="pdf/",
        help_text="Формат .pdf не более 100MB",
        validators=[
            FileExtensionValidator(allowed_extensions=["pdf"]),
            validate_size_pdf,
        ],
    )
    year = models.PositiveIntegerField("Год", help_text="Год издания")
    title = models.CharField("Название", max_length=256,
                             help_text="Название книги")
    description = models.TextField(
        "Описание", max_length=1024, blank=True, help_text="Описание книги"
    )
    image = models.ImageField(
        "Обложка",
        upload_to="book_cover/",
        blank=True,
        help_text="Формат .jpg не более 2MB",
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg"]),
            validate_size_image,
        ],
    )
    draft = models.BooleanField("Черновик", default=True)

    def __str__(self):
        return f"id {self.id}: {self.title} {self.author_by}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["-year"]
