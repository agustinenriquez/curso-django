from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product
from django.shortcuts import render
from .forms import ProductForm
# Create your views here.


def index(request):
    todos_los_productos = Product.objects.all() # SELECT * FROM Products
    context = {"hello": "Hola, Mundo!", "products": todos_los_productos, "productform": ProductForm()}
    return render(request, "web/listado_cursos.html", context)

def listado_de_productos(request):
    # Consulta SQLite 
    list_products = {}
    for product in Product.objects.all():
        list_products[product.name] = product.price
    return JsonResponse(list_products)

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
