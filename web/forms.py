from .models import Product
from django import forms
from django.forms import ModelMultipleChoiceField


class ProductForm(forms.ModelForm):
    cursos = forms.ModelMultipleChoiceField(queryset=None)
    
    class Meta:
        model = Product
        fields = '__all__' # Todos los campos del modelo Product

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['cursos'].queryset = Product.objects.all()


class UnForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
