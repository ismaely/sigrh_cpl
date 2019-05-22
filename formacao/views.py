from header.includes import *

@login_required
def area_formacao(request):
    dados = {'formacaoes': MENU_FORMACAO, 'fotos':request.session['salakiaku']}
    template = TEMPLATE_UTILIZADOR['fm']
    return render(request, template, dados)


# função que vai visualizar os dados do agente especifico que for solicitado
@login_required
def visualizar_informacao_conclusao(request, id=None):
    lista = Orgao.objects.select_related('agente').get(agente_id=id)
    formacao = Formacao_conclusao.objects.all().filter(agente_id=id)
    dados = {'lista': lista, 'formacao': formacao, 'formacaoes': MENU_FORMACAO, 'fotos':request.session['salakiaku']}
    template = TEMPLATE_FORMACAO['informacao']
    return render(request, template, dados)



#função que vai marca presença do agente na formação selecionado qdo recebe o guia de marcha
@login_required
def marca_precensa_selecionado(request, id):
    try:
        sels = Selecionado_formacao.objects.get(agente_id=id)
        presenca = Presenca.objects.create(agente_id=id, selecionado_id=sels.id, data=DATE_FORMAT)
        sweetify.success(request, 'Formação confirmada com sucesso...', button='Ok', timer='3300')
    except Exception as e:
        sweetify.error(request, 'Não foi possivel, agente não existe...', button='Ok', timer='3300')
        print(e)
    return HttpResponseRedirect(reverse('formacao:listar-selecionados'))



#função que vai buscar os dados do agente selecionado que vai ser atualizado
@login_required
def buscar_selecionado_atualizar(request):
    if request.method == 'POST':
        ids = header.views_core.retorna_numero_bi(request.POST['bi'])
        try:
            lista = Selecionado_formacao.objects.get(agente_id=ids)
            orgao = Orgao.objects.select_related('agente').get(agente_id=ids)
            #presenca = Presenca.objects.all()
            template = TEMPLATE_FORMACAO['selecionar']
            return render(request, template,{'lista': lista, 'orgao':orgao, 'fotos':request.session['salakiaku']})
        except Selecionado_formacao.DoesNotExist:
            sweetify.error(request, 'Não existe formação..', button='Ok', timer='4000')
            return HttpResponseRedirect(reverse('formacao:area-formacao'))

    sweetify.error(request, 'Não existe formação..', button='Ok', timer='4000')
    return HttpResponseRedirect(reverse('formacao:area-formacao'))





#views que vai pegar todos os dados do agente selecionado para formação
@login_required
def listar_agente_selecionado(request):
    lista = Selecionado_formacao.objects.select_related('agente').all()
    #orgao = Orgao.objects.select_related('agente').all()
    presenca = Presenca.objects.all()
    
    #limpar = lista.select_related(None)
    template = TEMPLATE_FORMACAO['selecionar']
    return render(request, template,{'lista': lista, 'presenca': presenca, 'formacaoes': MENU_FORMACAO, 'fotos':request.session['salakiaku']})



#função que vai listar agentes que estao na formação e q estao lista de selecionado
@login_required
def listar_agente_formacao(request):
    try:
        lista = Presenca.objects.all()
        dados = {'lista': lista, 'formacaoes': MENU_FORMACAO, 'fotos':request.session['salakiaku']}
        template = TEMPLATE_FORMACAO['listar_agente']
        return render(request, template, dados)
    except Exception as e:
        raise Http404("erro na listagem dos agentes  na formação %s" % (e))



@login_required
def listar_todos_terminaram_formacao(request):
    try:
        lista = Formacao_conclusao.objects.select_related('agente').all()
        dados = {'lista': lista, 'formacaoes': MENU_FORMACAO, 'fotos':request.session['salakiaku']}
        template = TEMPLATE_FORMACAO['listar_terminam']
        return render(request, template, dados)
    except Exception as e:
        raise Http404(" erro na listagem de todos que  ja terminaram a formacao %s " % (e))



@login_required
def listar_documentos(request):
    try:
        lista = []
        lista = documentacao.views.listar_documento()
        dados = {'listar': lista , 'pessoalQuadro': MENU_PESSOAL_QUADRO, 'fotos':request.session['salakiaku']}
        template = TEMPLATE_FORMACAO['listar_docs']
        return render(request, template, dados)

    except Exception as e:
        raise Http404("falha ao listar documento pessoa %s" % (e))



