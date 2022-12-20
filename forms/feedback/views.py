from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
# реализация через  Class Based Views:
# переписываем код в class FeedbackView(View), написанный через функции закомментированные
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView


# class FeedbackView(View):
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, 'feedback/load_file.html', context={'form': form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'feedback/load_file.html', context={'form': form})
#
# class FeedbackView(FormView):
#     form_class = FeedbackForm
#     template_name = 'feedback/load_file.html'
#     success_url = '/done'
#
#     def form_valid(self, form):
#         form.save()
#         return super(FeedbackView, self).form_valid(form)
#     # в context летит переменная 'form'

class FeedbackView(CreateView): #аналог FormView но не нужнопрописывать метод form_valid
    model = Feedback
    # form_class = FeedbackForm #можно не указывать, но нужно атрибут fields
    fields = '__all__' #если указать не все, то можно словить ошибку если есть поля с NULL
    template_name = 'feedback/feedback.html'
    success_url = '/done'

class FeedbackViewUpdate(UpdateView):#нужен если данные нужно идентифицировать и обновить
    model = Feedback
    form_class = FeedbackForm #можно не указывать, но нужно атрибут fields
    template_name = 'feedback/feedback.html'
    success_url = '/done'

# def index(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST) #в случае создания формы на основе модели форма заполняется автоматически
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # feed = Feedback(     #в случае создания формы на основе модели нам уже не нужно это
#             #     name=form.cleaned_data['name'],
#             #     surname=form.cleaned_data['surname'],
#             #     feedback=form.cleaned_data['feedback'],
#             #     rating=form.cleaned_data['rating'],
#             # )
#             # feed.save()
#             form.save() #в случае создания формы на основе модели остается только сохранить ее
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback/feedback.html', context={'form': form})

class FeedBackUpdateView(View):
    def get(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
        return render(request, 'feedback/feedback.html', context={'form': form})


# def update_feed(request, id_feedback):  #изменение значений БД через форму
#     feed = Feedback.objects.get(id=id_feedback)
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST, instance=feed)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForm(instance=feed)
#     return render(request, 'feedback/feedback.html', context={'form': form})

# здесь нужно вывести только шаблон -> используем наследование от TemplateView

class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['name'] = 'Ivanov'
        # context['date'] = '26/06/22'
        return context


# def done(request):
#     return render(request, 'feedback/done.html')

class ListFeedBack(ListView):  # ListView лучше для отображения списка данных из БД
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    # данные кладутся в переменную object_listб можно ее переименовать
    context_object_name = 'all_feed'

    def get_queryset(self):  # отвечает за получение данных из нашей модели
        queryset = super().get_queryset()
        # filter_qs = queryset.filter(rating__gt=3) # если нужно указать отзывы больше трех например
        # return filter_qs
        return queryset

# class ListFeedBack(TemplateView):
#     template_name = 'feedback/list_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['all_feed'] = Feedback.objects.all()
#
#         return context

# class DetailFeedBack(TemplateView):
#     template_name = 'feedback/detail_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['current'] = Feedback.objects.get(id=kwargs['id_feedback'])
#         return context


class DetailFeedBack(DetailView): # DetailView для отображения детальной информации из одной записи
    template_name = 'feedback/detail_feedback.html'
    model = Feedback # в context передается переменная по имени модели feedback или можно object
    # равноценно записи context_object_name = 'feedback' куда можно передать другое навание переменной


