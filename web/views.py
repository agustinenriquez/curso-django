from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, reverse
from django.views.generic import CreateView, FormView, ListView

from .forms import (ContactoForm, CursoForm, FormularioBusqueda,
                    FormularioInscripcion, UserForm)
from .models import Alumno, Curso


class IndexList(ListView):
    model = Curso

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(nombre__contains="Django")


def index(request):
    cursos = Curso.objects.all()  # SELECT * FROM Curso
    context = {
        "cursos": cursos,
        "cursoform": CursoForm(),
        "searchform": FormularioBusqueda()}
    return render(request, "web/listado_cursos.html", context)


def listado_de_cursos(request):
    cursos = {}
    # Consulta SQLite
    for curso in Curso.objects.all():
        cursos[curso.name] = curso.price
    return JsonResponse(curso)


class FormularioCurso(FormView):
    form_class = CursoForm


def formulario_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            context = {
                "form": form,
                "formularioNoValido": "El formu no es valido."}
            return render(request, "web/formulario_curso.html", context)
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
    PATH_HTML_CURSO = "web/inscripcion_curso.html"
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
                context['form_valido'] = True
                return render(request, PATH_HTML_CURSO, context)
            else:
                context['ya_inscripto'] = True
                return render(request, PATH_HTML_CURSO, context)
        else:
            context['form_no_valido'] = True
            return render(request, PATH_HTML_CURSO, context)
    else:
        form = FormularioInscripcion()
        return render(request, PATH_HTML_CURSO, {"form": form})


class CreateUserView(CreateView):
    model = User
    form_class = UserForm
    success_url = "/"
    template_name = "web/create_user.html"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        login(self.request, self.object)
        return super().form_valid(form)

    def get_success_url(self): 
        return self.success_url
