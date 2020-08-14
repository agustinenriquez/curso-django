from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Curso, Alumno
from .forms import CursoForm, FormularioBusqueda, ContactoForm, FormularioInscripcion
from django.template import RequestContext
from django.core.mail import send_mail


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
    curso = Curso.objects.get(pk=kwargs['pk'])
    if request.method == 'POST':
        form = FormularioInscripcion(request.POST)
        context = {"curso": curso, "form": form}
        if form.is_valid():
            alumno, created = Alumno.objects.get_or_create(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                edad=form.cleaned_data['edad'],
                dni=form.cleaned_data['dni'],
                email=form.cleaned_data['email'],
                cursos=curso)
            if created:
                # send_email(f'Recibimos tu solicitud de inscripcion'
                #             'al curso {curso.name}. Vas a recibir un correo de '
                #             'confirmacion de inscripciones@cursodjango.com.ar',
                #             [form.cleaned_data['email']],
                #             fail_silently=False)
                context['form_valido'] = True
                return render(request, "web/inscripcion_curso.html", context)
            else:
                context['ya_inscripto'] = True
                return render(request, "web/inscripcion_curso.html", context)
        else:
            context['form_no_valido'] = True
            return render(request, "web/inscripcion_curso.html", context)
    else:
        form = FormularioInscripcion()
        return render(request, "web/inscripcion_curso.html", {"form": form})

