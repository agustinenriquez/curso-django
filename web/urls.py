from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("listado-de-cursos/", views.listado_de_cursos, name="listado-de-cursos"),
    path("crear-curso", views.crear_curso, name="crear-curso"),
    path("alta-curso", views.formulario_curso, name="alta-curso"),
]