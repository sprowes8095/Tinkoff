from django import forms
from .models import Feedback
# тут создаем вид отображаемой страницы - формы для заполнения - на основе ранее созданной модели
# затем оперируем во Views

# в примере ниже мы сначала создали форму, а потом модель
# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Имя', min_length=2, max_length=15, \
#                            error_messages={'min_length': 'Слишком мало символов', \
#                                            'max_length': 'Слишком много символов', \
#                                            'required': 'Укажите хотя бы один символ'
#                                            })
#     surname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs = {'rows':10, 'cols':20})) # виджет для отображения поля для текста
#
#     rating = forms.IntegerField(label='Рейтинг', max_value=5, min_value=1)


# в примере ниже мы сначала создали модель, а потом создаем форму на ее основе
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # обязательно либо fields либо exclude
        # fields = ['name', 'surname', 'feedback','rating']
        fields = '__all__'  # чтобы не писать все поля вручную
        # exclude = ['rating']
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг'
        }
        error_messages = {
            'name': {
                'min_length': 'Слишком мало символов',
                'max_length': 'Слишком много символов',
                'required': 'Укажите хотя бы один симвов'
                },
            'surname': {
                'min_length': 'Слишком мало символов',
                'max_length': 'Слишком много символов',
                'required': 'Укажите хотя бы один симвов'
                }
        }

