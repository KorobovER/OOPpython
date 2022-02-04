# Generated by Django 3.2.9 on 2021-12-16 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_bb_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=120, verbose_name='Название')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('body', models.TextField(blank=True, db_index=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='additionalimage',
            name='bb',
        ),
        migrations.RemoveField(
            model_name='bb',
            name='author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='advuser',
            name='send_messages',
        ),
        migrations.DeleteModel(
            name='AdditionalImage',
        ),
        migrations.DeleteModel(
            name='Bb',
        ),
    ]