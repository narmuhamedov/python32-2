# Generated by Django 4.2.5 on 2023-09-28 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show', '0005_reviews'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
