from django.urls import path
from . import views

app_name = 'transferencia'
urlpatterns = [
    path('area_transferencia/', views.area_transferencia, name='area-transferencia'),
    path('transferencia/', views.registar_transferencia, name='adicionar-transferencia'),
    path('listar_pedido_transferencia/', views.listar_pedido_transferencia, name='listar-pedidos'),
    path('consultar/', views.consultar_transferencia, name='consultar-transferencia'),
    path('adicionar_troca/', views.adicionar_troca, name='troca'),
    path('listar_transferencia/', views.listar_agentes_transferido, name='listar'),
    path('listar_troca/', views.listar_troca_transferencia, name='listar-troca'),
    path('aprovar_transferencia/<int:id>/', views.aprovar_transferencia, name='aprovar-transferencia'),
    path('remover_pedido_transferencia/', views.remover_pedido_transferencia, name='remover-pedido'),
    path('atualizar_pedido_transferencia/<int:id>/', views.atualizar_pedido_transferencia, name='atualizar-pedido'),
    path('registar_documento/', views.registar_documentos, name='documento'),
    path('listar_documentos',  views.listar_documentos, name='listar-docs'),
    path('atualizar_documento/<int:id>/', views.atualizar_documento, name='atualizar-documento'),
    path('consultar_docs/', views.consultar_documento, name='consultar-documento'),
    path('eliminar_documento/<int:id>/', views.eliminar_documento, name='eliminar-documento'),
    path('emitir_guia_transferencia/<int:id>/', views.emitir_guia_transferencia, name='emitir-guia'),

]
