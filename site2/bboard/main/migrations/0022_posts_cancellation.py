# Generated by Django 4.0.3 on 2022-05-06 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_posts_category_alter_posts_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='cancellation',
            field=models.CharField(default=1, max_length=40, verbose_name='Введите если отменяете заказ'),
            preserve_default=False,
        ),
    ]
