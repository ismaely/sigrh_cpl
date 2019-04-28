from header.includes import *



@login_required
def area_pessoal_quadro(request):
    
    context = {'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_UTILIZADOR['pq']
    return render(request, template, context)


#views que vai gerar ou seja listar  o codigo de segurança
"""@login_required
def gerar_codigo_seguranca(request):
    try:
        codigo = Codigo.objects.first()
        if codigo is None:
            header.views_core.inserir_codigo()
            dados = {'codigo': codigo }
            template = TEMPLATE_PESSOAQUADRO['codigo']
            return render(request, template, dados)
        else:
            datas = codigo.data.split('-')
            if  int(DATE_FORMAT.day) > int(datas[2]) or int(DATE_FORMAT.month) != int(datas[1]):
                if  header.views_core.novo_codigo_seguranca():
                    codigo = Codigo.objects.first()

    except Codigo.DoesNotExist:
        return 0
    context = {'codigo': codigo, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['codigo']
    return render(request, template, context)"""



#view que vai atualizar o codigo de segurança
@login_required
def atualizar_novo_codigo_seguranca(request):
    if  header.views_core.novo_codigo_seguranca():
        return HttpResponseRedirect(reverse('pessoal_quadro:gerar-codigo'))




# editar os dados da nomiação do agente
@login_required
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
    context = {'form': form, 'nomiar': nomiar, 'form2': pessoa, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['nomiar']
    return render(request, template, context)



#views que vai editar os dados da ferias
@login_required
def editar_ferias(request, id):
    ferias = Feria.objects.get(id=id)
    form = FeriaForm(request.POST or None, instance=ferias)
    if request.method == 'POST':
        if form.is_valid():
            feria = form.save(commit=False)
            feria.agente_id = header.views_core.retorna_numero_agente_id(form.cleaned_data.get('numero_agente'))
            feria.save()
            sweetify.success(request, 'Dados alterado com sucesso....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))

    agente = Agente.objects.get(id=ferias.agente_id)
    forms = AgenteForm(request.POST or None, instance=agente)
    context = {'form': form, 'feria': ferias, 'form2': forms, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['feria']
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

    pes = Pessoa.objects.get(id=baixa.agente_id)
    print(form.errors)
    pessoa = PessoaForm(request.POST or None, instance=pes)
    context = {'form': form, 'baixa': baixa, 'form2': pessoa, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
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



def atualizar_documento(request, id):
    docs = Documento.objects.get(id=id)
    form = DocumentoForm(request.POST or None, instance=docs) 
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Dados atualizado com sucesso!....', button='Ok')
            return HttpResponseRedirect(reverse('documentacao:area-documentacao'))

    dados = {'form': form, 'docs': docs, 'documentos': MENU_DOCUMENTO}
    template = TEMPLATE_PESSOAQUADRO['docs']
    return render(request, template, dados)



#for key, value in idade.items
@login_required
def editar_cadastro(request, id):
    try:
        dados = {}
        pessoa = Pessoa.objects.get(id=id)
        agente = Agente.objects.get(id=id)
        orgao = Orgao.objects.get(id=id)
        form = PessoaForm_atualizar(request.POST or None, instance=pessoa)
        form2 = AgenteForm_atualizar(request.POST or None, instance=agente)
        form3 = OrgaoForm_atualizar(request.POST or None, instance=orgao)
        if form3.is_valid():
            form.save()
            form2.save()
            form3.save()
            sweetify.success(request, 'Dados do agente alterado com sucesso !..', button='Ok', timer='4000')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))

        dados = {'form': form, 'form2': form2, 'form3': form3, 'pessoa': pessoa, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
        template = TEMPLATE_PESSOAQUADRO['cadastro']
        return render(request, template, dados)
    except ValueError as e:
        print(e)
    dados = {'form': form, 'form2': form2, 'form3': form3, 'pessoa': pessoa, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['cadastro']
    return render(request, template, dados)




#views que vai atualizar a patente do agennte
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

    context = {'form': form, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['atuli_patente']
    return render(request, template, context)




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



#VIEWS QUE VALIDAR O CODIGO DE ATUALIZAR QDO SE PRETENDE ATUALIZAR PATENTE
@login_required
def codigo_atualizar_recebe(request):
    if request.method == 'POST':
        dados = dict()
        cod = request.body.decode('utf-8')
        if header.views_core.validar_codigo_atualizar(cod):
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



#VIEWS QUE VALIDAR O CODIGO PARA FAZER ALTERAÇÃO DO AGENTE DESPROMOVIDO
"""@login_required
def codigo_validar_despromocao(request):
    if request.method == 'POST':
        dados = dict()
        cod =[]
        cod = request.body.decode('utf-8')
        lista = json.loads(cod)
        codigo = lista['codigo']
        ids = lista['id']
        print(codigo)
        if header.views_core.validar_codigo_atualizar(codigo):
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
"""


#views que vai eleiminar processo disciplinar
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




#views que vai eliminar nomiação de um agente, (javascript)
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
    context = {'lista': lista, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['listar_nomiado']
    return render(request, template, context)



#views que vai listarr o tempo na policia , o tempo no cargo, tempo na patente
@login_required
def listar_tempo_efetividade(request):
    tempo_cargo = {}
    tempo_policia = {}
    anoPol = []
    ano =[]
    agente = Agente.objects.select_related('pessoa').all()
    lista = Nomiacao_Cargo.objects.select_related('agente').all()
    for tempo in agente:
        anoPol = tempo.data_igresso.split('/')
        if DATA_ANO == int (anoPol[2]):
            tempo_policia[tempo.id] = 'Meses'
            
        else:
            x = DATA_ANO - int (anoPol[2])
            tempo_policia[tempo.id] = str(x )+ ' ' + 'Anos'

    for temp in lista:
        ano = temp.data.split('/')
        if DATA_ANO == int (ano[2]):
            tempo_cargo[temp.agente_id] = 'Meses'
            
        else:
            if temp.agente_id is not None:
                x = DATA_ANO - int (ano[2])
                tempo_cargo[temp.agente_id] = str(x )+ ' ' + 'Anos'
        

    template = TEMPLATE_PESSOAQUADRO['listar_tempo']
    context = {'lista': agente, 'policia':tempo_policia, 'cargo': tempo_cargo, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    return render (request, template, context)





#views que vai listar a despromoção
"""@login_required
def listarDespromocao(request):
    desp = Despromocao.objects.all()
    dados = {'desp': desp, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['listar_desp']
    return render(request, template, dados)"""



#views que vai listar a baixas
@login_required
def listarBaixas(request):
    baixa = Baixa.objects.all().order_by('-id')
    dados = {'baixa': baixa, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['listar_baixa']
    return render(request, template, dados)



#views que vai listar a informação pessoal
@login_required
def informacao_pessoal(request, id=None):
    lista = Orgao.objects.select_related('agente').get(agente_id=id)
    dados = {'lista': lista, 'pessoalQuadro': MENU_PESSOAL_QUADRO }
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
    dados = {'lista': lista, 'processo': processo, 'pessoalQuadro': MENU_PESSOAL_QUADRO }
    template = TEMPLATE_PESSOAQUADRO['info_processo']
    return render(request, template, dados)




# ONDE ESTA SER LISTADO A REFFORMA E INSERIR OS DADOS NA TABELA DA REFORMA
@login_required
def listarReforma(request):
    idade = {}
    dados = []
    try:
        dados = Agente.objects.select_related('pessoa').all()
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
        
        for p, k in enumerate(anticipada, 1):
            idade[k.agente_id] = 'Anticipada'
            
        
    except Exception as e:
        print(e)
    context = {'lista': dados, 'idade': idade, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['listar_ref']
    return render(request, template, context)



@login_required
def imprimir_informacao(request):
    pass



#views que vai listar todos agentes
@login_required
def listar_todos_agente(request):
    lista =[]
    lista =Orgao.objects.order_by('-agente')
    context = {'lista': lista, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['listar_todo']
    return render(request, template, context)



@login_required
def listar_processoDisciplinar(request):
    lista =[]
    lista = Disciplina.objects.order_by('-agente')
    context = {'lista': lista, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['lista_discip']
    return render(request, template, context)




@login_required
def listar_documentos(request):
    try:
        lista = []
        lista = documentacao.views.listar_documento()
        dados = {'listar': lista , 'pessoalQuadro': MENU_PESSOAL_QUADRO}
        template = TEMPLATE_PESSOAQUADRO['listar_docs']
        return render(request, template, dados)

    except Exception as e:
        raise Http404("falha ao listar documento pessoa %s" % (e))




#views que vai pode registar a colocação do agente
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
                    #orgao = form.save(commit=False)
                    #orgao.agente_id = agen
                    #orgao.bi_id = form.cleaned_data.get('bi_id')
                    #orgao.numero_agente_id = form.cleaned_data.get('numero_agente_id')

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


    context = {'form': form, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
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
                    context = {'agente': agente, 'orgao': orgao, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
                    template = TEMPLATE_PESSOAQUADRO['consultar']
                    return render(request, template, context)
            except Exception as e:
                try:
                    agent = Agente.objects.get(nip=value)
                    if agent.pessoa_id is not None:
                        orgao = Orgao.objects.get(agente_id=agent.id)
                        context = {'agente': agent, 'orgao': orgao, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
                        template = TEMPLATE_PESSOAQUADRO['consultar']
                        return render(request, template, context)
                except Agente.DoesNotExist:
                    messages.warning(request, ' Não existe agente cadastrado com esse numero no sistema...')
                    template = TEMPLATE_PESSOAQUADRO['consultar_rota']
                    return HttpResponseRedirect(reverse(template))
    context = {'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['consultar']
    return render(request, template, context)



@login_required
def consultar_documentos(request):
    try:
        form = ConsultarDocumentoForms(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                lista = Documento.objects.filter(categoria=form.cleaned_data.get('categoria'))
                dados = {'form': form, 'listar': lista, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
                template = TEMPLATE_PESSOAQUADRO['consultar_docs']
                return render(request, template, dados)

    except Documento.DoesNotExist:
        print('erro na consulta de documento')

    dados = {'form': form, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['consultar_docs']
    return render(request, template, dados)



@login_required
def consultar_processo_disciplinar(request):
    if request.method == 'POST':
        value = request.POST['busca']
        try:
            process = Disciplina.objects.filter(numero_processo = value)
        except Disciplina.DoesNotExist:
            #sweetify.warning(request, 'Não existe processo com este numero!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))
   
    dados = {'lista': process, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
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

    context = {'form': form, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['despromocao']
    return render(request, template, context)



@login_required
def registar_baixa(request):
    form = BaixaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            baixa = form.save(commit=False)
            motivo = form.cleaned_data.get('motivo_baixa')
            tipo = form.cleaned_data.get('tipo_invalidez')
            baixa.agente_id = header.views_core.retorna_numero_bi(form.cleaned_data.get('bi'))
            if motivo == 'Invalidez' and tipo == '':
                baixa.tipo_invalidez = 'Parcial'
            baixa.save()
            sweetify.success(request, 'Dados Registado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))

    context = {'form': form, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['baixa']
    return render(request, template, context)



#views que vai registar a nomiação de um agente com nova patente e cargo
@login_required
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
            
    context = {'form': form, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['nomiar']
    return render(request, template, context)



# viwes que vai resistar reforma anticipada, mais primeiro o usario vai ter que digitar o codigo de segurança
@login_required
def registar_reforma_anticipada(request):
    form = Reforma_anticipadaForm(request.POST or None)
  
    if request.method == 'POST':
        if form.is_valid():
            reforma = form.save(commit=False)
            reforma.agente_id = header.views_core.retorna_numero_bi(form.cleaned_data.get('bi'))
            reforma.reforma = "Anticipada"
            reforma.save()
            sweetify.success(request, 'Dados Registado com sucesso!....', button='Ok', timer='4000')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))
    
    context = {'form': form, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['reforma']
    return render(request, template, context)
    


@login_required
def registar_processoDisciplinar(request):
    form = DisciplinaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            id = header.views_core.retorna_numero_bi(form.cleaned_data.get('bi'))
            desc = form.save(commit=False)
            desc.agente_id = id
            desc.save()
            sweetify.success(request, 'Dados registado com sucesso...', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))

    dados = {'form': form, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['disciplina']
    return render(request, template, dados)



@login_required
def registar_documentos(request):
    form = DocumentoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            if documentacao.views.registar_documento(request):
                sweetify.success(request, 'Documento Cadastrado com sucesso...', button='Ok')
                return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))

    dados = {'form': form, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['docs']
    return render(request, template, dados)



#VIEWS QUE VAI CADASTRAR OS DADOS DO UTILIZADOR
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
            if request.POST['foto_civil'] is not None and request.POST['foto_fardado'] is not None:
                um, dois = header.views_core.prepara_foto(request)
                agent = Agente.objects.get(pessoa_id=agente.id)
                agent.foto_civil = um
                agent.foto_fardado = dois
                agent.save()
            sweetify.success(request, 'Dados Registado com sucesso do agente!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('pessoal_quadro:area-pessoal-quadro'))

    #print(form.cleaned_data)
    #print(form.errors)
    #print(form2.errors)
    #print(form3.errors)
    dados = {'form': form, 'form2': form2, 'form3': form3, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = TEMPLATE_PESSOAQUADRO['cadastro']
    return render(request, template, dados)



def cabecario_ficha(id):
    lista = []
    lista = Orgao.objects.select_related('agente').get(agente_id=id)
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    p.setFont('Times-Roman', 12)

    logo = os.path.join(settings.MEDIA_ROOT, str('logo.jpeg'))

    if lista.agente.foto_fardado != '':
        
        fotofardado = os.path.join(settings.MEDIA_ROOT, str(lista.agente.foto_fardado))
    else:
        fotofardado = os.path.join(settings.MEDIA_ROOT, str('user.jpg'))
        

    logo_tabela = os.path.join(settings.MEDIA_ROOT, str('claro.png'))

    style = getSampleStyleSheet()
    estilosB = style["Normal"]
    estilosB.alignment = TA_CENTER
    estilosB.fontSize = 11
    estilosB.fontName = 'Times-Roman'

    # as colunas de cada linha
    nome = Paragraph(''' Nome Completo ''',estilosB)
    pai = Paragraph(''' Nome do Pai ''',estilosB)
    mae = Paragraph(''' Nome da Mãe ''',estilosB)
    genero = Paragraph(''' Genero ''',estilosB)
    # segunda linha
    nascimento = Paragraph(''' Data de Nascimento''',estilosB)
    provincia = Paragraph(''' Provincia ''',estilosB)
    estado = Paragraph(''' Estado Civil ''',estilosB)
    bi = Paragraph(''' Bi Nº ''',estilosB)
    #terceira linha 
    residencia = Paragraph(''' Residencia ''',estilosB)
    casa = Paragraph(''' Casa Nª ''',estilosB)
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
    funcao = Paragraph(''' Função ''',estilosB)
    data_colocacao = Paragraph(''' Data de Colocação ''',estilosB)
    #sexto linha
    contribuite = Paragraph(''' Contrbuite Nº ''',estilosB)
    social= Paragraph(''' Caixa social Nº ''',estilosB)
    orgao= Paragraph(''' Orgão de Colocação ''',estilosB)
    

    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []
    data1.append([nome, pai, mae, genero])
    data2.append([nascimento, provincia, estado, bi])
    data3.append([residencia, casa, telefone, email])
    data4.append([patente, categoria, nip, ingresso])
    data5.append([academico, curso, funcao, data_colocacao])
    data6.append([contribuite, social, orgao])

    dados1 = []
    dados2 = []
    dados3 = []
    dados4 = []
    dados5 = []
    dados6 = []

    dados1 = [str (lista.agente.pessoa.nome), str (lista.agente.pessoa.nome_pai), 
    str (lista.agente.pessoa.nome_mae), str (lista.agente.pessoa.genero)]

    dados2 = [str (lista.agente.pessoa.data_nascimento), str (lista.agente.pessoa.provincia), 
    str (lista.agente.pessoa.estado_civil), str (lista.agente.pessoa.bi)]

    dados3 = [str (lista.agente.pessoa.residencia), str (lista.agente.pessoa.casa_numero), 
    str (lista.agente.pessoa.telefone), str (lista.agente.pessoa.email)]

    dados4 = [str (lista.agente.patente), str (lista.agente.categoria), 
    str (lista.agente.nip), str (lista.agente.data_igresso)]

    dados5 = [str (lista.agente.nivel_academico), str (lista.agente.curso), 
    str (lista.agente.funcao), str (lista.data_colocacao)]

    dados6 = [str (lista.agente.numero_contribuite), str (lista.agente.numero_caixa_social), 
    str ( lista.orgao_colocacao)]

    data1.append(dados1)

    #tabela 1 dos dao pessoais
    table1 = Table(data1, colWidths=[6 * cm, 5.3 * cm, 5.3 * cm, 2.6 * cm])
    table1.setStyle(TableStyle([
    ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
    ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.white)
    ]))

    #tabela 2 
    data2.append(dados2)
    table2 = Table(data2, colWidths=[4.5 * cm, 4.3 * cm, 4.3 * cm, 6.1 * cm])
    table2.setStyle(TableStyle([
    ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
    ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.white)
    ]))

    #tabela3
    data3.append(dados3)
    table3 = Table(data3, colWidths=[4.5 * cm, 4.3 * cm, 4.3 * cm, 6.1 * cm])
    table3.setStyle(TableStyle([
    ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
    ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.white)
    ]))

    #tabela4
    data4.append(dados4)
    table4 = Table(data4, colWidths=[6.2 * cm, 6.3 * cm, 3.2 * cm, 3.5 * cm])
    table4.setStyle(TableStyle([
    ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
    ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.white)
    ]))

    #tabela 5
    data5.append(dados5)
    table5 = Table(data5, colWidths=[3.2 * cm, 5.5 * cm, 5.4 * cm, 5.1 * cm])
    table5.setStyle(TableStyle([
    ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
    ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.white)
    ]))

    #tabela 6
    data6.append(dados6)
    table6 = Table(data6, colWidths=[4.1 * cm, 5.5 * cm, 7.9 * cm, 2.4 * cm])
    table6.setStyle(TableStyle([
    ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
    ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.white)
    ]))
    
    return (buffer, p, logo, fotofardado, logo_tabela, table1, table2, table3, table4, table5, table6, estilosB, style)




#FUNÇÃO QUE VAI GERAR A FICHA PESSOAL
@login_required
def ficha_pessoal(request, id=None):

    try:
        if id > 0 :

            
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="ficha_pessoal.pdf"'

            buffer, p, logo, fotofardado, logo_tabela, table1, table2, table3, table4, table5, table6, estilosB, style = cabecario_ficha(id)

            #tamanho da linha          
            p.setLineWidth(2)

            #logo do centro da angola
            p.drawImage(logo, 40, 750, width=65, height=70, mask=None)

            # dados da respublica
            p.drawString(115,800,'REPÚBLICA DE ANGOLA')
            p.drawString(115,785,'MINISTÉRIO DO INTERIOR')
            p.drawString(115,770,'POLICIA NACIONAL')
            p.drawString(115,755,'COMANDO PROVÍNCIAL DE LUANDA')
            p.drawString(115,740,'DIRECÇÃO PROVÍNCIAL DE RECURSOS HUMANOS')
            p.line(0,740,700,650)


            # logo da fotofardado
            p.drawImage(fotofardado, 495, 750, width=60, height=60, mask=None)

            # zona do comunicado o informação que deve ser descrita
            p.drawString(248,660,'Ficha de Agente')
            
            #imagem para os dados pessoal 
            p.drawImage(logo_tabela, 24.5, 600.3, width=544.6, height=40, mask=None)
            p.drawString(30,626,'Dados Pessoal')

            #imagem para os dados de agente 
            p.drawImage(logo_tabela, 24.5, 472.5, width=544.6, height=35, mask=None)
            p.drawString(30,490,'Dados de Agente')


            width, height = A4
            #0nde começa a ser construida a tabela dos dados pessoais
            # primeira linha
            table1.wrapOn(p, width, height)
            table1.drawOn(p, 25, 580)

            # segunda linha
            table2.wrapOn(p, width, height)
            table2.drawOn(p, 25, 543.4)

            #terecira linha
            table3.wrapOn(p, width, height)
            table3.drawOn(p, 25, 509.2)
            
            #onde começa se construida a tabela de dados de agente
            #quarta linha
            table4.wrapOn(p, width, height)
            table4.drawOn(p, 25, 445.4)

            #quinta
            table5.wrapOn(p, width, height)
            table5.drawOn(p, 25, 410.3)
            
            #sexta
            table6.wrapOn(p, width, height)
            table6.drawOn(p, 25, 374)



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
            response['Content-Disposition'] = 'inline; filename="ficha_pessoal.pdf"'

            buffer, p, logo, fotofardado, logo_tabela, table1, table2, table3, table4, table5, table6, estilosB, style = cabecario_ficha(id)

            #tamanho da linha          
            p.setLineWidth(2)

            #logo do centro da angola
            p.drawImage(logo, 40, 750, width=65, height=70, mask=None)

            # dados da respublica
            p.drawString(115,800,'REPÚBLICA DE ANGOLA')
            p.drawString(115,785,'MINISTÉRIO DO INTERIOR')
            p.drawString(115,770,'POLICIA NACIONAL')
            p.drawString(115,755,'COMANDO PROVÍNCIAL DE LUANDA')
            p.drawString(115,740,'DIRECÇÃO PROVÍNCIAL DE RECURSOS HUMANOS')
            p.line(0,740,700,650)

            # logo da fotofardado
            p.drawImage(fotofardado, 495, 750, width=60, height=60, mask=None)
            # zona do comunicado o informação que deve ser descrita
            p.drawString(248,658,'Ficha de Processo Disciplinar')
            #imagem para os dados pessoal 
            p.drawImage(logo_tabela, 24.5, 600.3, width=544.6, height=40, mask=None)
            p.drawString(30,626,'Dados Pessoal')

            #imagem para os dados de agente 
            p.drawImage(logo_tabela, 24.5, 472.5, width=544.6, height=35, mask=None)
            p.drawString(30,490,'Dados de Agente')

            #imagem para dados disciplinar
            p.drawImage(logo_tabela, 24.5, 319.3, width=544.6, height=35, mask=None)
            p.drawString(30,335.5,'Processo Disciplinar')

            
            #criando dados para o processo disciplinar
             #0nde começa a ser construida a tabela
            processo = Paragraph(''' Processo Nº''',estilosB)
            data_disc = Paragraph(''' Data ''',estilosB)
            motivo = Paragraph(''' Motivo ''',estilosB)
            dispacho = Paragraph(''' Despacho ''',estilosB)
            pena = Paragraph(''' Resultado ( Pena ) ''',estilosB)
            descricao = Paragraph(''' Descrição ''',estilosB)
            
            discip1 = []
            discip2 = []
            discip1.append([processo, data_disc, dispacho])
            discip2.append([motivo, pena])

            dados_disciplinar = []
            dados_disciplinar = [str (disciplina.numero_processo), str (disciplina.data), 
            str (disciplina.dispacho)]

            dados_disciplinar2 = []
            dados_disciplinar2 = [str (disciplina.motivo), str (disciplina.pena)]

            width, height = A4
            #0nde começa a ser construida a tabela dos dados pessoais
            # primeira linha
            table1.wrapOn(p, width, height)
            table1.drawOn(p, 25, 580)

            # segunda linha
            table2.wrapOn(p, width, height)
            table2.drawOn(p, 25, 543.4)

            #terecira linha
            table3.wrapOn(p, width, height)
            table3.drawOn(p, 25, 509.2)
            
            #onde começa se construida a tabela de dados de agente
            #quarta linha
            table4.wrapOn(p, width, height)
            table4.drawOn(p, 25, 445.4)

            #quinta
            table5.wrapOn(p, width, height)
            table5.drawOn(p, 25, 410.3)
            
            #sexta
            table6.wrapOn(p, width, height)
            table6.drawOn(p, 25, 374)


            # tabela de dados da disciplina
            discip1.append(dados_disciplinar)
            table = Table(discip1, colWidths=[6.2 * cm, 6.5 * cm, 6.5 * cm, 3.4 * cm])
            table.setStyle(TableStyle([
            ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.white)
            ]))
            table.wrapOn(p, width, height)
            table.drawOn(p, 25, 290)

            discip2.append(dados_disciplinar2)
            table = Table(discip2, colWidths=[6.5 * cm, 10.9 * cm, 3.1 * cm, 1.5 * cm])
            table.setStyle(TableStyle([
            ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.white)
            ]))
            table.wrapOn(p, width, height)
            table.drawOn(p, 25, 253.3)

            estilo = style["Normal"]
            style.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            corpo = Paragraph('''<bold><font size=12>'''+ str(disciplina.descricao) + '''</font></bold>''', estilo)
            #p.drawString(30,210.5,'Este é um widget de texto. O Widget de texto permite que você adicione texto ou HTML a qualquer barra lateral em seu tema. Você pode usar um widget de texto para exibir texto, links, imagens, HTML ou uma combinação desses elementos. Edite ')

            aw = 25
            ah = 210
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



