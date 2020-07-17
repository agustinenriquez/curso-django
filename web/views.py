from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt
import os
import csv
import json
# Create your views here.


def index(request):
    return HttpResponse("<h1>Hola, Mundo!</h1>")


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

# Ejericios laboratorio 1

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
