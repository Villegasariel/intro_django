from django.shortcuts import render, get_object_or_404
from .models import Director, Pelicula

def lista_directores(request):
    directores = Director.objects.all()
    return render(request, 'lista_directores.html', {'directores': directores})

def detalle_director(request, director_id):
    director = get_object_or_404(Director, pk=director_id)
    return render(request, 'detalle_director.html', {'director': director})

def peliculas_director(request, director_id):
    director = get_object_or_404(Director, pk=director_id)
    peliculas = Pelicula.objects.filter(director=director)
    return render(request, 'peliculas_director.html', {'director': director, 'peliculas': peliculas})

def detalle_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
    return render(request, 'detalle_pelicula.html', {'pelicula': pelicula})
