from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from transferencia.models import Transferencia, Troca
from header.validators import consultar_bi_existe, validar_comprimento_4, validar_numeros, validar_string, validar_bi, consultar_numero_agente, consultar_bi
from header.opcoesModel import SITUACAO_TRANSFERENCIA, ORGAO_COMANDOS
import header


class TransferenciaForm(ModelForm):
    bi = forms.CharField(max_length=14, required=True, widget=forms.TextInput(attrs={'class': 'form-control bi_agente'}), validators=[validar_bi,consultar_bi_existe])
    orgao_destino = forms.CharField(max_length=100, widget=forms.Select(choices=ORGAO_COMANDOS))
    data_entrada = forms.CharField(widget=forms.DateInput(attrs={'class': 'datepicker form-control', 'data-inputmask': "'mask' : '99/99/9999'"}))
    dispacho = forms.CharField(max_length=30, required=False)
    motivo = forms.CharField(max_length=900, required=False, widget=forms.Textarea(attrs={'length':900}))
    arquivo = forms.FileField(required=False)
    numero_guia = forms.CharField(max_length=10)
    class Meta:
        model = Transferencia
        fields = [ 'orgao_destino', 'data_entrada', 'dispacho', 'motivo','arquivo', 'numero_guia']



class TrocaForm(ModelForm):
    bi1 = forms.CharField(max_length=14, required=True, validators=[validar_bi, consultar_bi_existe])
    bi2 = forms.CharField(max_length=14, required=True, validators=[validar_bi, consultar_bi_existe])
    origem_primeiro = forms.CharField(max_length=100, widget=forms.Select(choices=ORGAO_COMANDOS))
    destino_primeiro = forms.CharField(max_length=100, widget=forms.Select(choices=ORGAO_COMANDOS))
    origem_segundo = forms.CharField(max_length=100, required=False)
    destino_segundo = forms.CharField(max_length=100, required=False)
    data = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'datepicker form-control', 'data-inputmask': "'mask' : '99/99/9999'"}))
    motivo = forms.CharField(max_length=2000, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'length':900}))
    class Meta:
        model = Troca
        fields = ['origem_primeiro', 'destino_primeiro', 'origem_segundo', 'destino_segundo', 'data', 'motivo']


    def clean_bi2(self):
        bi_1 = self.cleaned_data['bi1']
        bi_2 = self.cleaned_data['bi2']
        if bi_1 == bi_2:
            raise ValidationError("O numero não e valido, não podem ser igual")
        return bi_2


    def clean_destino_primeiro(self):
        destino_primeiro = self.cleaned_data.get('destino_primeiro')
        origem_primeiro = self.cleaned_data.get('origem_primeiro')
        if destino_primeiro == origem_primeiro:
            raise forms.ValidationError(" Ops.. Erro o destino não pode ser igual a origem ")
        else: 
            return destino_primeiro


    
