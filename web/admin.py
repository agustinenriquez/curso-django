from django.contrib import admin
from .models import Curso
# Register your models here.


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
