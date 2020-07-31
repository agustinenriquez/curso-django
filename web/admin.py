from django.contrib import admin
from .models import Curso, Contacto, Alumno
# Register your models here.


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio",)


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    class Meta:
        model = Contacto
        fields = '__all__'


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    class Meta:
        model = Alumno
        fields = '__all__'
