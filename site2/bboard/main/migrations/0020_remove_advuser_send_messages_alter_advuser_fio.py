# Generated by Django 4.0.3 on 2022-04-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_advuser_send_messages_alter_advuser_fio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advuser',
            name='send_messages',
        ),
        migrations.AlterField(
            model_name='advuser',
            name='fio',
            field=models.CharField(default=True, max_length=50, verbose_name='Введите ФИО'),
        ),
    ]
