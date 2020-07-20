from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("lista_productos/", views.listado_de_productos, name="listado_productos"),
    path("crear-curso", views.crear_curso, name="crear-curso"),
    path("alta-curso", views.formulario_curso, name="alta-curso"),
]