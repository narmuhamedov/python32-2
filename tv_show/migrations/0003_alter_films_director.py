# Generated by Django 4.2.5 on 2023-09-14 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show', '0002_alter_films_options_films_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='director',
            field=models.CharField(max_length=100, null=True, verbose_name='Укажите директора'),
        ),
    ]
