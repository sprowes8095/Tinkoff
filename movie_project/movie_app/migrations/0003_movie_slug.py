# Generated by Django 4.1 on 2022-10-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_movie_budget_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
