# Generated by Django 4.1 on 2022-10-31 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0010_direcor_remove_movie_director_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('director_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Direcor',
        ),
    ]