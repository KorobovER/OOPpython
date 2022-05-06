from django.db import models
from django.contrib.auth.models import AbstractUser
from .utilities import get_timestamp_path


class AdvUser(AbstractUser):
    fio = models.CharField(default=True, verbose_name='Введите ФИО', max_length=50)

    class Meta(AbstractUser.Meta):
        pass


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        for bb in self.bb_set.all():
            bb.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Posts(models.Model):
    CHOICES_STATUS = (
        ("Новый", 'Новый'),
        ("Принято в работу", 'Принято в работу'),
        ("Выполнено", 'Выполнено'),
        ("Отменено", 'Отменено'),
    )
    title = models.CharField(max_length=40, verbose_name='Название')
    description = models.TextField(max_length=100, verbose_name='Описание')
    category = models.ForeignKey(Category, max_length=120, on_delete=models.CASCADE, verbose_name='Категория')
    status = models.TextField(verbose_name='Статус заявки', choices=CHOICES_STATUS, default="Новый")
    cancellation = models.CharField(max_length=40, verbose_name='Введите если отменяете заказ', blank=True, null=True)
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')
    author = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name='Автор объявления')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Заявки'
        verbose_name = 'Заявка'
        ordering = ['-created_at']


class AddCommentary(models.Model):
    bb = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='Заявки')
    comment = models.CharField(max_length=64, verbose_name='Название')

    class Meta:
        verbose_name_plural = 'Комментарий'
        verbose_name = 'Комментарий'


class AdditionalImage(models.Model):
    bb = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='Заявки')
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Изображение')

    class Meta:
        verbose_name_plural = 'Дополнительные иллюстрации'
        verbose_name = 'Дополнительная иллюстрация'
