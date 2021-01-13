from django.urls import path
from . import views
from hashlib import blake2b

app_name = 'transferencia'
urlpatterns = [
    path(blake2b(b'area_transferencia').hexdigest()+'/', views.area_transferencia, name='area-transferencia'),
    path(blake2b(b'transferencia').hexdigest()+'/', views.registar_transferencia, name='adicionar-transferencia'),
    path(blake2b(b'listar_pedido_transferencia').hexdigest()+'/', views.listar_pedido_transferencia, name='listar-pedidos'),
    path(blake2b(b'consultar').hexdigest()+'/', views.consultar_transferencia, name='consultar-transferencia'),
    path(blake2b(b'adicionar_troca').hexdigest()+'/', views.adicionar_troca, name='troca'),
    path(blake2b(b'listar_transferencia').hexdigest()+'/', views.listar_agentes_transferido, name='listar'),
    path(blake2b(b'listar_troca').hexdigest()+'/', views.listar_troca_transferencia, name='listar-troca'),
    path(blake2b(b'aprovar_transferencia').hexdigest()+'/<int:id>/', views.aprovar_transferencia, name='aprovar-transferencia'),
    path('remover_pedido_transferencia/', views.remover_pedido_transferencia, name='remover-pedido'),
    path(blake2b(b'atualizar_pedido_transferencia').hexdigest()+'/<int:id>/', views.atualizar_pedido_transferencia, name='atualizar-pedido'),
    path(blake2b(b'registar_documento').hexdigest()+'/', views.registar_documentos, name='documento'),
    path(blake2b(b'listar_documentos').hexdigest()+'/',  views.listar_documentos, name='listar-docs'),
    path(blake2b(b'atualizar_documento').hexdigest()+'/<int:id>/', views.atualizar_documento, name='atualizar-documento'),
    path(blake2b(b'consultar_docs').hexdigest()+'/', views.consultar_documento, name='consultar-documento'),
    path('eliminar_documento/<int:id>/', views.eliminar_documento, name='eliminar-documento'),
    path(blake2b(b'emitir_guia_transferencia').hexdigest()+'/<int:id>/', views.emitir_guia_transferencia, name='emitir-guia'),

]
