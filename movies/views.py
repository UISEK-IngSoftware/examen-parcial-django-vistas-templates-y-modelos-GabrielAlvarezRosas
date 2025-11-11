from django.http import HttpResponse
from django.template import loader
from .models import Movie
from django.shortcuts import render

def index(request):
    movies = Movie.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movies': movies}, request))

def movie(request, id:int):
    movie = Movie.objects.get(id=id)
    template = loader.get_template('display_movie.html')
    context = {
        'movie': movie

    }
    return HttpResponse(template.render(context, request))