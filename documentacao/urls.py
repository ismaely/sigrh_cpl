from django.urls import path
from . import views

app_name = 'documentacao'
urlpatterns = [
    path('registar_documento/', views.registar_documento, name='registar'),
    path('area_documentacao/', views.area_documentacao, name='area-documentacao'),
    path('consultar/', views.consultar_documento, name='consultar-documento'),
    path('listar_documento/', views.listar_documento, name='listar-documento'),
    path('eliminar_documento/', views.eliminar_documento, name='eliminar-documento'),
    path('atualizar_documento/<int:id>/', views.atualizar_documento, name='atualizar-documento'),
    path('testar/', views.foto_js, name='testar'),

]
