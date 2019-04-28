from header.includes import *


@login_required
def area_estatistica(request):
    pessoa = Pessoa.objects.all()
    transferencia = Transferencia.objects.prefetch_related('agente').all()
    formacao = Formacao_conclusao.objects.select_related('agente').all()
    reforma = Reforma.objects.select_related('agente').all()

    total_reforma = len(reforma)
    total_formacao = len(formacao)
    total_transferencia = len(transferencia)
    total_pessoa = len(pessoa)
    context = {
        'total_pessoa': total_pessoa, 
        'total_transferencia': total_transferencia, 
        'total_formacao': total_formacao, 
        'total_reforma': total_reforma,
        'estatistcas': MENU_ESTATISTICA}
    template = TEMPLATE_UTILIZADOR['estat']
    return render(request, template, context)


@login_required
def estatistica_transferencia(request):
    transferencia = Transferencia.objects.prefetch_related('agente').all()
    troca = Troca.objects.prefetch_related('primeiro_agente').all()

    total_transfe = len(transferencia)
    total_troca = len(troca)
   
    context = {
        'total_transfe':json.dumps(total_transfe),
        'total_troca': json.dumps(total_troca),
        'estatistcas': MENU_ESTATISTICA}
    template = TEMPLATE_ESTATISTICA["estat_transf"]
    return render(request, template, context)


@login_required
def estatistica_baixas(request):
    baixa = Baixa.objects.select_related('agente').all()
    total_baixa = len(baixa)
    total_Reforma = 0
    total_Demissao = 0
    total_Transferencia = 0
    total_Falecimento = 0
    total_Dificiencia = 0
    total_Invalidez = 0
    total_Outro = 0

    for cont, p in enumerate(baixa, 1):
        if p.motivo_baixa == 'Reforma':
            total_Reforma = + 1
        if p.motivo_baixa == 'Demissão':
            total_Demissao = + 1
        if p.motivo_baixa == 'Transferência':
            total_Transferencia = + 1
        if p.motivo_baixa == 'Falecimento':
            total_Falecimento = + 1
        if p.motivo_baixa == 'Dificiência Contraída':
            total_Dificiencia = + 1
        if p.motivo_baixa == 'Invalidez':
            total_Invalidez = + 1
        if p.motivo_baixa == 'Outro':
            total_Outro = + 1

    context = {
        'total_Reforma':json.dumps(total_Reforma),'total_Demissao':json.dumps(total_Demissao),
        'total_Transferencia':json.dumps(total_Transferencia),'total_Falecimento':json.dumps(total_Falecimento),
        'total_Dificiencia':json.dumps(total_Dificiencia),'total_Invalidez':json.dumps(total_Invalidez),
        'total_Outro':json.dumps(total_Outro),'total_baixas':json.dumps(total_baixa),
        'estatistcas': MENU_ESTATISTICA
        }

    template = TEMPLATE_ESTATISTICA["estat_baixa"]
    return render(request, template, context)



#Estatistica da reforma
@login_required
def estatistica_reforma(request):
    pessoa = Reforma.objects.select_related('agente').all()
    total_anticipada = 0
    total_normal = 0
    total_reforma = len(pessoa)

    for x, p in enumerate(pessoa):
        if p.reforma == 'Anticipada':
            total_anticipada = +1
        else:
            total_normal = + 1
    context = {
        'total_anticipada': json.dumps(total_anticipada),
        'total_normal': json.dumps(total_normal),
        'total_reforma': json.dumps(total_reforma),
        'estatistcas': MENU_ESTATISTICA}
    template = TEMPLATE_ESTATISTICA["estat_reforma"]
    return render(request, template, context) 



