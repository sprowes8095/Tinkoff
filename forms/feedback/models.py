from django.db import models
from django.core.validators import MinLengthValidator

# тут задаем вид таблицы для БД - названия столбцов и их параметры, затем переходим в
# модуль forms.py для создания формы на основе модели

class Feedback(models.Model):
    name = models.CharField(max_length=15, validators=[MinLengthValidator(2)])
    surname = models.CharField(max_length=15, validators=[MinLengthValidator(2)])
    feedback = models.TextField()
    rating = models.PositiveIntegerField()
