from django.urls import path
from . import views
from hashlib import blake2b

app_name = 'estatistica'
urlpatterns = [
    path(blake2b(b'lista_nivel_academico').hexdigest()+'/', views.listar_nivel_academico, name='nivel_academico'),
    path(blake2b(b'lista_Transferencia').hexdigest()+'/', views.lista_Transferencia, name='transferencia_lista'),
    path(blake2b(b'lista_reforma').hexdigest()+'/', views.listar_reforma, name='reforma'),
    path(blake2b(b'lista_baixa').hexdigest()+'/', views.listar_baixa, name='baixa'),
    path(blake2b(b'lista_disciplinar').hexdigest()+'/', views.listar_disciplinar, name='lista-disciplinar'),
    path(blake2b(b'lista_formacao').hexdigest()+'/', views.listar_formacao, name='formacao'),
    path(blake2b(b'area_estatistica').hexdigest()+'/', views.area_estatistica, name='area'),
    path(blake2b(b'estatistica_reforma').hexdigest()+'/', views.estatistica_reforma, name='estatistica-reforma'),
    path(blake2b(b'estatistica_transferencia').hexdigest()+'/', views.estatistica_transferencia, name='estatistica-transferencia'),
    path(blake2b(b'estatistica_baixas').hexdigest()+'/', views.estatistica_baixas, name='estatistica-baixas'),
    path(blake2b(b'estatistica_reforma').hexdigest()+'/', views.estatistica_reforma, name='estatistica-reforma'),
    path(blake2b(b'estatistica_formacaoSelecionado').hexdigest()+'/', views.estatistica_selecionadoFormacao, name='estatistica-selecionado'),
    path(blake2b(b'estatistica_formacaoConclusao').hexdigest()+'/', views.estatistica_formacaoConcluida, name='estatistica-conclusao'),

]
