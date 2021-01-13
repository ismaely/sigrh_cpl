from django import forms
from django.forms import ModelForm
from sigrh_cpl.settings import DATA_ANO, DATA_MES, DATE_FORMAT, DATE_INPUT_FORMATAR
from header.opcoesModel import APROVEITAMENTO, RAZAO_DA_POSSE, INSTITUICAO, PAIS_PRESPECTIVA, CURSOS_POLICIAL
from header.validators import consultar_bi_existe, validar_comprimento_4, validar_numeros, validar_string, validar_bi, consultar_numero_agente, consultar_bi
from formacao.models import Selecionado_formacao, Formacao_conclusao
from pessoal_quadro.models import Agente, Pessoa
import sweetify
import header


class SelecionarForm(ModelForm):
    bi = forms.CharField(max_length=14, required=True,widget=forms.TextInput(attrs={'class':'form-control formacao_bi_idade'}), validators=[validar_bi,consultar_bi_existe])
    curso = forms.CharField(max_length=900, widget=forms.Select(choices=CURSOS_POLICIAL))
    dispacho = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={ 'class':'form-control'}),)
    data = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), required=False)
    razao_posse = forms.CharField(max_length=40, required=False, widget=forms.Select(choices=RAZAO_DA_POSSE))
    instituicao = forms.CharField(max_length=900, required=False, widget=forms.Select(choices=INSTITUICAO))
    pais = forms.CharField(max_length=40, required=False, widget=forms.Select(choices=PAIS_PRESPECTIVA))
    #idade = forms.CharField(max_length=2, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}))

    class Meta:
        model = Selecionado_formacao
        fields = ['curso', 'dispacho', 'data', 'dispacho','razao_posse', 'instituicao', 'pais']

    def clean_bi(self):
        bi = header.views_core.retorna_numero_bi(self.cleaned_data.get('bi')) 
        if bi > 0:
            return bi
        else:
            raise forms.ValidationError(" O numero não é valido")
    


class FormacaoConlusao_Form(ModelForm):
    bi = forms.CharField(max_length=14, required=True, widget=forms.TextInput(attrs={'class':'form-control bi_agente'}), validators=[validar_bi,consultar_bi_existe])
    aproveitamento = forms.CharField(max_length=40, widget=forms.Select(choices=APROVEITAMENTO,attrs={'class': 'form-control'}))
    dispacho = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'data-inputmask': "'mask' : '9999/99'"}))
    data_conclusao = forms.CharField(label="Data:", widget=forms.DateInput(attrs={'type': 'date', 'data-inputmask': "'mask' : '99/99/9999'"}))
    comprovativo = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'type':'file', 'name':'file', 'class':'form-control'}))
    razao_posse = forms.CharField(max_length=40, required=False)
    #ultima_funcao = forms.CharField(max_length=40, required=False)
    pais = forms.CharField(max_length=40,  required=False)
    class Meta:
        model = Formacao_conclusao
        fields = ['aproveitamento', 'dispacho', 'data_conclusao', 'comprovativo', 'razao_posse', 'pais']

    def clean_aproveitamento(self):
        aproveitamento = self.cleaned_data.get('aproveitamento')
        if aproveitamento is None:
            raise forms.ValidationError(" O campo não pode ser vazio...")
        return aproveitamento
