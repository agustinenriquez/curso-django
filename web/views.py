from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt
import json
import csv
import os
from django.shortcuts import render
from tienda.settings import DEBUG
from .forms import ProductForm
# Create your views here.


def index(request):
    todos_los_productos = Product.objects.all() # SELECT * FROM Products
    context = {"hello": "Hola, Mundo!", "products": todos_los_productos, "productform": ProductForm()}
    return render(request, "web/index.html", context)

def listado_de_productos(request):
    # Consulta SQLite 
    list_products = {}
    for product in Product.objects.all():
        list_products[product.name] = product.price
    return JsonResponse(list_products)

def scrap_dollar(request):
    req = requests.get("https://www.dolarhoy.com")
    soup = BeautifulSoup(req.text)
    precio_dolar = soup.find_all('div', {'class': 'col-6', 'class': 'text-center'})[0]
    return HttpResponse(precio_dolar.findChildren('span')[0].text.strip())

def cotizacion_dolar(request):
    # Ejercicio clase 1.
    req = requests.get("https://api.recursospython.com/dollar")
    cotizacion_dolar_json = json.loads(req.text)
    respuesta_html = (
        f"<h1>Compra: {cotizacion_dolar_json['buy_price']}</h1>"
        f"</br>"
        f"<h1>Venta: {cotizacion_dolar_json['sale_price']}</h1>"
    )
    return HttpResponse(respuesta_html)

def aeropuertos_json(request):
    # Ejercicio 2 A
    ruta_aeropuertos = os.path.dirname(os.path.abspath(__file__)) + "/aeropuertos.csv"
    aeropuertos_lista = []
    with open(ruta_aeropuertos, mode="r") as csvfile:
        aeropuertos = csv.reader(csvfile, delimiter=",")
        for aeropuerto in aeropuertos:
            item = {}
            item['ciudad'] = aeropuerto[0]
            item['estado'] = aeropuerto[1]
            item['lan'] = aeropuerto[2]
            item['lon'] = aeropuerto[3]
            aeropuertos_lista.append(item)          
    return JsonResponse(json.dumps(aeropuertos_lista), safe=False)

def aeropuertos(request):
    # Ejercicio 2 B
    ruta_aeropuertos = os.path.dirname(os.path.abspath(__file__)) + "/aeropuertos.csv"
    respuesta_html = ""
    with open(ruta_aeropuertos, mode="r") as csvfile:
        aeropuertos = csv.reader(csvfile, delimiter=",")
        for aeropuerto in aeropuertos:
            respuesta_html += f"Ciudad: {aeropuerto[0]}, Estado: {aeropuerto[1]} </br>" 
    return HttpResponse(respuesta_html)

def crear_curso(request):
    new_product = Product.objects.create(name=request.POST['name'], price=request.POST['price'])
    if new_product:
        return HttpResponse("OK")
    else:
        return HttpResponse("Not created.")

def formulario_curso(request):
    form = ProductForm
    initial_product = Product.objects.last()
    form.base_fields['name'].initial = initial_product.name
    form.base_fields['price'].initial = initial_product.price
    context = {"form": form}
    return render(request, "web/alta_cursos.html", context)


# Ejercicios de Laboratorio clase 2

def peliculas(request, nombre_pelicula, id_comentario):
    respuesta = f"Comentario numbero {id_comentario} de la pelicula {nombre_pelicula}"
    return HttpResponse(respuesta)
