
from django import forms
from django.forms import ModelForm
from header.opcoesModel import (GENERO, PATENTE, MOTIVO_BAIXA, MOTIVO_DESPROMOCAO, NIVEL_ACADEMICO, IDADE_LIMITE, TIPO_LISTA_FORMACAO,
REFORMA_ANTICIPADA, MOTIVO_DISCILINAR, GENERO_AMBOS, MENU_ESTATIS_TRANSFERENCIA, PATENTE_ESTATISTICA, MENU_ESTATIS_REFORMA, RAZAO_DA_POSSE)
from pessoal_quadro.models import Disciplina
from formacao.models import Selecionado_formacao, Formacao_conclusao


#formulario para gerar a lista em pdf normal
class Lista_Transferencia_Form(forms.Form):
    patente = forms.CharField(max_length=100, widget=forms.Select(choices=PATENTE))
    genero = forms.CharField(max_length=12, required=False, widget=forms.Select(choices=GENERO_AMBOS))
    titulo = forms.CharField(max_length=90, required=True)
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','length':3000}))
    data = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'name': 'date'}))

#formulario para gerar a lista em pdf de nivel academico
class NivelAcademico_Form(forms.Form):
    patente = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=PATENTE))
    nivel_academico = forms.CharField(max_length=40, widget=forms.Select(choices=NIVEL_ACADEMICO))
    titulo = forms.CharField(max_length=90, required=True)
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','length':3000}))
    
    
#formulario para gerar a lista em pdf das reforma
class ReformaLista_Form(forms.Form):
    patente = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=PATENTE))
    titulo = forms.CharField(max_length=90, required=True)
    data = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'name': 'date'}))
    anticipada = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=REFORMA_ANTICIPADA))
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'length':3000}))
    

   #formulario para gerar a lista em pdf das Baixas  
class BaixaLista_Form(forms.Form):
    motivo = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=MOTIVO_BAIXA))
    titulo = forms.CharField(max_length=90, required=True)
    data = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'name': 'date'}))
    data_final = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'name': 'date'}))
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','length':3000}))
    

#formulario para gerar a lista em pdf dos processo disciplinar
class DisciplinarLista_Form(forms.Form):
    motivo = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=MOTIVO_DISCILINAR ))
    titulo = forms.CharField(max_length=90, required=True)
    data = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'name': 'date'}))
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','length':3000}))
    

#formulario para gerar a lista em pdf das formações realizada e selecionada
class FormacaoLista_Form(forms.Form):
    data = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'name': 'date'}))
    tipo = forms.CharField(max_length=100, widget=forms.Select(choices=TIPO_LISTA_FORMACAO))
    titulo = forms.CharField(max_length=90, required=True)
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','length':3000}))


# formulario da estatistica de transferencia
class Estatistica_Transferencia_Form(forms.Form):
    patente = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=PATENTE_ESTATISTICA))
    titulo = forms.CharField(max_length=90, required=False)
    tipo = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=MENU_ESTATIS_TRANSFERENCIA))
    data = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'name': 'date'}))


#ESTATISTICA BAIXA
class Estatistica_Baixa_Form(forms.Form):
    patente = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=PATENTE_ESTATISTICA))
    titulo = forms.CharField(max_length=90, required=False)
    data = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'name': 'date'}))


# ESTATISTICA REFORMA
class Estatistica_reforma_Form(forms.Form):
    patente = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=PATENTE_ESTATISTICA))
    tipo = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=MENU_ESTATIS_REFORMA))
    data = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'name': 'date'}))

# estatistica para agentes selecionados
class Estatistica_AgentesSelecionados_Form(forms.Form):
    titulo = forms.CharField(max_length=90, required=False)
    patente = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=PATENTE_ESTATISTICA))
    data = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'name': 'date'}))


# estatistica de agente que concluiram a formação
class Estatistica_ConclusaoFormacao_Form(forms.Form):
    patente = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=PATENTE_ESTATISTICA))
    tipo = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=RAZAO_DA_POSSE))
    data = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'name': 'date'}))
