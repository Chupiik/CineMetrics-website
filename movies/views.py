from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Movie

def home(request):
    return render(request, 'movies/index.html')

def about_us(request):
    return render(request, 'movies/about_us.html')


def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movies_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})
