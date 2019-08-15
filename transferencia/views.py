from header.includes import *


@login_required
def area_transferencia(request):
    form = Nip_Form(request.POST or None)
    dados = {'fotos':request.session['salakiaku'],'form':form, 'transferencias': MENU_TRANSFERENCIA}
    template = TEMPLATE_UTILIZADOR['tras']
    return render(request, template, dados)



#função que vai aprovar o pedido de transferencia do agente
@login_required
def aprovar_transferencia(request, id):
    if request.method == 'POST':
        ap = Transferencia.objects.get(id=id) 
        ap.situacao = "Aprovado" 
        ap.dispacho = request.POST['despacho']
        ap.save()
        sweetify.success(request, 'Trnsferência Realizada com Sucesso!....', button='Ok', timer='3500')
        return HttpResponseRedirect(reverse('transferencia:listar-pedidos'))

   

#função que vai cadastrar o pedido de troca do agente
@login_required
def adicionar_troca(request):
    form = TrocaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
           try:
                id_1 = header.views_core.retorna_numero_agente(form.cleaned_data.get('bi1'))
                id_2 = header.views_core.retorna_numero_agente(form.cleaned_data.get('bi2'))
                troca = form.save(commit=False)
                troca.origem_segundo = form.cleaned_data.get('destino_primeiro')
                troca.destino_segundo = form.cleaned_data.get('origem_primeiro')
                troca.primeiro_agente_id = id_1
                troca.segundo_agente_id = id_2
                troca.save()
                sweetify.success(request, 'Troca realizada com sucesso!....', button='Ok', timer='3500')
                return HttpResponseRedirect(reverse('transferencia:area-transferencia'))
           except Exception as e:
               print(e)
    
    context = {'form': form, 'fotos':request.session['salakiaku'], 'transferencias': MENU_TRANSFERENCIA}
    template = TEMPLATE_TRANSFERENCIA['troca']
    return render(request, template, context)
               


#função que vai registar o pedido de transferencia do agente
@login_required
def registar_transferencia(request):
    form = TransferenciaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            
            try:
                ids = header.views_core.retorna_numero_agente(form.cleaned_data.get('bi'))
                desp = form.save(commit=False)
                desp.agente_id = ids
                desp.save()
                sweetify.success(request, 'Dados Adicionado com sucesso!....', button='Ok', timer='3500')
                template = TEMPLATE_UTILIZADOR['perfil_rota']
                return HttpResponseRedirect(reverse('transferencia:area-transferencia'))
            except Exception as e :
                messages.warning(request, ' Não existe agente com esse numero no sistema...')
        
    context = {'form': form, 'fotos':request.session['salakiaku'], 'transferencias': MENU_TRANSFERENCIA}
    template = TEMPLATE_TRANSFERENCIA['transferencia']
    return render(request, template, context)



#função que vai atualizar os dados do pedido de transferencia
@login_required
def atualizar_pedido_transferencia(request, id):
    pedido =Transferencia.objects.get(id=id)
    form = TransferenciaForm(request.POST or None, instance=pedido)
    try:
        if request.method == 'POST':
            if form.is_valid():
                ids = header.views_core.retorna_numero_agente(form.cleaned_data.get('bi'))
                desp = form.save(commit=False)
                desp.agente_id = ids
                desp.save()
                template = TEMPLATE_UTILIZADOR['perfil_rota']
                sweetify.success(request, 'Dados atualizado com sucesso!....', button='Ok', timer='3500')
                return HttpResponseRedirect(reverse('transferencia:area-transferencia'))
    except Exception as e:
        print(" ERRO AO EDITAR TRANSFERENCIA")
    pes = Pessoa.objects.get(id=pedido.agente_id)
    pessoa = PessoaForm(request.POST or None, instance=pes)
    context = {'form': form, 'form2': pessoa, 'pedido': pedido, 'fotos':request.session['salakiaku'], 'transferencias': MENU_TRANSFERENCIA}
    template = TEMPLATE_TRANSFERENCIA['transferencia']
    return render(request, template, context)



