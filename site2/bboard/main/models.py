from django.db import models
from django.contrib.auth.models import AbstractUser
from .utilities import get_timestamp_path


class AdvUser(AbstractUser):
    fio = models.CharField(default=True, verbose_name='Введите ФИО', max_length=50)

    class Meta(AbstractUser.Meta):
        pass


def user_registrated(instance):
    pass


class Posts(models.Model):
    CHOICES_CATEGORY = (
        ("3D Дизайн", '3D Дизайн'),
        ('2D Дизайн', '2D Дизайн'),
        ('Эскиз', 'Эскиз'),
    )
    CHOICES_STATUS = (
        ("Новый", 'Новый'),
        ("Принято в работу", 'Принято в работу'),
        ("Выполнено", 'Выполнено'),
    )
    title = models.CharField(max_length=40, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.TextField(verbose_name='Категория', choices=CHOICES_CATEGORY)
    status = models.TextField(verbose_name='Статус заявки', choices=CHOICES_STATUS, default="Новый")
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')
    author = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name='Автор объявления')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Заявки'
        verbose_name = 'Заявка'
        ordering = ['-created_at']



