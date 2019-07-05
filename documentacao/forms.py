from django import forms
from django.forms import ModelForm
from documentacao.models import Documento
from header.opcoesModel import DOCUMENTO_CATEGORIA
from django.utils.translation import ugettext_lazy as _
from sigrh_cpl.settings import MAX_UPLOAD_SIZE, CONTENT_TYPES
from django.template.defaultfilters import filesizeformat
from django.contrib.contenttypes.models import ContentType

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
            'data_entrada': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'length': 900})
        }
   


class ConsultarDocumentoForms(forms.Form):
    categoria = forms.CharField(max_length=20, label="Categoria", widget=forms.Select(choices=DOCUMENTO_CATEGORIA, attrs={'type': 'search'}))