@login_required
def estatistica_selecionadoFormacao(request):
    selecionado = Selecionado_formacao.objects.select_related('agente').all()
    total_masculino = 0
    total_femenino = 0
    total_bolsaInterna = 0
    total_bolsaExterna = 0
    total_selecionado = len(selecionado)
    for x, p in enumerate(selecionado, 1):
        if p.razao_posse == 'Bolsa Interna':
            total_bolsaInterna = +1
            if p.agente.pessoa.genero == 'Masculino':
                total_masculino = +1
            else:
                total_femenino =+1
        else:
            total_bolsaExterna = +1
            if p.agente.pessoa.genero == 'Masculino':
                total_masculino = +1
            else:
                total_femenino =+1
    context = {
        'total_bolsaInterna': json.dumps(total_bolsaInterna),
        'total_bolsaExterna': json.dumps(total_bolsaExterna),
        'total_masculino': json.dumps(total_masculino),
        'total_femenino': json.dumps(total_femenino),
        'total_selecionado': json.dumps(total_selecionado),
        'estatistcas': MENU_ESTATISTICA}
    template = TEMPLATE_ESTATISTICA["selecionado"]
    return render(request, template, context)



@login_required
def estatistica_formacaoConcluida(request):
    conclusao = Formacao_conclusao.objects.select_related('agente').all()
    total_desistente = 0
    total_aprovados = 0
    total_reprovado = 0
    total_bolsaInterna = 0
    total_bolsaExterna = 0
    total_conclusao = len(conclusao)

    for k, p in enumerate(conclusao, 1):
        
        if p.aproveitamento == 'Desistente':
            total_desistente = +1
            if p.razao_posse == 'Bolsa Interna':
                total_bolsaInterna = +1
            else:
                total_bolsaExterna = +1
        if p.aproveitamento == 'Reprovado':
            total_reprovado = +1
            if p.razao_posse == 'Bolsa Interna':
                total_bolsaInterna = +1
            else:
                total_bolsaExterna = +1
        if p.aproveitamento == 'Aprovado':
            total_aprovados = +1
            if p.razao_posse == 'Bolsa Interna':
                total_bolsaInterna = +1
            else:
                total_bolsaExterna = +1 
    
    context = {
        'total_bolsaInterna': json.dumps(total_bolsaInterna),
        'total_bolsaExterna': json.dumps(total_bolsaExterna),
        'total_desistente': json.dumps(total_desistente),
        'total_aprovados': json.dumps(total_aprovados),
        'total_reprovado': json.dumps(total_reprovado),
        'total_conclusao': json.dumps(total_conclusao),
        'estatistcas': MENU_ESTATISTICA}
    template = TEMPLATE_ESTATISTICA["conclusao"]
    return render(request, template, context)
            



def retorna_idade(value):
    aux = []
    aux = value.split('/')
    return DATA_ANO - int (aux[2])


#CABEÇARIO DE TODAS AS LISTA NOMINAL
def cabecario_listas():
    dados = []
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, rightMargin=16, leftMargin=20,topMargin=20, bottomMargin=25, pagesize=letter,)
                        
    styles = getSampleStyleSheet()
    estilo_paragrafo = ParagraphStyle('Normal', alignment=TA_CENTER, fontSize=12,fontName="Times-Roman")
    #LOGO DA POLICIA
    #logo_policia = os.path.join(settings.MEDIA_ROOT, str('pol.jpg'))
    #policia = Image(logo_policia, width=48, height=48, mask=None, hAlign='LEFT')
    #LOGO DA POLICIA
    #dados.append( policia)
    dados.append(Spacer(1, 4))
    #LOGO DA REPUBLICA
    logo_angola = os.path.join(settings.MEDIA_ROOT, str('logo.jpeg'))
    angola= Image(logo_angola, width=72, height=75, mask=None, hAlign='CENTER')
    dados.append(angola)
    dados.append(Spacer(1, 6))
    
    cabecario = Paragraph('REPÚBLICA DE ANGOLA', estilo_paragrafo)
    dados.append(cabecario)
    dados.append(Spacer(1, 3))
    cabecario2 = Paragraph('MINISTÉRIO DO INTERIOR', estilo_paragrafo)
    dados.append(cabecario2)
    dados.append(Spacer(1, 3))
    cabecario3 = Paragraph('POLICIA NACIONAL', estilo_paragrafo)
    dados.append(cabecario3)
    dados.append(Spacer(1, 3))
    cabecario4 = Paragraph('COMANDO PROVÍNCIAL DE LUANDA', estilo_paragrafo)
    dados.append(cabecario4)
    dados.append(Spacer(1, 3))
    cabecario4 = Paragraph('DIRECÇÃO PROVÍNCIAL DE RECURSOS HUMANOS', estilo_paragrafo)
    dados.append(cabecario4)
    dados.append(Spacer(1, 101))
    linea_firma = Line(0,100,555,100)
    d = Drawing(0, 5)
    d.add(linea_firma)
    dados.append(d)
    #retornoo de cada funcionalidade
    return (buffer, dados, doc, styles)
    

