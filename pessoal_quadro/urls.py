from django.urls import path
from . import views
from hashlib import blake2b

app_name = 'pessoal_quadro'
urlpatterns = [
    path(blake2b(b'cadastrar').hexdigest()+'/', views.cadastrar, name='cadastrar'),
    path(blake2b(b'area_pessoal_quadro').hexdigest()+'/', views.area_pessoal_quadro, name='area-pessoal-quadro'),
    path(blake2b(b'consultar_dados').hexdigest()+'/', views.consultar_dados, name='consultar-dados'),
    path(blake2b(b'imprimir_informacao').hexdigest()+'/', views.imprimir_informacao, name='imprimir-informacao'),
    path(blake2b(b'listar_todos_agente').hexdigest()+'/', views.listar_todos_agente, name='listar-todos'),
    path(blake2b(b'registar_baixa').hexdigest()+'/', views.registar_baixa, name='registar-baixa'),
    path(blake2b(b'listar_baixas').hexdigest()+'/', views.listarBaixas, name='listar-baixas'),
    path(blake2b(b'registar_despromocao').hexdigest()+'/', views.registar_despromocao, name='registar-despromocao'),
    #path('listar_despromocao/', views.listarDespromocao, name='listar-despromocao'),
    path(blake2b(b'listar_reforma').hexdigest()+'/', views.listarReforma, name='listar-reforma'),
    path(blake2b(b'listar_nomiacao').hexdigest()+'/', views.listar_nomiacao, name='listar-nomiacao'),
    path(blake2b(b'listar_tempo_efetividade').hexdigest()+'/', views.listar_tempo_efetividade, name='listar-efetividade'),
    path(blake2b(b'editar_cadastro').hexdigest()+'/<int:id>/', views.editar_cadastro, name='editar-cadastro'),
    path(blake2b(b'informacao_pessoal').hexdigest()+'/<int:id>/', views.informacao_pessoal, name='informacao-pessoal'),
    path(blake2b(b'editarDados_baixas').hexdigest()+'/<int:id>/', views.editarDados_baixas, name='editar-baixas'),
    #path('atualizar_despromocao/<int:id>/', views.atualizar_despromocao, name='atualizar-despromocao'),
    #path('editar_feria/<int:id>/', views.editar_ferias, name='editar-feria'),
    path(blake2b(b'editar_dados_nomiacao').hexdigest()+'/<int:id>/', views.editar_nomiacao, name='editar-dados-nomiacao'),
    #path('remover_despromocao/', views.remover_despromocao, name='remover-despromocao'),
    path(blake2b(b'eliminar_nomiacao').hexdigest()+'/', views.eliminar_nomiacao, name='eliminar-nomiacao'),
    path(blake2b(b'eliminar_baixa').hexdigest()+'/', views.eliminar_baixa, name='eliminar-baixa'),
    path(blake2b(b'efectuar_colocacao').hexdigest()+'/', views.efectuar_Colocacao, name='efectuar-colocacao'),
    path(blake2b(b'registar_nomiacao').hexdigest()+'/', views.registar_nomiacao, name='registar-nomiacao'),
    path(blake2b(b'registar_reforma').hexdigest()+'/', views.registar_reforma_anticipada, name='registar-reforma'),
    path(blake2b(b'atualizar_patente').hexdigest()+'/', views.atualizar_patente, name='atualizar-patente'),
    #path('gerar-codigo/', views.gerar_codigo_seguranca, name='gerar-codigo'),
    path(blake2b(b'codigo_cadastrar').hexdigest()+'/', views.codigo_cadastrar, name='codigo-cadastrar'),
    #path('codigo_validar_despromocao/', views.codigo_validar_despromocao, name='codigo-validar-despromocao'),
    path(blake2b(b'ficha_pessoal').hexdigest()+'/<int:id>/', views.ficha_pessoal, name='ficha-pessoal'),
    path(blake2b(b'registar_documento').hexdigest()+'/', views.registar_documentos, name='documento'),
    path(blake2b(b'registar_Processo_displinar').hexdigest()+'/', views.registar_processoDisciplinar, name='Processo-displinar'),
    path(blake2b(b'listar_documentos').hexdigest()+'/',  views.listar_documentos, name='listar-docs'),
    path(blake2b(b'consultar_docs').hexdigest()+'/',  views.consultar_documentos, name='consultar-docs'),
    path(blake2b(b'listar_disciplina').hexdigest()+'/', views.listar_processoDisciplinar, name='listar-disciplina'),
    path(blake2b(b'processo_disciplinar_informacao').hexdigest()+'/<int:id>/', views.informacao_processo_disciplinar, name='pessoal-informacao'),
    path('eliminar_processo_disciplinar/', views.eliminar_processoDiciplinar, name='eliminar-processo'),
    path(blake2b(b'consultar_processo_disciplinar').hexdigest()+'/', views.consultar_processo_disciplinar, name='consultar-processo'),
    path('eliminar_reforma_anticipada/', views.eliminar_reforma_anticipada, name='eliminar-reforma'),
    path(blake2b(b'ficha_processo_disciplinar').hexdigest()+'/<int:id>/', views.ficha_processo_disciplinar, name='ficha-processo'),
    path('retorna_cursos/', views.retorna_cursos, name='retorna-cursos'),
    path('retorna_municipio/', views.retorna_municipio, name='retorna-municipio'),
    path(blake2b(b'listar_falecimento').hexdigest()+'/', views.listar_falecimento, name='listar-falecidos'),
    #path('consultar_dados_atualizar/', views.consultar_dados_atualizar, name='consultar-atualizar'),
]