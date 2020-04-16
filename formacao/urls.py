from django.urls import path
from . import views
from hashlib import blake2b

app_name = 'formacao'
urlpatterns = [
    path(blake2b(b'agentes_selecionados').hexdigest()+'/', views.listar_agente_selecionado, name='listar-selecionados'),
    path(blake2b(b'consultar').hexdigest()+'/', views.consultar_formacao, name='consultar-formacao'),
    path(blake2b(b'aera_formacao').hexdigest()+'/', views.area_formacao, name='area-formacao'),
    path(blake2b(b'conclusao_formacao').hexdigest()+'/', views.registar_conclusao_formacao, name='conclusao-formacao'),
    path(blake2b(b'listar_agente_formacao').hexdigest()+'/', views.listar_agente_formacao, name='listar-agente-formacao'),
    path(blake2b(b'listar_todos_concluiram').hexdigest()+'/', views.listar_todos_terminaram_formacao, name='listar-concluiram'),
    path(blake2b(b'adicionar_agente_formacao').hexdigest()+'/', views.adicionar_agente_formacao, name='adicionar-agente-formacao'),
    path('remover_agente_selecionado/', views.remover_lista_selecionado, name='remover-selecionado'), # url via ajax
    path(blake2b(b'remover_conclusao').hexdigest()+'/', views.remover_lista_conclusao, name='remover-conclusao'),
    path(blake2b(b'informacao_conclusao').hexdigest()+'/<int:id>/', views.visualizar_informacao_conclusao, name='informacao-conclusao'),
    path(blake2b(b'atualizar_conclusao_formacao').hexdigest()+'/<int:id>/', views.atualizar_conclusao_formacao, name='atualizar-conclusao'),
    path(blake2b(b'atualizar_selecionado').hexdigest()+'/<int:id>/', views.atualizar_selecionado_formacao, name='atualizar-selecionado'),
    path(blake2b(b'agente_presente_formacao').hexdigest()+'/<int:id>/', views.marca_precensa_selecionado, name='agente_presente'),
    path(blake2b(b'buscar_selecionado_atualizacao').hexdigest()+'/', views.buscar_selecionado_atualizar, name='buscar-selecionado'),
    path(blake2b(b'consultar_idade').hexdigest()+'/', views.calcula_idade, name='idade'),
    path(blake2b(b'registar_documento').hexdigest()+'/', views.registar_documentos, name='documento'),
    path(blake2b(b'listar_documentos').hexdigest()+'/',  views.listar_documentos, name='listar-docs'),
    path(blake2b(b'atualizar_documento').hexdigest()+'/<int:id>/', views.atualizar_documento, name='atualizar-documento'),
    path(blake2b(b'consultar_docs').hexdigest()+'/', views.consultar_documento, name='consultar-documento'),
    path(blake2b(b'eliminar_documento').hexdigest()+'/<int:id>/', views.eliminar_documento, name='eliminar-documento'),
    path(blake2b(b'imprimir_ficha_formacao').hexdigest()+'/<int:id>/', views.ficha_formacao, name='imprimir-ficha')
    
    #path('buscar_terminou_atualizacao/', views.buscar_conclusao_atualizacao, name='buscar-conclusao'),
    #path(buscar_terminou_atualizacao'consultar_formacao/', views.consultar_formacoes, name='remover-conclusao'),
    

]
