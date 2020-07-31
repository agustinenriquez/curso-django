from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("listado-de-cursos/", views.listado_de_cursos, name="listado-de-cursos"),
    path("crear-curso/", views.formulario_curso, name="crear-curso"),
    path("detalle-curso/<int:pk>/", views.detalle_curso, name="detalle-curso"),
    path("inscripcion-curso/<int:pk>", views.inscripcion_curso, name="inscripcion-curso"),
    path("contacto/", views.contacto, name="contacto"),
    path("busqueda/", views.busqueda, name="busqueda"),
]