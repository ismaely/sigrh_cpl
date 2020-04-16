from header.includes import *



@login_required
def area_pessoal_quadro(request):
    fotos = request.session['salakiaku']
    context = {'pessoalQuadro': MENU_PESSOAL_QUADRO, 'fotos': fotos}
    template = TEMPLATE_UTILIZADOR['pq']
    return render(request, template, context)




# editar os dados da nomiação do agente
@login_required
@csrf_protect
def editar_nomiacao(request, id):
    nomiar = Nomiacao_Cargo.objects.get(id=id)
    form = Nomiacao_cargoForm(request.POST or None, instance=nomiar)
    if request.method == 'POST':
        if form.is_valid():
            patente = form.cleaned_data.get('patente')
            id = header.views_core.retorna_numero_bi(form.cleaned_data.get('bi'))
            nomiar = form.save(commit=False)
            nomiar.agente_id = id
            nomiar.save()
            sweetify.success(request, 'Dados alterado com sucesso!....', button='Ok', timer='3200')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))
    pes = Pessoa.objects.get(id=nomiar.agente_id)
    pessoa = PessoaForm(request.POST or None, instance=pes)

    fotos = request.session['salakiaku']
    context = {'form': form, 'nomiar': nomiar, 'form2': pessoa, 'fotos':fotos, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['nomiar']
    return render(request, template, context)




#VIEWS QUE VAI EDITAR OS DADOS DA BAIXA DE UM AGENTE
@login_required
def editarDados_baixas(request, id):
    baixa = Baixa.objects.get(id=id)
    form = BaixaForm(request.POST or None, instance=baixa)
    if request.method == 'POST':
        if form.is_valid():
            baixa = form.save(commit=False)
            baixa.agente_id = header.views_core.retorna_numero_bi(form.cleaned_data.get('bi'))
            baixa.save()
            sweetify.success(request, 'Dados alterado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))
    fotos = request.session['salakiaku']
    pes = Pessoa.objects.get(id=baixa.agente_id)
    pessoa = PessoaForm(request.POST or None, instance=pes)
    context = {'form': form, 'baixa': baixa, 'form2': pessoa, 'fotos':fotos, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['baixa']
    return render(request, template, context)



#VIEWS QUE VAI ALTERAR OS DADOS DA DESPROMOÇÃO
"""@login_required
def atualizar_despromocao(request, id):
    desp = Despromocao.objects.get(id=id)
    form = DespromocaoForm(request.POST or None, instance=desp)
    if request.method == 'POST':
        if form.is_valid():
            agen = header.views_core.retorna_numero_agente(form.cleaned_data.get('bi'))
            desp = form.save(commit=False)
            desp.agente_id = agen
            desp.save()
            dados = {}
            sweetify.success(request, 'Dados Alterado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'), dados)
    pes = Pessoa.objects.get(id=desp.agente_id)
    pessoa = PessoaForm(request.POST or None, instance=pes)
    context = {'form': form, 'pessoa': pessoa, 'valor': desp, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['despromocao']
    return render(request, template, context)"""


@csrf_protect
def atualizar_documento(request, id):
    docs = Documento.objects.get(id=id)
    form = DocumentoForm(request.POST or None, instance=docs)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Dados atualizado com sucesso!....', button='Ok')
            return HttpResponseRedirect(reverse('documentacao:area-documentacao'))
    fotos = request.session['salakiaku']
    dados = {'form': form, 'docs': docs, 'fotos':fotos, 'documentos': MENU_DOCUMENTO}
    template = TEMPLATE_PESSOAQUADRO['docs']
    return render(request, template, dados)



#for key, value in idade.items
@login_required
@csrf_protect
def editar_cadastro(request, id):
    try:
        dados = {}
        pessoa = Pessoa.objects.get(id=id)
        agente = Agente.objects.get(id=id)
        orgao = Orgao.objects.get(id=id)
        form = PessoaForm_atualizar(request.POST or None, instance=pessoa)
        form2 = AgenteForm_atualizar(request.POST or None, instance=agente)
        form3 = OrgaoForm_atualizar(request.POST or None, instance=orgao)
        if request.method == 'POST':
            if form3.is_valid():
                form.save()
                form2.save()
                form3.save()
                sweetify.success(request, 'Dados do agente alterado com sucesso !..', button='Ok', timer='4000')
                return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))

        dados = {'fotos':request.session['salakiaku'],'form': form, 'form2': form2, 'form3': form3, 'pessoa': pessoa, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
        template = TEMPLATE_PESSOAQUADRO['cadastro']
        return render(request, template, dados)
    except ValueError as e:
        print(e)
    dados = {'fotos':request.session['salakiaku'],'form': form, 'form2': form2, 'form3': form3, 'pessoa': pessoa, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['cadastro']
    return render(request, template, dados)




#views que vai atualizar a patente do agennte
@csrf_protect
@login_required
def atualizar_patente(request):
    form = Atualizar_patenteForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                patente = form.cleaned_data.get('patente')
                id = header.views_core.retorna_numero_bi(form.cleaned_data.get('bi'))
                agente = Agente.objects.get(id=id)
                if id > 0 and agente.id is not None:
                    agente.patente = patente
                    agente.categoria = header.views_core.categoria_patente(patente)
                    agente.save()
                    paten = form.save(commit=False)
                    paten.agente_id = agente.id
                    paten.save()
                    sweetify.sweetalert(request, 'Alteração feita com sucesso ...', type="success", button='Ok', timer='3600')
                    return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))
            except Exception as e:
                print(e)
                context = {'form': form}
                messages.warning(request, 'O Nip ou BI do agente não existe no sistema!..')
                template = TEMPLATE_PESSOAQUADRO['atuli_patente']
                return render(request, template, context)

    context = {'form': form, 'pessoalQuadro': MENU_PESSOAL_QUADRO, 'fotos':request.session['salakiaku']}
    template = TEMPLATE_PESSOAQUADRO['atuli_patente']
    return render(request, template, context)





# função que retorna o curso por medio da requisição ajax
@login_required
def retorna_cursos(request):
    if request.method == 'POST':
        dados = dict()
        cod = []
        cod = request.body.decode('utf-8')
        lista = json.loads(cod)
        if lista['area'] == 'Área de Mecânica':
            dados = {
                'dados': Mecanica,
            }
            return JsonResponse(dados)
        elif lista['area'] == 'Área de Electricidade':
            dados = {
                'dados': Electricidade,
            }
            return JsonResponse(dados)
        elif lista['area'] == 'Área de Construção Civil':
            dados = {
                'dados': Construcao_Civil,
            }
            return JsonResponse(dados)
        elif lista['area'] == 'Área de Informática':
            dados = {
                'dados': Informatica,
            }
            return JsonResponse(dados)
        elif lista['area'] == 'Área de Administração':
            dados = {
                'dados': Administracao,
            }
            return JsonResponse(dados)
        elif lista['area'] == 'Área de Administração':
            dados = {
                'dados': Administracao,
            }
            return JsonResponse(dados)
        elif lista['area'] == 'Área de Saude':
            dados = {
                'dados': Saude,
            }
            return JsonResponse(dados)
        elif lista['area'] == 'Ciência Sociais':
            dados = {
                'dados': CIENCIAS_SOCIAIS,
            }
            return JsonResponse(dados)
        elif lista['area'] == 'Saude':
            dados = {
                'dados': SAUDE,
            }
            return JsonResponse(dados)
        elif lista['area'] == 'Direito':
            dados = {
                'dados': DIREITO,
            }
            return JsonResponse(dados)
        elif lista['area'] == 'Economia':
            dados = {
                'dados': ECONOMIA,
            }
            return JsonResponse(dados)
        elif lista['area'] == 'Letras':
            dados = {
                'dados': LETRAS,
            }
            return JsonResponse(dados)
        elif lista['area'] == 'Engenharia':
            dados = {
                'dados': ENGENHARIA,
            }
            return JsonResponse(dados)
        elif lista['area'] == 'Ciência':
            dados = {
                'dados': CIENCIA,
            }
            return JsonResponse(dados)
        else:
            dados = {
                'dados': ['--'],
            }
            return JsonResponse(dados)
        



# retorna o municipos das provincia
@login_required
def retorna_municipio(request):
    if request.method == 'POST':
        dados = dict()
        cod = []
        cod = request.body.decode('utf-8')
        lista = json.loads(cod)
        if lista['provincia'] == 'Luanda':
            dados = {
                'dados': LUANDA,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Bengo':
            dados = {
                'dados': BENGO,
            }
            return JsonResponse(dados)      
        elif lista['provincia'] == 'Benguela':
            dados = {
                'dados': BENGUELA,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Bié':
            dados = {
                'dados': BIE,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Cabinda':
            dados = {
                'dados': CABINDA,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Cabinda':
            dados = {
                'dados': CABINDA,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Cunene':
            dados = {
                'dados': CUNENE,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Huambo':
            dados = {
                'dados': HUAMBO,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Huila':
            dados = {
                'dados': HUILA,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Cuando Cubango':
            dados = {
                'dados': CUANDO_CUBANGO,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Cuanza Norte':
            dados = {
                'dados': CUANZA_NORTE,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Cuanza Sul':
            dados = {
                'dados': CUANZA_SUL,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Lunda Norte':
            dados = {
                'dados': LUNDA_NORTE,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Lunda Sul':
            dados = {
                'dados': LUNDA_SUL,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Malanje':
            dados = {
                'dados': MALANJE,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Moxico':
            dados = {
                'dados': MOXICO,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Namibe':
            dados = {
                'dados': NAMIBE,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Uige':
            dados = {
                'dados': UIGE,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Zaire':
            dados = {
                'dados': ZAIRE,
            }
            return JsonResponse(dados)



#VIEWS QUE VALIDAR O CODIGO DE CADASTRO PARA USARIO SEM PERMISÃO
@login_required
def codigo_cadastrar(request):
    if request.method == 'POST':
        dados = dict()
        cod = request.body.decode('utf-8')
        if header.views_core.validar_codigo_cadastro(cod):
            dados = {
                'validade': True,
                'chave': int( DATA_ANO) + int(DATA_MES),
                'msg': 'Acesso aceite'
            }
            return JsonResponse(dados)
        else:
            dados = {
                'validade': False,
                'msg': 'Acesso Negado!.. sem permisão'
            }
            return JsonResponse(dados)




#views que vai eleiminar processo disciplinar
@csrf_protect
def eliminar_processoDiciplinar(request):
    if request.method == 'POST':
        dados = dict()
        cod = []
        cod = request.body.decode('utf-8')
        lista = json.loads(cod)
        id = lista['id']
        if id > 0:
            docs = Disciplina.objects.filter(id=id).delete()
            dados = {
                    'validade': True,
                }
            return JsonResponse(dados)
        else:
            dados = {
                'validade': False,
            }
            return JsonResponse(dados)



#views que vai eleiminar processo disciplinar
def eliminar_reforma_anticipada(request):
    if request.method == 'POST':
        dados = dict()
        cod = []
        cod = request.body.decode('utf-8')
        lista = json.loads(cod)
        id = lista['id']
        if id > 0:
            docs = Reforma.objects.filter(id=id).delete()
            dados = {
                    'validade': True,
                }
            return JsonResponse(dados)
        else:
            dados = {
                'validade': False,
            }
            return JsonResponse(dados)




#views que vai eliminar nomiação de um agente, (javascript)
@csrf_protect
@login_required
def eliminar_nomiacao(request):
    if request.method == 'POST':
        dados = dict()
        cod = []
        cod = request.body.decode('utf-8')
        lista = json.loads(cod)
        id = lista['id']
        if id > 0:
            docs = Nomiacao_Cargo.objects.filter(id=id).delete()
            dados = {
                    'validade': True,
                    'msg': 'Acesso aceite'
                }
            return JsonResponse(dados)
        else:
            dados = {
                'validade': False,
                'msg': 'Acesso Negado!.. sem permisão'
            }
            return JsonResponse(dados)



# VIEWS QUE VAI REMOVER OS DADOS DA DESPROMOÇÃO APAGA OS DADOS
"""@login_required
def remover_despromocao(request):
    if request.method == 'POST':
        dados = dict()
        cod = []
        cod = request.body.decode('utf-8')
        lista = json.loads(cod)
        codigo = lista['codigo']
        id = lista['id']
        if header.views_core.validar_codigo_eliminar(codigo):
            docs = Despromocao.objects.filter(id=id).delete()
            dados = {
                    'validade': True,
                }
            return JsonResponse(dados)
        else:
            dados = {
                'validade': False,
            }
            return JsonResponse(dados)"""



#views que vai eliminar a baixa dos agentte
@csrf_protect
def eliminar_baixa(request):
    if request.method == 'POST':
        dados = dict()
        cod = []
        cod = request.body.decode('utf-8')
        lista = json.loads(cod)
        id = lista['id']
        if id > 0:
            docs = Baixa.objects.filter(id=id).delete()
            dados = {
                    'validade': True,
                }
            return JsonResponse(dados)
        else:
            dados = {
                'validade': False,
            }
            return JsonResponse(dados)



#view para listar todas nomiação solicitada
@login_required
def listar_nomiacao(request):
    lista =[]
    lista = Nomiacao_Cargo.objects.order_by('id')
    #print(header.views_core.gerar_codigo_cadastro())
    #lista = Orgao.objects.select_related('agente').all().order_by('-id')
    context = {'lista': lista, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['listar_nomiado']
    return render(request, template, context)



#views que vai listarr o tempo na policia , o tempo no cargo, tempo na patente
@login_required
@csrf_protect
def listar_tempo_efetividade(request):
    tempo_cargo = {}
    tempo_policia = {}
    anoPol = []
    ano =[]
    agente = Agente.objects.select_related('pessoa').all()
    lista = Nomiacao_Cargo.objects.select_related('agente').all()
    for tempo in agente:
        anoPol = tempo.data_igresso.split('-')
        if DATA_ANO == int (anoPol[0]):
            tempo_policia[tempo.id] = 'Meses'

        else:
            x_anos = DATA_ANO - int (anoPol[0])
            tempo_policia[tempo.id] = str(x_anos)+ ' ' + 'Anos'
    for temp in lista:
        ano = temp.data.split('-')
        if DATA_ANO == int (ano[0]):
            tempo_cargo[temp.agente_id] = 'Meses'
        else:
            if temp.agente_id is not None:
                x_anos = DATA_ANO - int (ano[0])
                tempo_cargo[temp.agente_id] = str(x_anos )+ ' ' + 'Anos'

    template = TEMPLATE_PESSOAQUADRO['listar_tempo']
    context = {'lista': agente, 'policia':tempo_policia, 'cargo': tempo_cargo, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    return render (request, template, context)





#views que vai listar a despromoção
"""@login_required
def listarDespromocao(request):
    desp = Despromocao.objects.all()
    dados = {'desp': desp, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['listar_desp']
    return render(request, template, dados)"""


@csrf_protect
@login_required
def listar_falecimento(request):
    lista = dict()
    lista = Falecimento.objects.select_related('agente').all().order_by('-id')
    dados = {'lista': lista, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['listar_falecimento']
    return render(request, template, dados)




#views que vai listar a baixas
@csrf_protect
@login_required
def listarBaixas(request):
    baixa = Baixa.objects.all().order_by('-id')
    dados = {'baixa': baixa, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['listar_baixa']
    return render(request, template, dados)



#views que vai listar a informação pessoal
@csrf_protect
@login_required
def informacao_pessoal(request, id=None):
    lista = Orgao.objects.select_related('agente').get(agente_id=id)
    dados = {'lista': lista, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO }
    template = TEMPLATE_PESSOAQUADRO['informacao']
    return render(request, template, dados)



#views que vai visualizar informação do processo disciplinar
@login_required
def informacao_processo_disciplinar(request, id=None):
    lista = []
    processo = []
    try:
        lista = Disciplina.objects.select_related('agente').get(id=id)
        processo = Disciplina.objects.filter(agente_id = lista.agente_id)
    except Exception as e:
        print(e)
    dados = {'lista': lista, 'processo': processo, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO }
    template = TEMPLATE_PESSOAQUADRO['info_processo']
    return render(request, template, dados)




# ONDE ESTA SER LISTADO A REFFORMA E INSERIR OS DADOS NA TABELA DA REFORMA
@csrf_protect
@login_required
def listarReforma(request):
    idade = {}
    dados = []
    try:
        dados = Agente.objects.select_related('pessoa').all()
        #anticipada = Reforma.objects.select_related('agente').filter(reforma='Anticipada').all()
        anticipada = Reforma.objects.filter(reforma='Anticipada').all()
        for k in  dados:
            if header.views_core.retorna_idade(k.pessoa.data_nascimento) > 50:
                ida = header.views_core.retorna_idade(k.pessoa.data_nascimento)
                idade[k.id] = str(ida) + " Anos"
                try:
                    reforma = Reforma.objects.get(agente_id=k.id)
                    if reforma.id is not None:
                        print(" ")
                except Reforma.DoesNotExist:
                    inser = Reforma.objects.create(agente_id=k.id)

        for k in anticipada:
            #ida = header.views_core.retorna_idade(k.agente_id.pessoa_id.data_nascimento)
            idade[k.agente_id] = 'Antecipada'

    except Exception as e:
        print(e)
    context = {'lista': dados, 'idade': idade, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['listar_ref']
    return render(request, template, context)



@login_required
def imprimir_informacao(request):
    pass



#views que vai listar todos agentes
@csrf_protect
@login_required
def listar_todos_agente(request):
    lista =[]
    lista =Orgao.objects.order_by('-agente')
    context = {'lista': lista, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['listar_todo']
    return render(request, template, context)


@csrf_protect
@login_required
def listar_processoDisciplinar(request):
    lista =[]
    lista = Disciplina.objects.order_by('-agente')
    context = {'lista': lista, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['lista_discip']
    return render(request, template, context)



@csrf_protect
@login_required
def listar_documentos(request):
    try:
        lista = []
        lista = documentacao.views.listar_documento()
        dados = {'listar': lista , 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
        template = TEMPLATE_PESSOAQUADRO['listar_docs']
        return render(request, template, dados)

    except Exception as e:
        raise Http404("falha ao listar documento pessoa %s" % (e))




#views que vai p    template = TEMPLATE_PESSOAQUADRO['nomiar']
@csrf_protect
@login_required
def efectuar_Colocacao(request):
    form = OrgaoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                bi_agente = form.cleaned_data.get('bi')
                if len(bi_agente) == 14 and verficar_bi_numero_agente(request):
                    agen = header.views_core.retorna_numero_agente(bi_agente)
                    novo = Orgao.objects.get(agente_id=agen)
                    novo.orgao_colocacao = form.cleaned_data.get('orgao_colocacao')
                    novo.data_colocacao = form.cleaned_data.get('data_colocacao')
                    novo.dispacho = form.cleaned_data.get('dispacho')
                    novo.save()
                else:
                    agen = header.views_core.retorna_numero_agente_id(bi_agente)
                    novo = Orgao.objects.get(agente_id=agen)
                    novo.orgao_colocacao = form.cleaned_data.get('orgao_colocacao')
                    novo.data_colocacao = form.cleaned_data.get('data_colocacao')
                    novo.dispacho = form.cleaned_data.get('dispacho')
                    novo.save()

                sweetify.success(request, 'Colocação efetuada com sucesso!....', button='Ok', timer='3100')
                return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))

            except Exception as e:
                messages.warning(request, 'O Nip ou BI não é valido..')
                context = {'form': form, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
                template = TEMPLATE_PESSOAQUADRO['orgao']
                return render(request, template, context)
    context = {'form': form, 'fotos':request.session['salakiaku'],  'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['orgao']
    return render(request, template, context)




#views que vai fazer a consulta do agente que for solicitada pela função consulta, bi ou numero d agente
@login_required
def consultar_dados(request):
    if request.method == 'POST':
        value = request.POST['busca']
        if value is not None:
            try:
                agente = Agente.objects.get(numero_agente=value)
                if agente.pessoa_id is not None:
                    orgao = Orgao.objects.get(agente_id=agente.id)
                    context = {'agente': agente, 'orgao': orgao, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
                    template = TEMPLATE_PESSOAQUADRO['consultar']
                    return render(request, template, context)
            except Exception as e:
                try:
                    agent = Agente.objects.get(nip=value)
                    if agent.pessoa_id is not None:
                        orgao = Orgao.objects.get(agente_id=agent.id)
                        context = {'agente': agent, 'orgao': orgao, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
                        template = TEMPLATE_PESSOAQUADRO['consultar']
                        return render(request, template, context)
                except Agente.DoesNotExist:
                    messages.warning(request, ' Não existe agente cadastrado com esse numero no sistema...')
                    template = TEMPLATE_PESSOAQUADRO['consultar_rota']
                    return HttpResponseRedirect(reverse(template))
    context = {'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['consultar']
    return render(request, template, context)



@login_required
def consultar_documentos(request):
    try:
        form = ConsultarDocumentoForms(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                lista = Documento.objects.filter(categoria=form.cleaned_data.get('categoria'))
                dados = {'form': form, 'listar': lista, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
                template = TEMPLATE_PESSOAQUADRO['consultar_docs']
                return render(request, template, dados)

    except Documento.DoesNotExist:
        print('erro na consulta de documento')

    dados = {'form': form, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['consultar_docs']
    return render(request, template, dados)



@login_required
@csrf_protect
def consultar_processo_disciplinar(request):
    if request.method == 'POST':
        value = request.POST['busca']
        try:
            process = Disciplina.objects.filter(numero_processo = value)
        except Disciplina.DoesNotExist:
            #sweetify.warning(request, 'Não existe processo com este numero!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))

    dados = {'lista': process, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['lista_discip']
    return render (request, template, dados)




@login_required
def registar_despromocao(request):
    form = DespromocaoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            agen = header.views_core.retorna_numero_agente(form.cleaned_data.get('bi'))
            desp = form.save(commit=False)
            desp.agente_id = agen
            desp.save()
            dados = {}
            sweetify.success(request, 'Dados Registado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'), dados)

    context = {'form': form, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['despromocao']
    return render(request, template, context)



@login_required
@csrf_protect
def registar_baixa(request):
    form = BaixaForm(request.POST or None)
    form2 = FalecimentoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and form2.is_valid() and header.validators.validar_baixa(request):
            try:
                baixa = form.save(commit=False)
                motivo = form.cleaned_data.get('motivo_baixa')
                tipo = form.cleaned_data.get('tipo_invalidez')
                id = header.views_core.retorna_numero_bi(form.cleaned_data.get('bi'))
                baixa.agente_id = id
                if motivo == 'Invalidez' and tipo == '':
                    baixa.tipo_invalidez = 'Parcial'
                baixa.save()
                if motivo == 'Falecimento' and request.POST['cimiteiro'] is not None:
                    falec = form2.save(commit=False)
                    falec.baixa_id = baixa.id
                    falec.agente_id = id
                    falec.save()
                sweetify.success(request, 'Dados Registado com sucesso!....', button='Ok', timer='4000')
                return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))
            except Exception as e:
                messages.warning(request, ' O numero de Agente esta errado')

    context = {'form': form,  'form2': form2, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['baixa']
    return render(request, template, context)



#views que vai registar a nomiação de um agente com nova patente e cargo
@login_required
@csrf_protect
def registar_nomiacao(request):
    form = Nomiacao_cargoForm(request.POST or None)
    if request.method == 'POST':
        resp, valor = verficar_id_nomiacao(request)
        if form.is_valid() and resp:
            #patente = form.cleaned_data.get('patente')
            id = header.views_core.retorna_numero_bi(form.cleaned_data.get('bi'))
            nomiar = form.save(commit=False)
            nomiar.agente_id = id
            nomiar.save()
            sweetify.success(request, 'Agente Nomiado com sucesso!....', button='Ok', timer='3200')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))
        else:
            try:
                if valor.id is not None:
                    valor.cargo = form.cleaned_data.get('cargo')
                    valor.data = form.cleaned_data.get('data')
                    valor.tipo = form.cleaned_data.get('tipo')
                    valor.categoria = form.cleaned_data.get('categoria')
                    valor.dispacho = form.cleaned_data.get('dispacho')
                    valor.descricao = form.cleaned_data.get('descricao')
                    valor.save()
                    sweetify.success(request, 'Agente Nomiado com sucesso!....', button='Ok', timer='3200')
                    return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))
            except Exception as e:
                messages.warning(request, ' Não existe agente com esse numero no sistema...')

    context = {'form': form, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['nomiar']
    return render(request, template, context)



# viwes que vai resistar reforma anticipada, mais primeiro o usario vai ter que digitar o codigo de segurança
@login_required
@csrf_protect
def registar_reforma_anticipada(request):
    form = Reforma_anticipadaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid() and header.validators.validar_reforma_anticipada(request):
            reforma = form.save(commit=False)
            reforma.agente_id = header.views_core.retorna_numero_bi(form.cleaned_data.get('bi'))
            reforma.reforma = "Anticipada"
            reforma.save()
            sweetify.success(request, 'Dados Registado com sucesso!....', button='Ok', timer='4000')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))

    context = {'form': form, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = 'pessoal_quadro/registar_reforma.html'
    return render(request, template, context)



@login_required
@csrf_protect
def registar_processoDisciplinar(request):
    form = DisciplinaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            id = form.cleaned_data.get('bi')
            desc = form.save(commit=False)
            desc.agente_id = id
            desc.save()
            sweetify.success(request, 'Dados registado com sucesso...', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))

    dados = {'form': form, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['disciplina']
    return render(request, template, dados)



@login_required
@csrf_protect
def registar_documentos(request):
    form = DocumentoForm(request.POST or None)
    if request.method == 'POST':   
        if form.is_valid():
            if documentacao.views.registar_documento(request):
                sweetify.success(request, 'Documento Cadastrado com sucesso...', button='Ok')
                return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))

    dados = {'form': form,'fotos':request.session['salakiaku'],  'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['docs']
    return render(request, template, dados)



# VIEWS QUE VAI CADASTRAR OS DADOS DO UTILIZADOR
@login_required
def cadastrar(request):
    form = PessoaForm(request.POST or None)
    form2 = AgenteForm(request.POST or None)
    form3 = OrgaoForm(request.POST or None)
    if request.method == 'POST':
        form2 = AgenteForm(request.POST, request.FILES or None)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            pessoa = form.save()
            agente = form2.save(commit=False)
            agente.pessoa_id = pessoa.id
            agente.categoria = header.views_core.categoria_patente(request.POST.get('patente'))
            agente.save()
            orgao = form3.save(commit=False)
            orgao.agente_id = agente.id
            orgao.save()

            if len(request.POST['foto_civil']) > 0 and len(request.POST['foto_fardado']) > 0:
                um, dois = header.views_core.prepara_foto(request)
                agent = Agente.objects.get(pessoa_id=agente.id)
                agent.foto_civil = um
                agent.foto_fardado = dois
                agent.save()
            else:
                agent = Agente.objects.get(pessoa_id=agente.id)
                agent.foto_civil = "foto/user.jpg"
                agent.foto_fardado = "foto/user.jpg"
                agent.save()

            sweetify.success(request, 'Dados Registado com sucesso do agente!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))

    dados = {'form': form, 'form2': form2, 'form3': form3, 'fotos':request.session['salakiaku'], 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['cadastro']
    return render(request, template, dados)



def cabecarioFicha(id):
    lista = []
    lista = Orgao.objects.select_related('agente').get(agente_id=id)
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    p.setFont('Times-Roman', 12)
    logo = os.path.join(settings.MEDIA_ROOT, str('logo.jpeg'))

    fotofardado = os.path.join(settings.MEDIA_ROOT, str(lista.agente.foto_fardado))
    fotocivil = os.path.join(settings.MEDIA_ROOT, str(lista.agente.foto_civil))

    logo_tabela = os.path.join(settings.MEDIA_ROOT, str('claro.png'))

    style = getSampleStyleSheet()
    estilosB = style["BodyText"]
    #estilosB = style['Heading3']
    estilosB.alignment = TA_LEFT
    estilosB.fontSize = 11
    estilosB.fontName = 'Times-Bold'
    #estilosB.box = 'lightblue'
    estilosB.textColor = 'black'

    # as colunas de cada linha
    nome = Paragraph(''' Nome Completo ''',estilosB)
    pai = Paragraph(''' Nome do Pai ''',estilosB)
    mae = Paragraph(''' Nome da Mãe ''',estilosB)
    genero = Paragraph(''' Género ''',estilosB)
    # segunda linha
    nascimento = Paragraph(''' Data de Nascimento''',estilosB)
    provincia = Paragraph(''' Provincia ''',estilosB)
    estado = Paragraph(''' Estado Civil ''',estilosB)
    bi = Paragraph(''' Bi Nº ''',estilosB)
    #terceira linha
    residencia = Paragraph(''' Residencia ''',estilosB)
    municipio = Paragraph(''' Municipio ''',estilosB)
    telefone = Paragraph(''' Telefone ''',estilosB)
    email = Paragraph(''' E-mail ''',estilosB)

    #quarta linha
    patente = Paragraph(''' Patente ''',estilosB)
    categoria = Paragraph(''' Categoria ''',estilosB)
    nip = Paragraph(''' Nip ''',estilosB)
    ingresso = Paragraph(''' Data de Ingresso ''',estilosB)
    #quinta linha
    academico = Paragraph(''' Nivel Academico ''',estilosB)
    curso = Paragraph(''' Curso ''',estilosB)
    area_formacao = Paragraph(''' Área de Formação ''',estilosB)
    data_colocacao = Paragraph(''' Data de Colocação ''',estilosB)
    #sexto linha
    contribuite = Paragraph(''' Nº Contrbuite ''',estilosB)
    social= Paragraph(''' Nº Caixa social ''',estilosB)
    orgao= Paragraph(''' Orgão de Colocação ''',estilosB)
    numero_agente = Paragraph(''' Nº de Agente ''',estilosB)

    data1 = []
    data2 = []
   
    #Dados pessoal -- primaeira linha
    data1.append([nome, nascimento, provincia])
    dados1 = [str(lista.agente.pessoa.nome).upper(), str (lista.agente.pessoa.data_nascimento).upper(), 
    str (lista.agente.pessoa.provincia).upper()]
    data1.append(dados1)
    #linha do pai
    data1.append([pai, bi, municipio])
    dados1 =[str(lista.agente.pessoa.nome_pai).upper() ,str (lista.agente.pessoa.bi).upper(),
    str (lista.agente.pessoa.municipio).upper()]
    data1.append(dados1)
    #linha da mae
    data1.append([mae, genero, residencia])
    dados1 = [str (lista.agente.pessoa.nome_mae).upper(), str (lista.agente.pessoa.genero).upper(), 
    str (lista.agente.pessoa.residencia).upper()]
    data1.append(dados1)
    # linha do email
    data1.append([email, estado, telefone])
    dados1 = [str (lista.agente.pessoa.email), str (lista.agente.pessoa.estado_civil).upper(), 
    str (lista.agente.pessoa.telefone).upper()]
    data1.append(dados1)

    # dados de agente
    data2.append([patente, categoria, ingresso])
    dados2 = [str (lista.agente.patente).upper(), str (lista.agente.categoria).upper(),
    str (lista.agente.data_igresso)]
    data2.append(dados2)

    # dados agente linha 2
    data2.append([area_formacao, academico, data_colocacao])
    dados2 = [ str (lista.agente.area_formacao).upper(), str (lista.agente.nivel_academico).upper(),
    str (lista.data_colocacao)]
    data2.append(dados2)
    # dados agente linha 3
    data2.append([curso, contribuite, nip])
    dados2 = [str (lista.agente.curso).upper(), str (lista.agente.numero_contribuite).upper(),
    str (lista.agente.nip)]
    data2.append(dados2)

    data2.append([orgao, social, numero_agente])
    dados2 = [str (lista.orgao_colocacao).upper(), str (lista.agente.numero_caixa_social),
    str(lista.agente.numero_agente)]
    data2.append(dados2)

    # tabela 1 dos dao pessoais
    table1 = Table(data1, colWidths=[9 * cm, 4.8 * cm, 5.4 * cm, 1.1 * cm])
    table1.setStyle(TableStyle([
    ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
    ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
    ]))
  
    #dados de agente
    table2 = Table(data2, colWidths=[9 * cm, 6.6 * cm, 3.6 * cm, 1 * cm])
    table2.setStyle(TableStyle([
    ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
    ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
    ]))


    p.saveState()
    policia = os.path.join(settings.MEDIA_ROOT, str("policia.png"))
    p.drawImage(policia, 1.40 * inch,0.65 * inch, width=40, height=40, mask=None)
    #p.line(0, 0.70 * inch,600, 0.70 * inch)
    p.drawString(0.60 *inch, 0.45 * inch,'Comando Províncial de Luanda')

    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2
    )
    data = 'cpl-salakiaku %s' %(lista.agente.nip)
    qr.add_data(data)
    qr.make(fit=True)
    nome =  str(random.random()) + ".png"
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(settings.MEDIA_ROOT+'/codigo_qr/'+nome)
    p.drawImage(settings.MEDIA_ROOT+'/codigo_qr/'+nome, 5.60 * inch,0.65 * inch, width=40, height=40, mask=None)
    p.drawString(4.50 *inch, 0.45 * inch,'Salakiaku / Processado por computador')
    p.restoreState()
    return (buffer, p, logo, fotofardado, fotocivil, logo_tabela, table1, table2, estilosB, style)




#FUNÇÃO QUE VAI GERAR A FICHA PESSOAL
@login_required
def ficha_pessoal(request, id=None):

    try:
        if id > 0 :
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="ficha_pessoal.pdf"'

            buffer, p, logo, fotofardado, fotocivil, logo_tabela, table1, table2, estilosB, style = cabecarioFicha(id)

            #tamanho da linha
            p.setLineWidth(2)

            #logo do centro da angola
            p.drawImage(logo, 253.5, 750, width=65, height=70, mask=None)

            # dados da respublica
            p.drawString(218,737,'REPÚBLICA DE ANGOLA')
            p.drawString(212.6,723,'MINISTÉRIO DO INTERIOR')
            p.drawString(231.6,709,'POLICIA NACIONAL')
            p.drawString(179,695,'COMANDO PROVÍNCIAL DE LUANDA')
            p.drawString(142,681,'DIRECÇÃO PROVÍNCIAL DE RECURSOS HUMANOS')
            p.line(100,670,500,670)

            #foto civil a primeira
            p.drawImage(fotocivil, 100, 605, width=60, height=60, mask=None)
            # logo da fotofardado
            p.drawImage(fotofardado, 440, 605, width=60, height=60, mask=None)

            # zona do comunicado o informação que deve ser descrita 
            p.drawString(240,620,'Ficha Pessoal do Agente')

            #imagem para os dados pessoal
            p.drawImage(logo_tabela, 24.5, 560.3, width=544.6, height=40, mask=None)
            p.drawString(30,580,'DADOS PESSOAL')

            #imagem para os dados de agente
            p.drawImage(logo_tabela, 24.5, 390.5, width=544.6, height=35, mask=None)
            p.drawString(30,410.5,'DADOS DE AGENTE')
            #criando dados para o processo disciplinar

            width, height = A4
            #0nde começa a ser construida a tabela dos dados pessoais
            # primeira tabela
            table1.wrapOn(p, width, height)
            table1.drawOn(p, 25, 428.3)

            #onde começa se construida a tabela de dados de agente
            #segunda  tabela dados agente
            table2.wrapOn(p, width, height)
            table2.drawOn(p, 25, 261)
           
            p.showPage()
            p.save()
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response
        else:

            print("erro--")
    except Exception as e:
        raise e

    context = {'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_UTILIZADOR['pq']
    return render(request, template, context)



#Ficha para o processo disciplinar
@login_required
def ficha_processo_disciplinar(request, id=None):

    try:
        if id > 0 :

            disciplina = Disciplina.objects.select_related('agente').get(agente_id=id)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="processo_disciplinar.pdf"'

            buffer, p, logo, fotofardado, fotocivil, logo_tabela, table1, table2, estilosB, style = cabecarioFicha(id)

            #tamanho da linha
            p.setLineWidth(2)

            #logo do centro da angola
            p.drawImage(logo, 253.5, 750, width=65, height=70, mask=None)

            # dados da respublica
            p.drawString(218,737,'REPÚBLICA DE ANGOLA')
            p.drawString(212.6,723,'MINISTÉRIO DO INTERIOR')
            p.drawString(231.6,709,'POLICIA NACIONAL')
            p.drawString(179,695,'COMANDO PROVÍNCIAL DE LUANDA')
            p.drawString(142,681,'DIRECÇÃO PROVÍNCIAL DE RECURSOS HUMANOS')
            p.line(100,670,500,670)

            #foto civil a primeira
            p.drawImage(fotocivil, 100, 605, width=60, height=60, mask=None)
            # logo da fotofardado
            p.drawImage(fotofardado, 440, 605, width=60, height=60, mask=None)

            # zona do comunicado o informação que deve ser descrita 
            p.drawString(216.9,620,'Informação do Processo Disciplinar')

            #imagem para os dados pessoal
            p.drawImage(logo_tabela, 24.5, 560.3, width=544.6, height=40, mask=None)
            p.drawString(30,580,'DADOS PESSOAL')

            #imagem para os dados de agente
            p.drawImage(logo_tabela, 24.5, 390.5, width=544.6, height=35, mask=None)
            p.drawString(30,410.5,'DADOS DE AGENTE')
            #criando dados para o processo disciplinar
            #imagem para dados disciplinar
            p.drawImage(logo_tabela, 24.5, 223.3, width=544.6, height=35, mask=None)
            p.drawString(30,237.7,'PROCESSO DISCIPLINAR')

            #0nde começa a ser construida a tabela
            processo = Paragraph(''' Processo Nº''',estilosB)
            data_disc = Paragraph(''' Data ''',estilosB)
            motivo = Paragraph(''' Motivo ''',estilosB)
            dispacho = Paragraph(''' Despacho ''',estilosB)
            pena = Paragraph(''' Resultado ( Pena ) ''',estilosB)
            descricao = Paragraph(''' Descrição ''',estilosB)

            discip1 = []
            
            discip1.append([processo, data_disc, dispacho])
            disciplinar = [str (disciplina.numero_processo), str (disciplina.data),
            str (disciplina.dispacho)]
            discip1.append(disciplinar)
            
            discip1.append([pena, motivo])
            disciplinar = [str (disciplina.pena).upper(), str (disciplina.motivo).upper()]
            discip1.append(disciplinar)

            width, height = A4
            #0nde começa a ser construida a tabela dos dados pessoais
            # primeira tabela
            table1.wrapOn(p, width, height)
            table1.drawOn(p, 25, 428.3)

            #onde começa se construida a tabela de dados de agente
            #segunda  tabela dados agente
            table2.wrapOn(p, width, height)
            table2.drawOn(p, 25, 261)
           
            # tabela de dados da disciplina
            table = Table(discip1, colWidths=[9 * cm, 6.8 * cm, 3.4 * cm, 1.1 * cm])
            table.setStyle(TableStyle([
            ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
            ]))
            table.wrapOn(p, width, height)
            table.drawOn(p, 25, 157.8)

            estilo = style["Normal"]
            style.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            corpo = Paragraph('''<bold><font size=12> OBS: ''' + str(disciplina.descricao) + '''</font></bold>''', estilo)
            #p.drawString(30,210.5,'Este é um widget de texto. O Widget de texto permite que você adicione texto ou HTML a qualquer barra lateral em seu tema. Você pode usar um widget de texto para exibir texto, links, imagens, HTML ou uma combinação desses elementos. Edite ')

            aw = 25
            ah = 140
            w, h = corpo.wrap(518, height)
            corpo.drawOn(p, aw, ah)

            p.showPage()
            p.save()
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response
        else:

            print("erro--")

    except Exception as e:
        raise e

    context = {'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_UTILIZADOR['pq']
    return render(request, template, context)
