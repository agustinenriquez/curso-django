from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.shortcuts import render
from tienda.settings import DEBUG
from .forms import ProductForm
# Create your views here.


def index(request):
    todos_los_productos = Product.objects.all() # SELECT * FROM Products
    context = {"hello": "Hola, Mundo!", "products": todos_los_productos, "productform": ProductForm()}
    return render(request, "web/index.html", context)


def profile(request):
    return render(request, 'web/profile.html')


def acerca_de(request):
    return HttpResponse("Hola")


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


@csrf_exempt
def mi_endpoint(request):
    return 'Hola'


def cotizacion_dolar(request):
    # Ejercicio clase 1.
    req = requests.get("https://api.recursospython.com/dollar")
    cotizacion_dolar_json = json.loads(req.text)
    respuesta_html = f"<h1>Compra: {cotizacion_dolar_json['buy_price']} </h1></br><h1>Venta: {cotizacion_dolar_json['sale_price']}</h1>"
    return HttpResponse(respuesta_html)


def aeropuertos_json(request):
    # Ejercicio 2
    ruta_aeropuertos = os.path.dirname(os.path.abspath(__file__)) + "/aeropuertos.csv"
    diccionario_respuesta = {}
    with open(ruta_aeropuertos, mode="r") as file:
        aeropuertos = file.readlines()
        for aeropuerto in aeropuertos:
            aeropuerto_splitted = aeropuerto.split(",")
    return HttpResponse(diccionario_respuesta)


def aeropuertos(request):
    # Ejercicio 2
    ruta_aeropuertos = os.path.dirname(os.path.abspath(__file__)) + "/aeropuertos.csv"
    respuesta_html = ""
    with open(ruta_aeropuertos, mode="r") as file:
        aeropuertos = file.readlines()
        for aeropuerto in aeropuertos:
            aeropuerto_splitted = aeropuerto.split(",")
            respuesta_html += f"Ciudad: {aeropuerto_splitted[0]}, Estado:{aeropuerto_splitted[1]} </br>" 
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
