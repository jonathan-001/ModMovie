from django.shortcuts import get_object_or_404, render
from .models import Movie

# Create your views here.
def home(request):
    movies = Movie.objects.all().order_by('-created_at')[:6]  # newest 6
    return render(request, 'home.html', {'movies': movies})


def details(request):
    return render(request, 'details.html')


def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    movie.view_count += 1
    movie.save(update_fields=['view_count'])
    return render(request, 'details.html', {'movie': movie})