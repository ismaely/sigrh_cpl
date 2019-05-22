from django import forms
from django.forms import ModelForm
from sigrh_cpl.settings import DATA_ANO, DATA_MES
from header.opcoesModel import (ESTADO_CIVIL, GENERO, PATENTE,  MOTIVO_BAIXA, MOTIVO_DESPROMOCAO, MOTIVO_REFORMA, 
NIVEL_ACADEMICO, IDADE_LIMITE, NOMIACAO_TIPO, NOMIACAO_CATEGORIA, PROVINCIA, ORGAO_COMANDOS)
from header.validators import (consultar_bi_existe, validar_comprimento_4, validar_numero_caixa_social, validar_comprimento_3,
 validar_numeros, validar_string, validar_email, validar_bi, consultar_numero_agente, consultar_bi) 
from pessoal_quadro.models import Baixa, Feria, Orgao, Pessoa, Agente, Despromocao, Nomiacao_Cargo, Reforma




class PessoaForm_atualizar(ModelForm):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_4, validar_string])
    nome_pai = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nome_mae = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_nascimento = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'data-inputmask': "'mask' : '99/99/9999'"}))
    bi = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control bi_mask'}))
    estado_civil = forms.CharField(max_length=20, widget=forms.Select(choices=ESTADO_CIVIL))
    provincia = forms.CharField(max_length=25, widget=forms.Select(choices=PROVINCIA))
    municipio = forms.CharField(max_length=30, required=False, widget=forms.Select(choices=''))
    residencia = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_3])
    telefone = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'class': 'form-control', 'data-inputmask': "'mask' : '(+244) 999-999-999'" }))
    email = forms.EmailField(max_length=80, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_email])
    genero = forms.CharField(max_length=12, widget=forms.Select(choices=GENERO))
    class Meta:
        model = Pessoa
        fields = ['nome', 'nome_pai', 'nome_mae', 'data_nascimento', 'bi', 'estado_civil', 'genero'
                  ,'provincia',  'residencia', 'telefone', 'email', 'municipio']

    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')
        data = data_nascimento.split('-')
        ano = DATA_ANO - int (data[0])
        if ano < 18:
            raise forms.ValidationError(" E menor de idade não pode fazer parte da policia")
        else:
            return data_nascimento



class AgenteForm_atualizar(ModelForm):
    numero_contribuite = forms.CharField(max_length=20, widget=forms.TextInput(attrs={ 'class': 'form-control nif_mask'}))
    numero_caixa_social = forms.CharField(max_length=20,  widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_numeros])
    nivel_academico = forms.CharField(max_length=20,  widget=forms.Select(choices=NIVEL_ACADEMICO))
    curso = forms.CharField(max_length=80, required=False, widget=forms.Select(choices=''))
    #funcao = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_3])
    patente = forms.CharField(max_length=100,  widget=forms.Select(choices=PATENTE))
    categoria = forms.CharField(max_length=100, required=False)
    nip = forms.CharField(max_length=8, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}),)
    numero_agente = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_3, validar_numeros])
    data_igresso = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'data-inputmask': "'mask' : '99/99/9999'"}))
    foto_fardado = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'hidden', 'class': 'form-control', 'id': 'salva2'}))
    foto_civil = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'hidden', 'class': 'form-control', 'id': 'salva1'}))
    area_formacao = forms.CharField(max_length=30, required=False, widget=forms.Select(choices=''))
    #widget=forms.TextInput(attrs={'type': 'hidden'})
    class Meta:
        model = Agente
        fields = ['numero_contribuite', 'numero_caixa_social', 'nivel_academico', 'curso', 'patente', 'categoria', 'numero_agente', 'nip', 'data_igresso',
         'foto_fardado', 'foto_civil', 'area_formacao']


    def clean_data_igresso(self):
        data_igresso = self.cleaned_data.get('data_igresso')
        data = data_igresso.split('-')
        if int (data[0]) > DATA_ANO:
            raise forms.ValidationError(" A data de igresso não é valida!")
        else:
            return data_igresso
    #VALIDAR NUMERO DO AGENTE
    def clean_numero_agente(self):
        numero_agente = self.cleaned_data.get('numero_agente')
        nip = self.cleaned_data.get('nip')
        try:
            valor = Agente.objects.get(numero_agente=numero_agente)
            if numero_agente == nip:
                raise forms.ValidationError(" o numero do agente não pode ser igual ao nip")
            else:
                return numero_agente
        except Agente.DoesNotExist:
            return numero_agente



class OrgaoForm_atualizar(ModelForm):
    bi_id = forms.CharField(max_length=14, required=False, widget=forms.TextInput(attrs={'class': 'form-control bi_agente'}), validators=[validar_bi, consultar_bi_existe])
    orgao_colocacao = forms.CharField(required=False, widget=forms.Select(choices=ORGAO_COMANDOS))
    data_colocacao = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'data-inputmask': "'mask' : '99/99/9999'"}))
    dispacho = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'data-inputmask': "'mask' : '9999/99'"}))
    class Meta:
        model = Orgao
        fields = ['orgao_colocacao', 'data_colocacao', 'dispacho']