def myFirstPage(canvas, doc):
    #PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
    Title = "Salakiaku"
    canvas.saveState()
    #canvas.setFont('Times-Bold',16)
    #canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.45 * inch, "Comando Províncial de Luanda / %s" % Title)
    canvas.restoreState()


def footer_rodape(canvas, doc):
    pageinfo = "Salakiaku"
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Comando Províncial de Luanda /  %s" %  pageinfo)
    canvas.restoreState()


# FUNÇÃO QUE VAI CONSTRUIR A PARTE DA TABELA COM TODOS DADOS 
def listar_tabelas(dados, cabeca, lista, doc, response, buffer):
    folha = []
    dados.append(Spacer(1, 20))
    folha = Table([cabeca] + lista)
    folha.setStyle(TableStyle([
            ('GRID', (0, 0), (7, -1), 1.3,  colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.white)
        ]
    ))
    dados.append(folha)
    dados.append(PageBreak())
    doc.build(dados, onFirstPage=myFirstPage, onLaterPages=footer_rodape)
    response.write(buffer.getvalue())
    buffer.close()



# LISTA NORMAL PONTO PRINCIPAL PATENTE
@login_required
def lista_normal(request):
    form = NormalPatente_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            patente = form.cleaned_data.get('patente')
            genero = form.cleaned_data.get('genero')
            titulo = form.cleaned_data.get('titulo')
            descricao = form.cleaned_data.get('descricao')
            
            #   aque e onde começa a criação do pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename={0}.pdf'.format(titulo)
            #response['Content-Disposition'] = 'attachment; filename="lista_nominal.pdf"'
            
            #A PASSSAR OSO DADOS DO CABECARIO
            buffer, dados, doc, styles = cabecario_listas()
            dados.append(Spacer(3, -78))
            estilo_paragrafo = ParagraphStyle('cabeça', alignment=TA_CENTER, fontSize=14,fontName="Times-Roman")
            ti = Paragraph(titulo, estilo_paragrafo)
            dados.append(ti)
            dados.append(Spacer(3, 20))
            # INFORMAÇÃO DA LISTA
            header = Paragraph(descricao, styles['Normal'])
            styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            dados.append(header)
            cabeca = ('#', 'AGENTE Nº', 'NOME', 'GENERO', 'PROVINCIA', 'TELEFONE', 'PATENTE') 
            lista = []
            lista = [(cont, p.numero_agente, p.pessoa.nome,  p.pessoa.genero, p.pessoa.provincia, p.pessoa.telefone, p.patente)
            for cont, p in enumerate(Agente.objects.select_related('pessoa').filter(patente=patente), 1)  if p.pessoa.genero == genero]
             
            listar_tabelas(dados, cabeca, lista, doc, response, buffer)
            return response

    context = {'normal': form, 'estatistcas': MENU_ESTATISTICA}
    template = TEMPLATE_ESTATISTICA["normal"]
    return render(request, template, context)        
        