@login_required
def eliminar_documento(request, id=None):
    if id is not None:
        docs = Documento.objects.get(id=id).delete()
        sweetify.success(request, 'Documento eliminado com sucesso!....', button='Ok', timer='3500')
        return HttpResponseRedirect(reverse('formacao:listar-docs'))
    else:
        sweetify.error(request, 'Falha Não foi possivel!....', button='Ok', timer='3500')
        return HttpResponseRedirect(reverse('formacao:listar-docs'))



@login_required
def calcula_idade(request):
    if request.method == 'POST':
        dados = dict()
        #cod = request.body.decode('utf-8')

        #lista = json.loads(cod)
        #bi = lista['bi']
        bi = request.POST.get("bi")
        try:
            resp, data = header.validators.consultar_bi_True_False(bi)
            if resp:
                idade = header.views_core.retorna_idade(data)
                dados = {
                    'idade': idade,
                    'resp': True
                    }
                return JsonResponse(dados)
            else:
                dados = {
                    'idade': 0,
                    'False': False
                    }
                return JsonResponse(dados)
        except Exception as e:
            dados = {
                    'idade': 'erro no sistema',
                    'resp': False
                    }
            return JsonResponse(dados)



@login_required
def remover_lista_selecionado(request):
    if request.method == 'POST':
        dados = dict()
        cod = []
        cod = request.body.decode('utf-8')
        lista = json.loads(cod)
        id = lista['id']
        if id > 0:
            docs = Selecionado_formacao.objects.get(id=id).delete()
            dados = {
                    'validade': True,
                }
            return JsonResponse(dados)
        else:
            dados = {
                'validade': False,
            }
            return JsonResponse(dados)



@login_required
def remover_lista_conclusao(request):
    if request.method == 'POST':
        dados = dict()
        cod = []
        cod = request.body.decode('utf-8')
        lista = json.loads(cod)
        id = lista['id']
        if id > 0:
            docs = Formacao_conclusao.objects.get(id=id).delete()
            dados = {
                    'validade': True,
                }
            return JsonResponse(dados)
        else:
            dados = {
                'validade': False,
            }
            return JsonResponse(dados)



@login_required
def atualizar_selecionado_formacao(request, id):
    selec= Selecionado_formacao.objects.get(id=id)
    form = SelecionarForm(request.POST or None, instance=selec)
    if request.method == 'POST':
        if form.is_valid() and header.validators.consultar_bi_existe(request.POST['bi']):
            agen = header.views_core.retorna_numero_agente(form.cleaned_data.get('bi'))
            desp = form.save(commit=False)
            desp.agente_id = agen
            desp.save()
            sweetify.success(request, 'Daods atualizado com sucesso!....', button='Ok', timer='3300')
            return HttpResponseRedirect(reverse('formacao:area-formacao'))
        else:
            messages.warning(request, ' O bi não é valido, Não existe..')

    pes = Pessoa.objects.get(id=selec.agente_id)
    pessoa = PessoaForm(request.POST or None, instance=pes)
    dados = {'form': form, 'form2': pessoa, 'forma': selec, 'formacaoes': MENU_FORMACAO, 'fotos':request.session['salakiaku']}
    template = TEMPLATE_FORMACAO['adicionar']
    return render(request, template, dados)



@login_required
def registar_documentos(request):
    form = DocumentoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            if documentacao.views.registar_documento(request):
                sweetify.success(request, 'Documento Cadastrado com sucesso...', button='Ok')
                return HttpResponseRedirect(reverse('formacao:area-formacao'))

    dados = {'form': form, 'formacaoes': MENU_FORMACAO, 'fotos':request.session['salakiaku']}
    template =TEMPLATE_FORMACAO['docs']
    return render(request, template, dados)




#função que vai pegar os dados da formação concluida para atualizar
@login_required
def atualizar_conclusao_formacao(request, id):
    conclui = Formacao_conclusao.objects.get(id=id)
    form = FormacaoConlusao_Form(request.POST or None, instance=conclui)
    if request.method == 'POST':
        if form.is_valid() and header.validators.consultar_bi_existe(request.POST['bi']):
            agen = header.views_core.retorna_numero_agente(form.cleaned_data.get('bi'))
            desp = form.save(commit=False)
            desp.agente_id = agen
            desp.save()
            sweetify.success(request, 'Dados atualizado com sucesso....', button='Ok', timer='3300')
            return HttpResponseRedirect(reverse('formacao:area-formacao'))
        else:
            messages.warning(request, 'Não é valido o nip, Não existe..')

    pes = Pessoa.objects.get(id=conclui.agente_id)
    pessoa = PessoaForm(request.POST or None, instance=pes)
    dados = {'form': form, 'form2': pessoa, 'forma': conclui, 'fotos':request.session['salakiaku'], 'formacaoes': MENU_FORMACAO}
    template = TEMPLATE_FORMACAO['conclusao']
    return render(request, template, dados)



