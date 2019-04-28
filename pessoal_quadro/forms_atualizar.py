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
    nome_pai = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_4, validar_string])
    nome_mae = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_4, validar_string])
    data_nascimento = forms.CharField(widget=forms.DateInput(attrs={'class': 'datepicker', 'data-inputmask': "'mask' : '99/99/9999'"}))
    bi = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control bi_mask'}))
    estado_civil = forms.CharField(max_length=20, widget=forms.Select(choices=ESTADO_CIVIL))
    provincia = forms.CharField(max_length=25, widget=forms.Select(choices=PROVINCIA))
    residencia = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_3])
    casa_numero = forms.CharField(max_length=7, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'class': 'form-control', 'data-inputmask': "'mask' : '(+244) 999-999-999'" }))
    email = forms.EmailField(max_length=80, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_email])
    genero = forms.CharField(max_length=12, widget=forms.Select(choices=GENERO))
    class Meta:
        model = Pessoa
        fields = ['nome', 'nome_pai', 'nome_mae', 'data_nascimento', 'bi', 'estado_civil', 'genero'
                  ,'provincia', 'residencia', 'casa_numero', 'telefone', 'email']

    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')
        data = data_nascimento.split('/')
        ano = DATA_ANO - int (data[2])
        if ano < 18:
            raise forms.ValidationError(" E menor de idade não pode fazer parte da policia")
        else:
            return data_nascimento



class AgenteForm_atualizar(ModelForm):
    numero_contribuite = forms.CharField(max_length=20, widget=forms.TextInput(attrs={ 'class': 'form-control nif_mask'}), validators=[validar_comprimento_3])
    numero_caixa_social = forms.CharField(max_length=20,  widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_numeros])
    nivel_academico = forms.CharField(max_length=20,  widget=forms.Select(choices=NIVEL_ACADEMICO))
    curso = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_4, validar_string])
    funcao = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_3])
    patente = forms.CharField(max_length=100,  widget=forms.Select(choices=PATENTE))
    categoria = forms.CharField(max_length=100, required=False)
    nip = forms.CharField(max_length=8, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}),)
    numero_agente = forms.CharField(max_length=10,  widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_3, validar_numeros])
    data_igresso = forms.CharField(widget=forms.DateInput(attrs={'class': 'datepicker form-control', 'data-inputmask': "'mask' : '99/99/9999'"}))
    foto_fardado = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'hidden', 'class': 'form-control', 'id': 'salva2'}))
    foto_civil = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'hidden', 'class': 'form-control', 'id': 'salva1'}))
    #widget=forms.TextInput(attrs={'type': 'hidden'})
    class Meta:
        model = Agente
        fields = ['numero_contribuite', 'numero_caixa_social', 'nivel_academico', 'curso', 'funcao', 'patente', 'categoria', 'numero_agente', 'nip', 'data_igresso', 'foto_fardado', 'foto_civil']

    # VALIDAR O CAMPO  numero_contribuite
    """def clean_numero_contribuite(self):
        numero_contribuite = self.cleaned_data.get('numero_contribuite')
        numero_caixa_social = self.cleaned_data.get('numero_caixa_social')
        try:
            valor = Agente.objects.get(numero_contribuite=numero_contribuite)
            if numero_contribuite == numero_caixa_social:
                raise forms.ValidationError(" o numero de contribuite não pode ser igual a da caixa social")
            elif valor.numero_contribuite is not None:
                raise forms.ValidationError(" o numero de contribuite ja existe")
        except Agente.DoesNotExist:
            return numero_contribuite"""



class OrgaoForm_atualizar(ModelForm):
    bi_id = forms.CharField(max_length=14, required=False, widget=forms.TextInput(attrs={'class': 'form-control bi_agente'}), validators=[validar_bi,consultar_bi_existe])
    orgao_colocacao = forms.CharField(required=False, widget=forms.Select(choices=ORGAO_COMANDOS))
    #localizacao = forms.CharField(max_length=40, required=False, widget=forms.TextInput(attrs={'placeholder': 'Localização'}),)
    data_colocacao = forms.CharField(required=False, widget=forms.DateInput(attrs={'class': 'datepicker', 'data-inputmask': "'mask' : '99/99/9999'"}))
    dispacho = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}),)
    #unidade = forms.CharField(max_length=90, required=False, widget=forms.TextInput(attrs={'placeholder': 'Unidade'}))
    class Meta:
        model = Orgao
        fields = ['orgao_colocacao', 'data_colocacao', 'dispacho']