# listagem do nivel academico
@login_required
def listar_nivel_academico(request):
    form = NivelAcademico_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            patente = form.cleaned_data.get('patente')
            nivel_academico = form.cleaned_data.get('nivel_academico')
            titulo = form.cleaned_data.get('titulo')
            descricao = form.cleaned_data.get('descricao')
            #  aque e onde começa a criação do pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename={0}.pdf'.format(titulo)
            
            #A PASSSAR OSO DADOS DO CABECARIO
            buffer, dados, doc, styles = cabecario_listas()
            dados.append(Spacer(3, -78))
            estilo_paragrafo = ParagraphStyle('cabeça', alignment=TA_CENTER, fontSize=14,fontName="Times-Roman")
            ti = Paragraph(titulo, estilo_paragrafo)
            dados.append(ti)
            dados.append(Spacer(1, 27))
            # INFORMAÇÃO DA LISTA
            header = Paragraph(descricao, styles['Normal'])
            styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            dados.append(header)

            lista = []
            cabeca = ('#', 'AGENTE Nº', 'NOME', 'GENERO', 'NIVEL ACADEMICO', 'CURSO', 'FUNÇÃO', 'PATENTE') 
            if nivel_academico:
                lista = [(cont, p.numero_agente, p.pessoa.nome, p.pessoa.genero, p.nivel_academico, p.curso, p.funcao, p.patente) 
                for cont, p in enumerate(Agente.objects.select_related('pessoa').filter(nivel_academico=nivel_academico), 1)  if p.patente == patente ]
            
            listar_tabelas(dados, cabeca, lista, doc, response, buffer)
            return response

    context = {'academico': form, 'estatistcas': MENU_ESTATISTICA }
    template = TEMPLATE_ESTATISTICA["academico"]
    return render(request, template, context)  



#views que vai gerar a lista em pdf dos agente na reforma
@login_required
def listar_reforma(request):
    form = ReformaLista_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            patente = form.cleaned_data.get('patente')
            titulo = form.cleaned_data.get('titulo')
            anticipada = form.cleaned_data.get('anticipada')
            descricao = form.cleaned_data.get('descricao')
            #  aque e onde começa a criação do pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename={0}.pdf'.format(titulo)
            #A PASSSAR OSO DADOS DO CABECARIO
            buffer, dados, doc, styles = cabecario_listas()
            dados.append(Spacer(3, -78))
            estilo_paragrafo = ParagraphStyle('cabeça', alignment=TA_CENTER, fontSize=14,fontName="Times-Roman")
            ti = Paragraph(titulo, estilo_paragrafo)
            dados.append(ti)
            dados.append(Spacer(1, 30))
            # INFORMAÇÃO DA LISTA
            header = Paragraph(descricao, styles['Normal'])
            styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            dados.append(header)

            lista = [] 
            cabeca = ('#', 'AGENTE Nº', 'NOME', 'GENERO', 'DATA NASCIMENTO', 'IDADE', 'REFORMA', 'PATENTE') 
            if patente is not None:
                if anticipada == 'Anticipada':
                    lista = [(cont, p.agente.numero_agente, p.agente.pessoa.nome, p.agente.pessoa.genero, p.agente.pessoa.data_nascimento, retorna_idade(p.agente.pessoa.data_nascimento),  p.reforma, p.agente.patente) 
                    for cont, p in enumerate(Reforma.objects.select_related('agente').filter(reforma=anticipada), 1) ]
                else:
                    lista = [(cont-1, p.agente.numero_agente, p.agente.pessoa.nome, p.agente.pessoa.genero, p.agente.pessoa.data_nascimento, retorna_idade(p.agente.pessoa.data_nascimento),  p.reforma, p.agente.patente)
                    for cont,pa in enumerate(Agente.objects.select_related('pessoa').filter(patente=patente), 1)
                    for  p in Reforma.objects.select_related('agente').filter(agente_id=pa.id)]
            listar_tabelas(dados, cabeca, lista, doc, response, buffer)
            return response

    context = {'reforma': form, 'estatistcas': MENU_ESTATISTICA }
    template = TEMPLATE_ESTATISTICA["reforma"]
    return render(request, template, context) 



