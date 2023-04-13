from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_directores, name='lista_directores'),
    path('<int:director_id>/', views.detalle_director, name='detalle_director'),
    path('<int:director_id>/peliculas/', views.peliculas_director, name='peliculas_director'),
    path('pelicula/<int:pelicula_id>/', views.detalle_pelicula, name='detalle_pelicula'),
]
