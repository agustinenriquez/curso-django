from django.shortcuts import render, reverse
from django.http import JsonResponse, HttpResponseRedirect, Http404
from .models import Curso
from .forms import CursoForm, FormularioBusqueda, ContactoForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    """
        Devuelve el index con el listado de todos los cursos.
    """
    cursos = Curso.objects.all() # SELECT * FROM Curso
    context = {"cursos": cursos, "cursoform": CursoForm(), "searchform": FormularioBusqueda()}
    return render(request, "web/listado_cursos.html", context)


def listado_de_cursos(request):
    """
        Devuelve un Json con todos los cursos.
    """
    cursos = {}
    # Consulta SQLite 
    for curso in Curso.objects.all():
        cursos[curso.name] = curso.price
    return JsonResponse(curso)


@login_required
def formulario_curso(request):
    """
        Devuelve el formulario de creacion de cursos y procesa las requests POST
        que llegan a traves de él. Se necesia estar logueado.
    """
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = CursoForm()
        return render(request, "web/formulario_curso.html", {"form": form})


def contacto(request):
    """
        Devuelve el formulario de contacto definido en forms.py
    """
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = ContactoForm()
    return render(request, "web/formulario_contacto.html", {'form': form})


def busqueda(request):
    """
        Devuelve resultados de busqueda hechos a traves del input del base.html.
    """
    cursos = Curso.objects.filter(nombre__contains=request.GET['q'])
    return render(request, "web/resultado_busqueda.html", {"cursos": cursos})


def detalle_curso(request, *args, **kwargs):
    """
        Devuelve el detalle de un curso usando la pk definida en urls.py
    """
    if kwargs['pk']:
        curso = Curso.objects.get(pk=kwargs['pk'])
        return render(request, "web/detalle_curso.html", {"curso": curso})
    else:
        raise Http404


def inscripcion_curso(request, *args, **kwargs):
    """
        Devuelve el formulario de inscripcion de cursos y procesa las requests POST
        que llegan a traves de él.
    """
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "web/formulario_inscripcion.html", {"form_no_valido": True})
    else:
        form = CursoForm()
        return render(request, "web/formulario_inscripcion.html", {"form": form})
