from django.contrib import admin
from .models import Curso, Contacto
# Register your models here.


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "inscriptos")


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    class Meta:
        model = Contacto
        fields = '__all__'
