from django.shortcuts import render, reverse
from django.http import JsonResponse, HttpResponseRedirect, Http404
from django.core.exceptions import PermissionDenied
from .models import Curso, Alumno
from .forms import CursoForm, FormularioBusqueda, ContactoForm, FormularioInscripcion
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


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
    if not request.user.is_superuser:
        raise PermissionDenied
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
    curso = Curso.objects.get(pk=kwargs['pk'])
    if request.method == 'POST':
        form = FormularioInscripcion(request.POST)
        context = {"curso": curso, "form": form}
        if form.is_valid():
            alumno, created = Alumno.objects.get_or_create(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                edad=form.cleaned_data['edad'],
                email=form.cleaned_data['email'],
                cursos=curso)
            if created:
                send_mail(
                    f'Recibimos tu inscripción a {{curso.nombre}}',
                    'Vas a recibir un correo de nuestro equipo para confirmar.',
                    'inscripciones@educacionit.com.ar',
                    [form.cleaned_data['email']],
                    fail_silently=False,
                )
                context["form_valido"] = True
                return render(request,
                    "web/formulario_inscripcion.html", context)
            else:
                context["ya_inscripto"] = True
                return render(request,
                    "web/formulario_inscripcion.html",
                    context)
        else:
            context["form_no_valido"] = True
            return render(request, "web/formulario_inscripcion.html", context)
    else:
        form = FormularioInscripcion()
        context = {"curso": curso, "form": form}
        return render(request, "web/formulario_inscripcion.html", context)
