from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('done', views.DoneView.as_view()),
    path('list', views.ListFeedBack.as_view()),
    path('detail/<int:pk>', views.DetailFeedBack.as_view()), # переменная обязательно pk если используется DetailView, либо делаем поиск по slug
    path('update/<int:pk>', views.FeedbackViewUpdate.as_view()), # переменная обязательно pk если используется DetailView, либо делаем поиск по slug
    path('', views.FeedbackView.as_view()), #.as_view()
    path('<int:id_feedback>', views.FeedBackUpdateView.as_view()),

]