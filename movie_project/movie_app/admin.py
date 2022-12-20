from django.contrib import admin, messages
from .models import Movie, Director, Actor, Room
from django.db.models import QuerySet


# Register your models here.

admin.site.register(Director)
admin.site.register(Actor)
# admin.site.register(Room)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):  # настройка отображения модели в админке
    list_display = [ 'actor','holl', 'room']


# создаем фильтр
# для этого создаем новый класс

class RatingFilter(admin.SimpleListFilter):
    title = 'фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'низкий рейтинг'),
            ('от 40 до 60', 'средний рейтинг'),
            ('>60', 'высокий рейтинг')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 60':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == '>60':
            return queryset.filter(rating__gte=60)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):  # настройка отображения модели в админке
    # fields = ['name', 'rating', 'currency'] #добавляем элементы для отображения в меню создания обьекта
    # exclude = ['slug'] #исключаем элемент, который не нужно отображать в форме создания обьекта
    readonly_fields = ['year']  # запрет к редактированию поля
    list_display = ['name', 'director', 'rating', 'currency', 'budget', 'rating_status']
    list_editable = ['currency','director', 'rating']  # возможность пользователю редактировать поля, кроме первого в листе отображения
    ordering = ['year', 'name']  # сортировка первичная и вторичная
    list_per_page = 10
    search_fields = ['name', 'rating']  # возможность осуществления поиска по заданным колонкам
    actions = ['set_usd', 'set_euro']
    list_filter = ['name', RatingFilter]
    # filter_horizontal = ['actors'] #для выбора нескольких позиций. это поле нельзя добавлять в list_display
    filter_vertical = ['actors'] #для выбора нескольких позиций
    prepopulated_fields = {'slug': ('name',)}  # словарь на основе кортежа

    # задаем вычисляемое поле (типа annotate) для отображения в админке. на вход идет переменная
    # класса Movie. Чтобы IDE подсказывала возможные методы и переменные нужно аннотировать переменную.
    # передаем ее в лист отображения list_display.
    # По умолчанию это вычисляемое поле без возможности сортировки - навешиваем декоратор с передачей
    # поля для желаемой сортировки, в переменную description передаем желаемое название поля

    @admin.display(ordering='rating',
                   description='Статус')  # admin.site.register(Movie,MovieAdmin) либо вешаем декоратор над классом модель-админ
    def rating_status(self, movie: Movie):
        if movie.rating < 65:
            return 'Зачем это смотреть?!'
        elif 65 <= movie.rating < 85:
            return 'Можно глянуть'
        elif movie.rating >= 85:
            return 'Топчик!'

    # Создание действия в админке: создаем новый метод, затем регистрируем его
    # в переменной actions  в виде списка

    @admin.action(description='Установить валюту доллар')
    def set_usd(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    # from django.contrib import  messages для того чтобы изменить тип
    # сообщения в level на ошибку
    @admin.action(description='Установить валюту евро')
    def set_euro(self, request, qs: QuerySet):
        count = qs.update(currency=Movie.EURO)  # метод возвращает количество
        self.message_user(request, f'было обновлено {count} записей', \
                          level=messages.ERROR)