@login_required
def atualizar_documento(request, id):
    docs = Documento.objects.get(id=id)
    form = DocumentoForm(request.POST or None, instance=docs) 
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Dados atualizado com sucesso!....', button='Ok')
            return HttpResponseRedirect(reverse('transferencia:area-transferencia'))

    dados = {'form': form, 'docs': docs, 'fotos':request.session['salakiaku'], 'transferencias': MENU_TRANSFERENCIA}
    template = TEMPLATE_TRANSFERENCIA['docs']
    return render(request, template, dados)



@login_required
def consultar_documento(request):
    try:
        form = ConsultarDocumentoForms(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                lista = Documento.objects.filter(categoria=form.cleaned_data.get('categoria'))
                dados = {'form': form, 'listar': lista, 'transferencias': MENU_TRANSFERENCIA}
                template = TEMPLATE_TRANSFERENCIA['consultar_doc']
                return render(request, template, dados)

    except Documento.DoesNotExist:
        messages.warning(request, ' Falha! Não existe Documento...')
        #sweetify.sweetalert(request, 'Falha! Não existe', type="error", button='Ok', timer='3600')

    dados = {'form': form, 'transferencias': MENU_TRANSFERENCIA}
    template = TEMPLATE_TRANSFERENCIA['consultar_doc']
    return render(request, template, dados)




@login_required
def listar_documentos(request):
    try:
        lista = []
        lista = documentacao.views.listar_documento()
        dados = {'listar': lista, 'fotos':request.session['salakiaku'],  'transferencias': MENU_TRANSFERENCIA }
        template = TEMPLATE_TRANSFERENCIA['listar_docs']
        return render(request, template, dados)

    except Exception as e:
        raise Http404("falha ao listar documento pessoa %s" % (e))




#FUNÇÃO QUE VAI LISTAR TODOS PEDIDOS DE TRANSFERENCIA
@login_required
def listar_pedido_transferencia(request):
    lista = Transferencia.objects.select_related('agente').all().filter(situacao="Espera")
    context = {'lista': lista, 'fotos':request.session['salakiaku'], 'transferencias': MENU_TRANSFERENCIA}
    template = TEMPLATE_TRANSFERENCIA['listar_pedido']
    return render(request, template, context)



#FUNÇÃO QUE VAI LISTAR TODOS AGENTES TRANSFERIDOS
@login_required
def listar_agentes_transferido(request):
    lista = Transferencia.objects.select_related('agente').all().filter(situacao="Aprovado")
    context = {'lista': lista, 'fotos':request.session['salakiaku'], 'transferencias': MENU_TRANSFERENCIA}
    template = TEMPLATE_TRANSFERENCIA['transferido']
    return render(request, template, context)



#função que vai listar a troca de transferencia de 
@login_required
def listar_troca_transferencia(request):
    lista = Troca.objects.all()
    context = {'lista': lista, 'fotos':request.session['salakiaku'], 'transferencias': MENU_TRANSFERENCIA}
    template = TEMPLATE_TRANSFERENCIA['listar_troca']
    return render(request, template, context)




@login_required
def consultar_transferencia(request):
    if request.method == 'POST':
        value = request.POST['busca']
        if value is not None and len(value) > 0:
            try:
                agen = Agente.objects.get(nip=value)
                if agen.nip is not None:
                    tras = Transferencia.objects.filter(agente_id=agen.id)
                    context = {'lista':tras, 'fotos':request.session['salakiaku'], 'transferencias': MENU_TRANSFERENCIA}
                    template = TEMPLATE_TRANSFERENCIA['listar_pedido']
                    return render(request, template, context)
            except Exception as e:
                try:
                    agent = Agente.objects.get(numero_agente=value)
                    if agent.nip is not None:
                        tras = Transferencia.objects.filter(agente_id=agent.id)
                        context = {'lista':tras, 'fotos':request.session['salakiaku'], 'transferencias': MENU_TRANSFERENCIA}
                        template = TEMPLATE_TRANSFERENCIA['listar_pedido']
                        return render(request, template, context)
                except Exception as e:
                    sweetify.warning(request, 'Não existem Transferencia para este agente!....', button='Ok', timer='3800')
                    return HttpResponseRedirect(reverse('transferencia:area-transferencia'))
                    
                
    context = {'fotos':request.session['salakiaku'], 'transferencias': MENU_TRANSFERENCIA}
    template = TEMPLATE_TRANSFERENCIA['mensagem']
    return render(request, template, context)




@login_required
def registar_documentos(request):
    form = DocumentoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            if documentacao.views.registar_documento(request):
                sweetify.success(request, 'Documento Cadastrado com sucesso...', button='Ok')
                return HttpResponseRedirect(reverse('transferencia:area-transferencia'))

    dados = {'form': form, 'fotos':request.session['salakiaku'], 'transferencias': MENU_TRANSFERENCIA}
    template =TEMPLATE_TRANSFERENCIA['docs']
    return render(request, template, dados)




@login_required
def eliminar_documento(request, id=None):
    if id is not None:
        docs = Documento.objects.get(id=id).delete()
        sweetify.success(request, 'Documento eliminado com sucesso!....', button='Ok', timer='3500')
        return HttpResponseRedirect(reverse('transferencia:listar-docs'))
    else:
        sweetify.error(request, 'Falha Não foi possivel!....', button='Ok', timer='3500')
        return HttpResponseRedirect(reverse('transferencia:listar-docs'))
 


@login_required
def emitir_guia_transferencia(request, id):
    value = id
    form = Nip_Form(request.POST or None)
    if request.method == 'POST' or value > 0:
        if form.is_valid():
            value = header.views_core.retorna_numero_agente(request.POST['nip'])
            print(value)
            #sweetify.error(request, 'Não pode ser lançada a nota porque, não esta inscrito na cadeira', position ='top-end',   persistent='OK')
        try:
            resp= Transferencia.objects.get(Q(id=value) | Q(agente_id=value))
            buffer = BytesIO()
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="guia_transferencia.pdf"'
            #p = canvas.Canvas(buffer)
            doc = SimpleDocTemplate(response ,pagesize=letter, rightMargin=55,leftMargin=55,topMargin=30,bottomMargin=75, author="Ismael")
            
            styles = getSampleStyleSheet()
            styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

            estilos = styles["Normal"]
            centro = ParagraphStyle(name='top',alignment=TA_CENTER, fontName="Times-Roman")
            negrito = ParagraphStyle(name='top',alignment=TA_CENTER, fontName="Times-Bold")
            direito = ParagraphStyle(name='top',alignment=TA_RIGHT, fontName="Times-Bold")
            simples = ParagraphStyle(name='top',alignment=TA_CENTER)
            Story = []

            #estilo = ParagraphStyle('TITULO', alignment = TA_CENTER ,fontSize = 12, fontName="Times-Roman")
            logo = os.path.join(settings.MEDIA_ROOT, str('logo.jpeg'))
            img = Image(logo, width=65, height=70,  mask=None, hAlign='CENTER')
            Story.append(img)

            Story.append(Spacer(1, 4))
            ANGOLA = '<font size=12>%s</font>' % ("REPÚBLICA DE ANGOLA")
            Story.append(Paragraph(ANGOLA, centro))
            Story.append(Spacer(1, 3))
            MINISTERIO = '<font size=12>%s</font>' % ("MINISTÉRIO DO INTERIOR")
            Story.append(Paragraph(MINISTERIO, centro))
            Story.append(Spacer(1, 3))
            POLICIA = '<font size=12>%s</font>' % ("COMANDO GERAL DA POLICIA NACIONAL")
            Story.append(Paragraph(POLICIA, centro))
            Story.append(Spacer(1, 3))
            GABINETE = '<font size=12>%s</font>' % ("GABINETE DO COMANDANTE")
            Story.append(Paragraph(GABINETE,negrito))
            Story.append(Spacer(1, 35))
            LETRA = '<font size=12>%s</font>' % ("À")
            Story.append(Paragraph(LETRA,negrito))
            Story.append(Spacer(1, 60))
            
            LUANDA = '<font size=12>= LUANDA =</font>'
            Story.append(Paragraph(LUANDA, direito))
            Story.append(Spacer(1, 65))
            
            DESPACHO = """<font size=12>Of. Nr. %s /GAB CGPN/328-L2GCG/2019</font>"""  %(str(resp.numero_guia))
            Story.append(Paragraph(DESPACHO,centro))
            Story.append(Spacer(1, 60))
            
            TEXTO = """ <font size=12>Para comprimento tenho a honra de autorizar a solicitação da transferencia,
        
            </font>""" 
            #styles["Justify"]
            Story.append(Paragraph(TEXTO, simples))
            Story.append(Spacer(1, 2))

            TEXTO = """<font size=12>
            datada do mes,e anexo, firmada pelo Agente: %s, que mereceu da sua Excelência Comandante Geral da Policia Nacional,
            o seguinte despacho: %s
            .</font>""" 
            TEXTO = TEXTO % (str(resp.agente.pessoa.nome), str(resp.dispacho))
            Story.append(Paragraph(TEXTO, styles["Justify"]))

            TEXTO = """<font size=12>
            O mesmo fara parate do orgão: %s, partir da data anuciada %s, que consta no despacho da autorização. O referido 
            documento entra imediadamente emm vigor. </font>""" 
            TEXTO = TEXTO % (str(resp.orgao_destino), str(resp.data_entrada))
            Story.append(Paragraph(TEXTO, styles["Justify"]))

            Story.append(Spacer(1, 75))
            GABINETE = '<font size=12>%s</font>' % ("PELA ORDEM E PELA PAZ AO SERVIÇO DA NAÇÃO")
            Story.append(Paragraph(GABINETE,negrito))

            Story.append(Spacer(1, 95))
            GABINETE = '<font size=12>%s</font>' % ("**** COMISSÁRIO-GERAL ****")
            Story.append(Paragraph(GABINETE,negrito))
            Story.append(Spacer(1, 12))

            Story.append(PageBreak())
            #p.showPage()
            doc.build(Story, onFirstPage=rodape_guia, onLaterPages=rodape_guia)
            response.write(buffer.getvalue())
            buffer.close()
            return response
        except Exception as e:
            sweetify.error(request, 'Não possui guia de transferencia', position ='top-end',   persistent='OK')
        
    sweetify.error(request, 'Não possui guia de transferencia', position ='top-end',   persistent='OK')
    return HttpResponseRedirect(reverse('transferencia:listar'))


def rodape_guia(canvas, doc):
    #page_num = canvas.getPageNumber()
    SR = "S/Referência"
    canvas.drawRightString(7.9*cm, 16.2*cm, SR)
    SC = "S/Comunicação"
    canvas.drawRightString(13.4*cm, 16.2*cm, SC)
    NR= "N/Referência"
    canvas.drawRightString(18.4*cm, 16.2*cm, NR)
    canvas.setFont('Times-Roman', 11)
    GUIA= "GUIA DE AUTORIZAÇÃO DE TRANSFERÊNCIA.-"
    canvas.drawRightString(13.0*cm, 13.6*cm, GUIA)
    canvas.line(125,384,370,384)
    canvas.setFont('Times-Bold', 12)
    DN = "D.N. RECURSOS HUMANOS"
    canvas.drawRightString(16.2*cm, 19.8*cm, DN)
    



#função que vai remover o pedido de transferencia
@login_required
def remover_pedido_transferencia(request):
    if request.method == 'POST':
        dados = dict()
        cod = []
        cod = request.body.decode('utf-8')
        lista = json.loads(cod)
        id = lista['id']
        if id > 0:
            docs = Transferencia.objects.get(id=id).delete()
            dados = {
                    'validade': True,
                }
            return JsonResponse(dados) 
        else:
            dados = {
                'validade': False,
            }
            return JsonResponse(dados)
  