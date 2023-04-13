from django.contrib import admin
from .models import Director, Pelicula

class PeliculaInline(admin.StackedInline):
    model = Pelicula

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    inlines = [PeliculaInline]

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'director', 'fecha_lanzamiento')