#views que vai gerar a lista em pdf de baixas 
@login_required
def listar_baixa(request):
    form = BaixaLista_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            motivo = form.cleaned_data.get('motivo')
            titulo = form.cleaned_data.get('titulo')
            descricao = form.cleaned_data.get('descricao')
            #  aque e onde começa a criação do pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename={0}.pdf'.format(titulo)
            
            #A PASSSAR OSO DADOS DO CABECARIO
            buffer, dados, doc, styles = cabecario_listas()
            dados.append(Spacer(3, -78))
            estilo_paragrafo = ParagraphStyle('cabeça', alignment=TA_CENTER, fontSize=14,fontName="Times-Roman")
            ti = Paragraph(titulo, estilo_paragrafo)
            dados.append(ti)
            dados.append(Spacer(1, 30))
            # INFORMAÇÃO DA LISTA
            header = Paragraph(descricao, styles['Normal'])
            styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            dados.append(header)

            lista = [] 
            cabeca =()
            if motivo is not None:
                if motivo == 'Invalidez':
                    cabeca = ('#', 'Nª AGENTE', 'NOME', 'GENERO', 'DATA', 'MOTIVO', 'INVALIDEZ', 'PATENTE') 
                    lista = [(cont, p.agente.numero_agente, p.agente.pessoa.nome, p.agente.pessoa.genero, p.data_oucorrencia, p.motivo_baixa, p.tipo_invalidez, p.agente.patente) 
                    for cont, p in enumerate(Baixa.objects.select_related('agente').filter(motivo_baixa=motivo), 1) ]
                else:
                    cabeca = ('#', 'Nª AGENTE', 'NOME', 'GENERO', 'PROVINCIA', 'DATA', 'MOTIVO', 'PATENTE') 
                    lista = [(cont, p.agente.numero_agente, p.agente.pessoa.nome, p.agente.pessoa.genero, p.agente.pessoa.provincia,  p.data_oucorrencia, p.motivo_baixa, p.agente.patente) 
                    for cont, p in enumerate(Baixa.objects.select_related('agente').filter(motivo_baixa=motivo), 1) ]
            listar_tabelas(dados, cabeca, lista, doc, response, buffer)
            return response

    context = {'baixa': form, 'estatistcas': MENU_ESTATISTICA }
    template = TEMPLATE_ESTATISTICA["baixa"]
    return render(request, template, context) 




#views que vai gerar a lista em pdf dos agente despromovidos
@login_required
def listar_disciplinar(request):
    form = DisciplinarLista_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            motivo = form.cleaned_data.get('motivo')
            titulo = form.cleaned_data.get('titulo')
            descricao = form.cleaned_data.get('descricao')
            ano = form.cleaned_data.get('ano')
            #  aque e onde começa a criação do pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename={0}.pdf'.format(titulo)
            #A PASSSAR OSO DADOS DO CABECARIO
            buffer, dados, doc, styles = cabecario_listas()
            dados.append(Spacer(3, -78))
            estilo_paragrafo = ParagraphStyle('cabeça', alignment=TA_CENTER, fontSize=14,fontName="Times-Roman")
            ti = Paragraph(titulo, estilo_paragrafo)
            dados.append(ti)
            dados.append(Spacer(1, 30))
            # INFORMAÇÃO DA LISTA
            header = Paragraph(descricao, styles['Normal'])
            styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            dados.append(header)

            lista = [] 
            cabeca = ('#', 'NOME', 'DATA', 'MOTIVO', 'PENA', 'PATENTE') 
            if motivo is not None:
                if ano == '':
                    lista = [(cont, p.agente.pessoa.nome, p.data, p.motivo, p.pena, p.agente.patente) 
                    for cont, p in enumerate(Disciplina.objects.select_related('agente').filter(motivo=motivo), 1) ]
                else:
                    lista = [(cont, p.agente.pessoa.nome, p.data, p.motivo, p.pena, p.agente.patente) 
                    for cont, p in enumerate(Disciplina.objects.select_related('agente').filter(data__endswith = ano), 1) ]
                    
                    
            listar_tabelas(dados, cabeca, lista, doc, response, buffer)
            return response

    context = {'disciplia': form, 'estatistcas': MENU_ESTATISTICA }
    template = TEMPLATE_ESTATISTICA["disciplina"]
    return render(request, template, context) 