@login_required
def atualizar_documento(request, id):
    docs = Documento.objects.get(id=id)
    form = DocumentoForm(request.POST or None, instance=docs) 
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Dados atualizado com sucesso!....', button='Ok')
            return HttpResponseRedirect(reverse('formacao:area-formacao'))

    dados = {'form': form, 'docs': docs, 'fotos':request.session['salakiaku'], 'formacaoes': MENU_FORMACAO}
    template = TEMPLATE_FORMACAO['docs']
    return render(request, template, dados)



# função que vai registar a conclusão da formação
@login_required
def registar_conclusao_formacao(request):
    form = FormacaoConlusao_Form(request.POST or None)
    if request.method == 'POST':
        form = FormacaoConlusao_Form(request.POST, request.FILES or None)
        if form.is_valid():
            if header.validators.validar_conclusao_formacao(request):
                agen = header.views_core.retorna_numero_agente(form.cleaned_data.get('bi'))
                seleciona = Selecionado_formacao.objects.get(agente_id=agen)
                desp = form.save(commit=False)
                desp.agente_id = agen
                desp.curso = seleciona.curso
                desp.dispacho = seleciona.dispacho
                desp.razao_posse = seleciona.razao_posse
                #desp.ultima_funcao = seleciona.ultima_funcao
                desp.pais = seleciona.pais
                desp.instituicao = seleciona.instituicao
                desp.save()
                seleciona.delete()
                sweetify.success(request, 'Conclusão da formação adicionado com sucesso!....', button='Ok', timer='3300')
                return HttpResponseRedirect(reverse('formacao:area-formacao'))

    dados = {'form': form, 'fotos':request.session['salakiaku'], 'formacaoes': MENU_FORMACAO}
    template = TEMPLATE_FORMACAO['conclusao']
    return render(request, template, dados)



# função que vai registar o agente para formação
@login_required
def adicionar_agente_formacao(request):
    form = SelecionarForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            agen = header.views_core.retorna_numero_agente(form.cleaned_data.get('bi'))
            if header.validators.validar_selecionar_formacao(request) and header.validators.verficar_falecimento(request, agen):
                desp = form.save(commit=False)
                desp.agente_id = agen
                desp.save()
                dados = {}
                sweetify.success(request, 'Agente adicionado com sucesso!....', button='Ok', timer='3300')
                return HttpResponseRedirect(reverse('formacao:area-formacao'))

    dados = {'form': form, 'fotos':request.session['salakiaku'], 'formacaoes': MENU_FORMACAO}
    template = TEMPLATE_FORMACAO['adicionar']
    return render(request, template, dados)



