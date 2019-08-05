from header.includes import *


@login_required
def area_transferencia(request):
    dados = {'fotos':request.session['salakiaku'], 'transferencias': MENU_TRANSFERENCIA}
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
    if request.method == 'POST':
        if form.is_valid():
            ids = header.views_core.retorna_numero_agente(form.cleaned_data.get('bi'))
            desp = form.save(commit=False)
            desp.agente_id = ids
            desp.save()
            template = TEMPLATE_UTILIZADOR['perfil_rota']
            sweetify.success(request, 'Dados atualizado com sucesso!....', button='Ok', timer='3500')
            return HttpResponseRedirect(reverse('transferencia:area-transferencia'))
    
    pes = Pessoa.objects.get(id=pedido.agente_id)
    #pes = header.views_core.retorna_nip_bi()
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
                except Agente.DoesNotExist:
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

    
    ap = Transferencia.objects.get(id=id)
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Declaração_pessoal.pdf"'
    #p = canvas.Canvas(buffer)
    
    doc = SimpleDocTemplate(buffer,pagesize=letter, rightMargin=55,leftMargin=55,topMargin=150,bottomMargin=75)
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    Story = []
    print(doc.height)

    #estilo = ParagraphStyle('TITULO', alignment = TA_CENTER ,fontSize = 12, fontName="Times-Roman")
    #ptext =Paragraph('LISTA NOMINAL',estilo)
    #LISTA.append(ptext)
    #LISTA.append(Spacer(1, 12))
    magName = "Pythonista"
    issueNum = 12
    subPrice = "99.00"
    limitedDate = "03/05/2010"
    freeGift = "tin foil hat"
    full_name = "Marvin Jones"
    address_parts = ["411 State St.", "Reno, NV 80158"]

    for page in range(10):
        # Create return address
        ptext = '<font size=12>%s</font>' % full_name
        Story.append(Paragraph(ptext, styles["Normal"]))       
        for part in address_parts:
            ptext = '<font size=12>%s</font>' % part.strip()
            Story.append(Paragraph(ptext, styles["Normal"]))
 
        Story.append(Spacer(1, 12))
        ptext = '<font size=12>Dear %s:</font>' % full_name.split()[0].strip()
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 12))
 
        ptext = """<font size=12>We would like to welcome you to our subscriber base 
        for %s Magazine! You will receive %s issues at the excellent introductory 
        price of $%s. Please respond by %s to start receiving your subscription 
        and get the following free gift: %s.</font>""" 
        ptext = ptext % (magName, issueNum, subPrice, limitedDate, freeGift)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
 
        ptext = '<font size=12>Thank you very much and we look forward to serving you.</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size=12>Sincerely,</font>'
        Story.append(Paragraph(ptext, styles["Normal"]))
       
        Story.append(PageBreak())
        #p.showPage()
        
       
        doc.build(Story, onFirstPage=header.views_core.rodape_imagem_Vertical, onLaterPages=header.views_core.rodape_imagem_Vertical)
        response.write(buffer.getvalue())
        buffer.close()
        return response
        
   



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
  



