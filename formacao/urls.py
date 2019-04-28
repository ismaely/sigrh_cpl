from django.urls import path
from . import views

app_name = 'formacao'
urlpatterns = [
    path('agentes_selecionados/', views.listar_agente_selecionado, name='listar-selecionados'),
    path('consultar/', views.consultar_formacao, name='consultar-formacao'),
    path('aera_formacao/', views.area_formacao, name='area-formacao'),
    path('conclusao_formacao/', views.registar_conclusao_formacao, name='conclusao-formacao'),
    path('listar_agente_formacao/', views.listar_agente_formacao, name='listar-agente-formacao'),
    path('listar_todos_concluiram/', views.listar_todos_terminaram_formacao, name='listar-concluiram'),
    path('adicionar_agente_formacao/', views.adicionar_agente_formacao, name='adicionar-agente-formacao'),
    path('remover_agente_selecionado/', views.remover_lista_selecionado, name='remover-selecionado'),
    path('remover_conclusao/', views.remover_lista_conclusao, name='remover-conclusao'),
    path('informacao_conclusao/<int:id>/', views.visualizar_informacao_conclusao, name='informacao-conclusao'),
    path('atualizar_conclusao_formacao/<int:id>/', views.atualizar_conclusao_formacao, name='atualizar-conclusao'),
    path('atualizar_selecionado/<int:id>/', views.atualizar_selecionado_formacao, name='atualizar-selecionado'),
    path('agente_presente_formacao/<int:id>/', views.marca_precensa_selecionado, name='agente_presente'),
    path('buscar_selecionado_atualizacao/', views.buscar_selecionado_atualizar, name='buscar-selecionado'),
    path('consultar_idade/', views.calcula_idade, name='idade'),
    path('registar_documento/', views.registar_documentos, name='documento'),
    path('listar_documentos/',  views.listar_documentos, name='listar-docs'),
    path('atualizar_documento/<int:id>/', views.atualizar_documento, name='atualizar-documento'),
    path('consultar_docs/', views.consultar_documento, name='consultar-documento'),
    path('eliminar_documento/<int:id>/', views.eliminar_documento, name='eliminar-documento'),
    path('imprimir_ficha_formacao/<int:id>/', views.ficha_formacao, name='imprimir-ficha')
    
    #path('buscar_terminou_atualizacao/', views.buscar_conclusao_atualizacao, name='buscar-conclusao'),
    #path(buscar_terminou_atualizacao'consultar_formacao/', views.consultar_formacoes, name='remover-conclusao'),
    

]
