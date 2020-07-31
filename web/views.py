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
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = CursoForm()
        return render(request, "web/formulario_curso.html", {"form": form})


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = ContactoForm()
    return render(request, "web/formulario_contacto.html", {'form': form})


def busqueda(request):
    cursos = Curso.objects.filter(nombre__contains=request.GET['query'])
    return render(request, "web/resultado_busqueda.html", {"cursos": cursos})


def detalle_curso(request, *args, **kwargs):
    """
        Devuelve el detalle de un curso usando la pk definida en urls.py
    """
    curso = Curso.objects.get(pk=kwargs['pk'])
    return render(request, "web/detalle_curso.html", {'curso': curso})


def inscripcion_curso(request, *args, **kwargs):
    """
        Devuelve el formulario de inscripcion de un curso segun id.
    """
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = CursoForm()
        return render(request, "web/inscripcion_curso.html", {"form": form})

