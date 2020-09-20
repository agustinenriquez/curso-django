from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("lista_productos/", views.listado_de_productos, name="listado_productos"),
    path("scrap/dolar/", views.scrap_dollar, name="scrap_dollar"),
    path("cotizacion-dolar", views.cotizacion_dolar, name="cotizacion-dolar"),
    path("aeropuertos", views.aeropuertos, name="aeropuertos"),
    path("aeropuertos/json/", views.aeropuertos_json, name="aeropuertos-json"),
    path("crear-curso", views.crear_curso, name="crear-curso"),
    path("alta-curso", views.formulario_curso, name="alta-curso"),
    path("unform/", views.unform, name="unform"),
]