
""" A que é onde consta todos template para o pessoal_quadro  """
TEMPLATE_PESSOAQUADRO = {
    'cadastro': 'pessoal_quadro/cadastro.html',
    'informacao': 'pessoal_quadro/informacao_pessoal.html',
    'cadastro_rota': 'pessoal_quadro:cadastrar',
    'imprimir': 'pessoal_quadro/imprimir.html',
    'listar_todo': 'pessoal_quadro/listar_todos_agente.html',
    'baixa': 'pessoal_quadro/registar_baixa.html',
    'baixa_rota': 'pessoal_quadro:registar-baixa',
    'listar_baixa': 'pessoal_quadro/listarBaixa.html',
    'despromocao': 'pessoal_quadro/registar_despromocao.html',
    'listar_desp': 'pessoal_quadro/listar_despromocao.html',
    'desp_rota': 'pessoal_quadro:listar-despromocao',
    'listar_ref': 'pessoal_quadro/listar_reforma.html',
    'consultar': 'pessoal_quadro/consultar_dados.html',
    'consultar_rota': 'pessoal_quadro:consultar-dados',
    'feria': 'pessoal_quadro/registar_ferias.html',
    'listar_feria': 'pessoal_quadro/listar_ferias.html',
    'orgao': 'pessoal_quadro/efectuar_colocacao.html',
    'nomiar': 'pessoal_quadro/registar_nomiacao.html',
    'listar_nomiado': 'pessoal_quadro/listar_nomiados.html',
    'codigo': 'pessoal_quadro/gerar_codigo.html',
    'atuli_patente': 'pessoal_quadro/atualizar_patente.html',
    'reforma': 'pessoal_quadro/registar_reforma.html',
    'listar_tempo': 'pessoal_quadro/listar_tempo.html',
    'consul_atual': 'pessoal_quadro/consultar_atualizar.html',
    'docs': 'pessoal_quadro/registar_documento.html',
    'listar_docs': 'pessoal_quadro/listar_documento.html',
    'consultar_docs': 'pessoal_quadro/consultar_docs.html', 
    'disciplina': 'pessoal_quadro/registar_disciplina.html', 
    'lista_discip': 'pessoal_quadro/listar_disciplina.html',
    'info_processo': 'pessoal_quadro/informacao_processoDisciplinar.html',
    'listar_falecimento': 'pessoal_quadro/listar_falecimento.html',
}

""" Rotas e templeate do modulo utilizador """
TEMPLATE_UTILIZADOR = {
    'home': 'utilizador/home.html',
    'login': 'utilizador/login.html',
    'utilizador': 'utilizador/adicionar_utilizador.html',
    'login_rota': '/utilizador/login/',
    'perfil_rota': 'utilizador:sigr_policia',
    'areas': 'utilizador:areas-servico',
    'areas_servico': 'utilizador/areas_servico.html',
    'utilizador_perfil': 'utilizador/utilizador_perfil.html',
    'pq': 'header/pessoal_quadro.html',
    'fm': 'header/formacao.html',
    'doc': 'header/documentacao.html',
    'tras': 'header/transferencia.html',
    'estat': 'header/estatistica.html',
    'sucesso': 'utilizador/sucesso_conta.html',
    'listar': 'utilizador/listar_utilizador.html',
    'troca_padrao': 'utilizador/troca_senhaPadrao.html',
    'mensagem': 'header/mensagem.html',
    'senha_utilizador': 'utilizador/alterar_senha_utilizador.html',
}

""" Rotas e templeate do modulo documento """
TEMPLATE_DOCUMENTO = {
    'registar': 'documentacao/registar_documento.html',
    'consultar': 'documentacao/consultar.html',
    'listar': 'documentacao/listar_documento.html',
    'listar_rota': 'documentacao:listar-documento',
    'testa': 'documentacao/testar.html',
}

""" Rotas e templeate do modulo Formação  """
TEMPLATE_FORMACAO = {
    'adicionar': 'formacao/adicionar_pessoal_formacao.html',
    'selecionar': 'formacao/listar_agente_selecionado.html',
    'conclusao': 'formacao/conclusao_formacao.html',
    'consultar': 'formacao/consultar_formacao.html',
    'listar_agente': 'formacao/listar_agente_formacao.html',
    'listar_terminam': 'formacao/listar_terminaram_formacao.html',
    'selecionar_rota': 'formacao:listar-selecionados',
    'consultar_rota': 'formacao:consultar-formacao',
    'listar_terminam_rota': 'formacao:listar-todos',
    'informacao': 'formacao/informacao_conclusao.html',
    'busca_sele': 'formacao/buscar_selecionado.html',
    'busca_conclu': 'formacao/buscar_conclusao.html',
    'docs': 'formacao/registar_documento.html',
    'consultar_doc': 'formacao/consultar_docs.html',
    'listar_docs': 'formacao/listar_documento.html',
}

""" Rotas e templeate do modulo orgão """
TEMPLATE_ORGAO = {
    'adicionar': "orgao/adicionar_novo_orgao.html"
}

""" Rotas e templeate do modulo transferencia """
TEMPLATE_TRANSFERENCIA = {
    'transferencia': 'transferencia/adicionar_transferencia.html',
    'listar_pedido': 'transferencia/listar_pedido_transferencia.html',
    'listar_troca': 'transferencia/listar_troca.html',
    'consultar': 'transferencia/consulta.html',
    'consultar_doc': 'transferencia/consultar_docs.html',
    'troca': 'transferencia/adicionar_troca.html', 
    'transferido': 'transferencia/listar_pessoal_transferido.html',
    'docs': 'transferencia/registar_documento.html',
    'listar_docs': 'transferencia/listar_documento.html',
    'mensagem': 'transferencia/mensagem.html',
}


TEMPLATE_ESTATISTICA = {
    'estat_transfer': "estatistica/estatistica_transferencia.html",
    'menu': "estatistica/menu2.html",
    'normal': "estatistica/normal_pdf.html",
    'academico': "estatistica/nivel_academico_pdf.html",
    'reforma': "estatistica/reforma_pdf.html",
    'baixa': "estatistica/baixa_pdf.html",
    'disciplina': "estatistica/disciplina_pdf.html",
    'formacao': "estatistica/formacao_pdf.html",
    'estat_reforma': "estatistica/estat_reforma.html",
    'estat_transf': "estatistica/estat_transferencia.html",
    'estat_baixa': "estatistica/estat_baixas.html",
    'selecionado': "estatistica/estat_selecionado.html",
    'conclusao': "estatistica/estat_conclusao.html",
}
