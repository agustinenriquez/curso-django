from .models import Curso
from django import forms
from django.forms import ModelMultipleChoiceField


class CursoForm(forms.ModelForm):
    cursos = forms.ModelMultipleChoiceField(queryset=None)
    
    class Meta:
        model = Curso
        fields = '__all__' # Todos los campos del modelo Curso

    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields['cursos'].queryset = Curso.objects.all()
