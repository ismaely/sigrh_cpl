
from django import forms
from django.forms import ModelForm
from header.opcoesModel import (GENERO, PATENTE, MOTIVO_BAIXA, MOTIVO_DESPROMOCAO, NIVEL_ACADEMICO,
 IDADE_LIMITE, IDADE_INTERVALOS, TIPO_LISTA_FORMACAO, REFORMA_ANTICIPADA, MOTIVO_DISCILINAR )
from pessoal_quadro.models import Disciplina
from formacao.models import Selecionado_formacao, Formacao_conclusao


#formulario para gerar a lista em pdf normal
class NormalPatente_Form(forms.Form):
    patente = forms.CharField(max_length=100, widget=forms.Select(choices=PATENTE))
    genero = forms.CharField(max_length=12, required=False, widget=forms.Select(choices=GENERO))
    titulo = forms.CharField(max_length=90, required=True)
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','length':3000}))
    

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
    anticipada = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=REFORMA_ANTICIPADA))
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'length':3000}))
    

   #formulario para gerar a lista em pdf das Baixas  
class BaixaLista_Form(forms.Form):
    motivo = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=MOTIVO_BAIXA))
    titulo = forms.CharField(max_length=90, required=True)
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','length':3000}))
    

#formulario para gerar a lista em pdf dos processo disciplinar
class DisciplinarLista_Form(forms.Form):
    ANO = []
    ANO.append(('', ''))
    for p in Disciplina.objects.select_related('agente').all():
        desp = p.data.split('/')
        if ANO.count((desp[2],desp[2])) == 0:
            ANO.append((str(desp[2]),str(desp[2])))
    motivo = forms.CharField(max_length=100, required=False, widget=forms.Select(choices=MOTIVO_DISCILINAR ))
    titulo = forms.CharField(max_length=90, required=True)
    ano=forms.CharField(max_length=90,required=False,  widget=forms.Select(choices=ANO))
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','length':3000}))
    

#formulario para gerar a lista em pdf das formações realizada e selecionada
class FormacaoLista_Form(forms.Form):
    ANO = []
    ANO.append(('', ''))
    for p in Selecionado_formacao.objects.select_related('agente').all():
        desp = p.data.split('-')
        if ANO.count((desp[2],desp[2])) == 0:
            ANO.append((str(desp[0]),str(desp[0])))
    for p in Formacao_conclusao.objects.select_related('agente').all():
        desp = p.data_conclusao.split('/')
        if ANO.count((desp[2],desp[2])) == 0:
            ANO.append((str(desp[2]),str(desp[2])))
    tipo = forms.CharField(max_length=100, widget=forms.Select(choices=TIPO_LISTA_FORMACAO))
    titulo = forms.CharField(max_length=90, required=True)
    ano=forms.CharField(max_length=90,required=False,  widget=forms.Select(choices=ANO))
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','length':3000}))
