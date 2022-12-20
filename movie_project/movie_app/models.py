from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Room(models.Model):
    holl = models.IntegerField()
    room = models.IntegerField()

    def __str__(self):
        return f'этаж {self.holl} № {self.room}'

class Actor(models.Model):
    MALE = 'M'
    FAMALE = 'F'

    SET_GENDER = [
        (MALE, 'Мужчина'),
        (FAMALE, 'Женщина'),
            ]

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    gender = models.CharField(max_length=1, choices=SET_GENDER, default=MALE)
    room = models.OneToOneField(Room, on_delete=models.SET_NULL, null=True, blank=True) #связь ОДИН К ОДНОМУ

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.first_name}  {self.last_name}'
        else:
            return f'Актриса {self.first_name}  {self.last_name}'


    def get_info(self):
        return reverse('info_from_actor', args=[self.id])


class Director(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    director_email = models.EmailField()

    def get_info(self):
        return reverse('info_from_director', args=[self.id])

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'

class Movie(models.Model):
    # создание поля choices со списком значений-currency
    EURO = 'EUR'
    USD = 'USD'
    RUB = 'RUB'

    SET_CURRENCY = [
        (EURO, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)  # blank=True - возможность оставить поле пустым
    budget = models.IntegerField(default=1000000, validators=[MinValueValidator(1)])
    slug = models.SlugField(default='', null=False, db_index=True)  # смотри документацию Slugfield
    currency = models.CharField(max_length=3, choices=SET_CURRENCY, default=RUB)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True, related_name='movies')
    #делаем связь ОДИН КО МНОГИМ - внешний ключ ForeignKey
    #PROTECT не позволяет удалить обьект, если у него есть дочерние записи
    #CASCADE удаляет обьект и все связные записи
    #SET_NULL запись удалится, но в записях проставится 0
    # related_name='movies' позволяет изменить название movie_set

    #при записи ForeignKey создается обратная связь, которую можно вызвать в терминале
    #через команду a=Director.objects.all()[1] >> a.movie_set.all()


    actors = models.ManyToManyField(Actor)  # связь МНОГИЕ КО МНОГИМ

    # теперь метод сэйв переопределять ненужно, сделали через
    # админку через переменную prepopulated_fields
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     return super(Movie, self).save(*args, **kwargs)

    def get_info(self):
        return reverse('info_from_movie', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'
