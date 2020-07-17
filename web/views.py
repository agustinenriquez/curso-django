from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt
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
