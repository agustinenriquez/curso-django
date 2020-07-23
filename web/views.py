from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Curso
from .forms import CursoForm
# Create your views here.


def index(request):
    cursos = Curso.objects.all() # SELECT * FROM Products
    context = {"cursos": cursos, "cursoform": CursoForm()}
    return render(request, "web/listado_cursos.html", context)

def listado_de_cursos(request):
    cursos = {}
    # Consulta SQLite 
    for curso in Curso.objects.all(): 
        cursos[curso.name] = curso.price
    return JsonResponse(curso)

def crear_curso(request):
    new_curso = Curso.objects.create(name=request.POST['name'], price=request.POST['price'])
    if new_curso:
        return HttpResponse("OK")
    else:
        return HttpResponse("Not created.")

def formulario_curso(request):
    form = CursoForm
    initial_curso = Curso.objects.last()
    form.base_fields['name'].initial = initial_curso.name
    form.base_fields['price'].initial = initial_curso.price
    context = {"form": form}
    return render(request, "web/alta_cursos.html", context)
