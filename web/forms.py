from .models import Curso, Contacto
from django import forms
from django.core.validators import MaxValueValidator


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


class FormularioCursos(forms.Form):
    TURNOS = (('NOCHE', 'noche'), ('TARDE', 'tarde'), ('MAÑANA', 'manaña'))
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    inscriptos = forms.IntegerField(label="Inscriptos")
    solo_empresas = forms.BooleanField(label="¿Solo empresas?", required=False)
    turno = forms.ChoiceField(choices=TURNOS, required=True)
    fecha_inicio = forms.DateField(label="Fecha de inicio", input_formats=["%d/%m/%Y"])

    def __str(self):
        return self.nombre


class FormularioBusqueda(forms.Form):
    search_box = forms.CharField(label="Nombre", max_length=50, required=False)

    def __str(self):
        return self.search_box

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'


class FormularioInscripcion(forms.Form):
    TURNOS = (('NOCHE', 'noche'), ('TARDE', 'tarde'), ('MAÑANA', 'manaña'))
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido", max_length=50, required=True)
    edad = forms.IntegerField(label="Edad", required=True)
    telefono = forms.IntegerField(validators=[MaxValueValidator(9999999999)], label="Telefono", required=True)
    email = forms.EmailField(required=True)
    dni = forms.IntegerField(label="DNI", required=True)
    turno = forms.ChoiceField(choices=TURNOS, required=True)

    def __str__(self):
        return self.email
