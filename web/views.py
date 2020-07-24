from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Curso
from .forms import CursoForm, FormularioBusqueda, ContactoForm
from django.template import RequestContext
# Create your views here.


def index(request):
    cursos = Curso.objects.all() # SELECT * FROM Curso
    context = {"cursos": cursos, "cursoform": CursoForm(), "searchform": FormularioBusqueda()}
    return render(request, "web/listado_cursos.html", context)


def listado_de_cursos(request):
    cursos = {}
    # Consulta SQLite 
    for curso in Curso.objects.all():
        cursos[curso.name] = curso.price
    return JsonResponse(curso)


def formulario_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return HttpResponseRedirect(reverse("index"))
    else:
        form = CursoForm()
        return render(request, "web/formulario_curso.html", {"form": form})


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return HttpResponseRedirect(reverse("index"))
    else:
        form = ContactoForm()
    return render(request, "web/formulario_contacto.html", {'form': form})

def busqueda(request):
    cursos = Curso.objects.filter(name__contains=request.GET['q'])
    return render(request, "web/resultado_busqueda.html", {"cursos": cursos})