@login_required
def consultar_documento(request):
    try:
        form = ConsultarDocumentoForms(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                lista = Documento.objects.filter(categoria=form.cleaned_data.get('categoria'))
                dados = {'form': form, 'listar': lista, 'formacaoes': MENU_FORMACAO}
                template = TEMPLATE_FORMACAO['consultar_doc']
                return render(request, template, dados)

    except Documento.DoesNotExist:
        print('erro na consulta de documento')

    dados = {'form': form, 'fotos':request.session['salakiaku'], 'formacaoes': MENU_FORMACAO}
    template = TEMPLATE_FORMACAO['consultar_doc']
    return render(request, template, dados)



@login_required
def consultar_formacao(request):
    if request.method == 'POST':
        value = request.POST['busca']
        if value is not None:
            agente = header.views_core.retorna_numero_agente_id(value)
            try:
                formacao = Formacao_conclusao.objects.filter(agente_id=agente)
                orgao = Orgao.objects.get(agente_id=agente)
                context = {'formacao': formacao, 'lista': orgao, 'formacaoes': MENU_FORMACAO}
                template = TEMPLATE_FORMACAO['consultar']
                return render(request, template, context)
            except Exception as e:
                sweetify.warning(request, 'Não existe agente cadastrado com esse numero no sistema!....', button='Ok', timer='3900')
                return HttpResponseRedirect(reverse('formacao:area-formacao'))
   
    template = TEMPLATE_FORMACAO['consultar']
    return render(request, template, {'fotos':request.session['salakiaku'], 'formacaoes': MENU_FORMACAO})





#Ficha para o processo disciplinar
@login_required
def ficha_formacao(request, id=None):

    try:

        lista_dados = Formacao_conclusao.objects.select_related('agente').filter(agente_id=id)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="ficha_pessoal.pdf"'

        buffer, p, logo, fotofardado, logo_tabela, table1, table2, table3, table4, table5, table6, estilosB, style = cabecarioFicha(id)

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
        p.drawString(248,658,'Ficha De Formações Realizada ')
        #imagem para os dados pessoal 
        p.drawImage(logo_tabela, 24.5, 600.3, width=544.6, height=40, mask=None)
        p.drawString(30,626,'Dados Pessoal')

        #imagem para os dados de agente 
        p.drawImage(logo_tabela, 24.5, 472.5, width=544.6, height=35, mask=None)
        p.drawString(30,490,'Dados de Agente')

        #imagem para barra cinza
        p.drawImage(logo_tabela, 24.5, 321.3, width=544.6, height=35, mask=None)
        p.drawString(30,341.5,'Formações Realizada')

        
        #criando dados para o processo disciplinar
            #0nde começa a ser construida a tabela
        curso = Paragraph(''' Curso''',estilosB)
        pais = Paragraph(''' Pais de Realização ''',estilosB)
        data = Paragraph(''' Data de Conclusão ''',estilosB)
        despacho = Paragraph(''' Despacho ''',estilosB)
        aproveitamento = Paragraph(''' Aproveitamento ''',estilosB)
        instituicao = Paragraph(''' Instituição ''',estilosB)
        bolsa = Paragraph(''' Bolsa ''',estilosB)
        
        discip1 = []
        discip2 = []
        discip1.append([curso, data, despacho, aproveitamento])
        discip2.append([pais, instituicao, bolsa])

        dados_formacao = []
        for formacao in lista_dados:
            dados_formacao = [str (formacao.curso), str (formacao.data_conclusao), str(formacao.dispacho), str (formacao.aproveitamento)]
        

        dados_formacao2 = []
        for formacao in lista_dados:
            dados_formacao2 = [str (formacao.pais), str (formacao.instituicao), str(formacao.razao_posse)]

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


        # tabela de dados da formação de conclusao
        discip1.append(dados_formacao)
        table = Table(discip1, colWidths=[8.7 * cm, 3.2 * cm, 3.1 * cm, 4.2 * cm])
        table.setStyle(TableStyle([
        ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
        ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.white)
        ]))
        table.wrapOn(p, width, height)
        table.drawOn(p, 25, 290)

        discip2.append(dados_formacao2)
        table = Table(discip2, colWidths=[4.4 * cm, 11.4 * cm, 3.4 * cm, 1.1 * cm])
        table.setStyle(TableStyle([
        ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
        ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.white)
        ]))
        table.wrapOn(p, width, height)
        table.drawOn(p, 25, 253.3)

        #estilo = style["Normal"]
        #style.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        #corpo = Paragraph('''<bold><font size=12>'''+ str(disciplina.descricao) + '''</font></bold>''', estilo)
        #p.drawString(30,210.5,'Este é um widget de texto. O Widget de texto permite que você adicione texto ou HTML a qualquer barra lateral em seu tema. Você pode usar um widget de texto para exibir texto, links, imagens, HTML ou uma combinação desses elementos. Edite ')

        aw = 25
        ah = 210
        #w, h = corpo.wrap(518, height)
        #corpo.drawOn(p, aw, ah)


        p.showPage()
        p.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
        
    except Formacao_conclusao.DoesNotExist:
        sweetify.error(request, 'Não existe dados do agente!....', button='Ok', timer='3500')
        return HttpResponseRedirect(reverse('formacao:area-formacao'))

    dados = {'formacaoes': MENU_FORMACAO }
    template = TEMPLATE_UTILIZADOR['fm']
    return render(request, template, {})




#função que vai buscar os dados da formação que ja terminaram para atualizar
"""@login_required
def buscar_conclusao_atualizacao(request):
    if request.method == 'POST':
        ids = header.views_core.retorna_numero_bi(request.POST['bi'])
        if ids > 0:
            lista = Formacao_conclusao.objects.select_related('agente').all().filter(agente_id=ids)
            dados = {'lista': lista}
            template = TEMPLATE_FORMACAO['busca_conclu']
            return render(request, template,{'lista': lista})

    sweetify.error(request, 'Não existe dados com este numero do bi..', button='Ok', timer='4000')
    return HttpResponseRedirect(reverse('formacao:area-formacao'))
"""
