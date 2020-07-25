from django.contrib import admin
from .models import Curso, Contacto, Alumno
# Register your models here.


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "inscriptos")


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    class Meta:
        model = Contacto
        fields = '__all__'


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("nombre_completo", "nombre", "apellido", "cursos", "email", "edad", )

    def nombre_completo(self, obj):
        return f'{obj.nombre} {obj.apellido}'
    nombre_completo.short_description = 'Nombre Completo'
