from django.urls import path
from . import views

app_name = 'estatistica'
urlpatterns = [
    path('lista_nivel_academico/', views.listar_nivel_academico, name='nivel_academico'),
    path('lista_Transferencia/', views.lista_Transferencia, name='transferencia_lista'),
    path('lista_reforma/', views.listar_reforma, name='reforma'),
    path('lista_baixa/', views.listar_baixa, name='baixa'),
    path('lista_disciplinar/', views.listar_disciplinar, name='lista-disciplinar'),
    path('lista_formacao/', views.listar_formacao, name='formacao'),
    path('area_estatistica/', views.area_estatistica, name='area'),
    path('estatistica_reforma/', views.estatistica_reforma, name='estatistica-reforma'),
    path('estatistica_transferencia/', views.estatistica_transferencia, name='estatistica-transferencia'),
    path('estatistica_baixas/', views.estatistica_baixas, name='estatistica-baixas'),
    path('estatistica_reforma/', views.estatistica_reforma, name='estatistica-reforma'),
    path('estatistica_formacaoSelecionado/', views.estatistica_selecionadoFormacao, name='estatistica-selecionado'),
    path('estatistica_formacaoConclusao/', views.estatistica_formacaoConcluida, name='estatistica-conclusao'),

    

]
