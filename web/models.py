from django.db import models


class Curso(models.Model):
    TURNOS = (('NOCHE', 'noche'), ('TARDE', 'tarde'), ('MAÑANA', 'manaña'),)
    nombre = models.CharField(max_length=50, blank=False)
    inscriptos = models.IntegerField(default=0)
    turno = models.CharField(max_length=50, choices=TURNOS, blank=True)

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    author = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=350)
    email = models.EmailField()

    def __str__(self):
        return self.author


class Alumno(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    edad = models.IntegerField(default=0)
    email = models.EmailField(max_length=254)
    cursos = models.ForeignKey("Curso", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
