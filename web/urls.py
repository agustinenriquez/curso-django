from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("acerca_de/", views.acerca_de, name="acerca_de"),
    path("lista_productos/", views.listado_de_productos, name="listado_productos"),
    path("scrap/dolar/", views.scrap_dollar, name="scrap_dollar"),
]