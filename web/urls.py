from django.urls import path
from . import views
from .views import IndexList, FormularioCurso, CreateUserView

urlpatterns = [
    path("", IndexList.as_view(), name="index"),
    path("listado-de-cursos/", views.listado_de_cursos, name="listado-de-cursos"),
    path("crear-curso/", FormularioCurso.as_view(), name="crear-curso"),
    path("detalle-curso/<int:pk>/", views.detalle_curso, name="detalle-curso"),
    path("inscripcion-curso/<int:pk>", views.inscripcion_curso, name="inscripcion-curso"),
    path("contacto/", views.contacto, name="contacto"),
    path("busqueda/", views.busqueda, name="busqueda"),
    path("crear-usuario/", CreateUserView.as_view(), name="add-user"),
]