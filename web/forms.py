from .models import Curso, Contacto
from django import forms


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