#views que vai gerar a lista em pdf dos agente dos agente em formação
@login_required
def listar_formacao(request):
    form = FormacaoLista_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            tipo = form.cleaned_data.get('tipo')
            titulo = form.cleaned_data.get('titulo')
            descricao = form.cleaned_data.get('descricao')
            ano = form.cleaned_data.get('ano')
            #  aque e onde começa a criação do pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename={0}.pdf'.format(titulo)
            
            #A PASSSAR OSO DADOS DO CABECARIO
            buffer, dados, doc, styles = cabecario_listas()
            dados.append(Spacer(3, -78))
            estilo_paragrafo = ParagraphStyle('normal', alignment=TA_CENTER, fontSize=14,fontName="Times-Roman")
            ti = Paragraph(titulo, estilo_paragrafo)
            dados.append(ti)
            dados.append(Spacer(1, 30))
            # INFORMAÇÃO DA LISTA
            header = Paragraph(descricao, styles['Normal'])
            styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            dados.append(header)

            lista = [] 
            cabeca = () 
            if tipo:
                if tipo == 'formacao':
                    if ano:
                        cabeca = ('#', 'Nª AGENTE', 'NOME', 'PAIS', 'BOLSA', 'CURSO', 'PATENTE') 
                        lista = [(cont, p.agente.numero_agente, p.agente.pessoa.nome, p.pais, p.razao_posse,p.curso, p.agente.patente) 
                        for cont, p in enumerate(Selecionado_formacao.objects.select_related('agente').filter(data__startswith = ano), 1) ]
                    else:
                        cabeca = ('#', 'Nª AGENTE', 'NOME', 'PAIS', 'BOLSA', 'CURSO', 'PATENTE') 
                        lista = [(cont, p.agente.numero_agente, p.agente.pessoa.nome, p.pais, p.razao_posse,p.curso, p.agente.patente) 
                        for cont, p in enumerate(Selecionado_formacao.objects.select_related('agente').all()) ]
                else:
                    if ano is not None and tipo:
                        cabeca = ('#', 'NOME', 'PAIS', 'BOLSA', 'CURSO', 'APROVEITAMENTO', 'PATENTE') 
                        lista = [(cont, p.agente.pessoa.nome, p.pais, p.razao_posse, p.curso, p.aproveitamento, p.agente.patente) 
                        for cont, p in  enumerate(Formacao_conclusao.objects.select_related('agente').filter(aproveitamento=tipo, data_conclusao__endswith = ano).all(), 1) ]
                    else:
                        cabeca = ('#', 'NOME', 'PAIS', 'BOLSA', 'CURSO', 'APROVEITAMENTO', 'PATENTE') 
                        lista = [(cont, p.agente.pessoa.nome, p.pais, p.razao_posse, p.curso, p.aproveitamento, p.agente.patente) 
                        for cont, p in  enumerate(Formacao_conclusao.objects.select_related('agente').filter(aproveitamento=tipo).all(), 1) ]
            
            listar_tabelas(dados, cabeca, lista, doc, response, buffer)
            return response

    context = {'formacao': form, 'estatistcas': MENU_ESTATISTICA }
    template = TEMPLATE_ESTATISTICA["formacao"]
    return render(request, template, context) 
