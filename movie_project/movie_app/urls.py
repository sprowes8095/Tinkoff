from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_movies),
    path('actors', views.AllActors.as_view()),
    path('actors/<int:pk>', views.ByActor.as_view(), name='info_from_actor'),
    path('directors', views.AllDirectors.as_view()),
    path('directors/<int:pk>', views.OneDirector.as_view(), name='info_from_director'),
    path('movie/<slug:slug>', views.OneMovie.as_view(), name='info_from_movie'),
]