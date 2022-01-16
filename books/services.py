from django.core.exceptions import ValidationError


def validate_size_image(file_obj):
    """ Проверка размера изображения """

    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {megabyte_limit}MB")


def validate_size_pdf(file_obj):
    """Проверка размера файла pdf"""

    megabyte_limit = 100
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {megabyte_limit}MB")
