# Generated by Django 4.1 on 2022-11-03 08:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
