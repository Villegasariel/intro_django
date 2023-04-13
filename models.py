from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField()

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
