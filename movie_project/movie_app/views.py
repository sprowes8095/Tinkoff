from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.db.models import F, Sum, Max, Min, Count, Avg

# Create your views here.

def all_movies(request):
    movies = Movie.objects.order_by('-rating','budget')
    # total =  movies.aggregate(Count('id'))

    return render(request, 'movie_app/all_movies.html', {'movies': movies, 'total': movies.count()})
#
# class OneMovie(TemplateView):
#     template_name = 'movie_app/one_movie.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['movie'] = Movie.objects.get(slug=kwargs['slug_movie'])
#         return context

class OneMovie(DetailView):
    template_name = 'movie_app/one_movie.html'
    model = Movie


# def one_movie(request, slug_movie:str):
#     movie = get_object_or_404(Movie, slug=slug_movie)
#     return render(request, 'movie_app/one_movie.html', {'movie': movie})


# def all_directors(request):
#     regists = Director.objects.all()
#     return render(request, 'movie_app/directors.html', {'regists': regists})

class AllDirectors(ListView):
    template_name = 'movie_app/directors.html'
    model = Director
    context_object_name = 'regists'

# class OneDirector(TemplateView):
#     template_name = 'movie_app/one_director.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['regist'] = Director.objects.get(id=kwargs['id_director'])
#         return context

class OneDirector(DetailView):
    template_name = 'movie_app/one_director.html'
    model = Director
    context_object_name = 'regist'


# def id_director(request, id_director: int):
#     director = get_object_or_404(Director, id=id_director)
#     return render(request, 'movie_app/one_director.html', {'regist': director})

# def all_actors(request):
#     actors = Actor.objects.all()
#     return render(request, 'movie_app/actors.html', {'actors': actors})

class AllActors(ListView):
    template_name = 'movie_app/actors.html'
    model = Actor
    context_object_name = 'actors'


# def by_actor(request, id_actor: int):
#     actor = get_object_or_404(Actor, id=id_actor)
#     return render(request, 'movie_app/actor.html', {'actor': actor})

# class ByActor(TemplateView):
#     template_name = 'movie_app/actor.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['actor'] = Actor.objects.get(id=kwargs['id_actor'])
#         return context
#
class ByActor(DetailView):
    template_name = 'movie_app/actor.html'
    model = Actor
    context_object_name = 'actor'

