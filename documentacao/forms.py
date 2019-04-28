
from django import forms
from django.forms import ModelForm
from documentacao.models import Documento, Imagam
from header.opcoesModel import DOCUMENTO_CATEGORIA

class DocumentoForm(ModelForm):
    class Meta:
        model = Documento
        fields = [
            'numero_ordem',
            'data_entrada',
            'categoria',
            'descricao',
            'arquivo',

        ]
        labels = {
            'numero_ordem': 'Numero de ordem',
            'data_entrada': 'Data de Entrada',
            'categoria': 'Categoria',
            'descricao': 'Descrição',
            'arquivo': 'Arquivo',

        }
        widgets = {
            'data_entrada': forms.DateInput(attrs={'class': 'datepicker form-control', 'data-inputmask': "'mask' : '99/99/9999'"}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'length': 900})
        }


class ConsultarDocumentoForms(forms.Form):
    categoria = forms.CharField(max_length=20, label="Categoria", widget=forms.Select(choices=DOCUMENTO_CATEGORIA, attrs={'type': 'search'}))




class ImageForm(ModelForm):
    um = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'text', 'class': 'form-control', 'id': 'salva1'}))
    dois = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'text',  'class': 'form-control', 'id': 'salva2'}))
    class Meta:
        model = Imagam
        fields = ['um', 'dois']
