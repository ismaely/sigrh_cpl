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
        'estatistcas': MENU_ESTATISTICA,
        'fotos':request.session['salakiaku']}
    template = TEMPLATE_UTILIZADOR['estat']
    return render(request, template, context)


@login_required
def estatistica_transferencia(request):
    form = Estatistica_Transferencia_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            masculino = 0
            femenino = 0
            total = 0
            patente = form.cleaned_data.get('patente')
            titulo = form.cleaned_data.get('titulo')
            data = form.cleaned_data.get('data')
            data_final = form.cleaned_data.get('data_final')
            tipo = form.cleaned_data.get('tipo')
            if patente:
                if data < data_final and tipo != 'Troca' and data_final:
                    transferencia=Transferencia.objects.select_related('agente').filter(agente__patente=patente,data_entrada__range=(data, data_final), situacao=tipo)
                    total = len(transferencia)
                    for item in transferencia:
                        if item.agente.pessoa.genero == 'M':
                            masculino += 1
                        elif item.agente.pessoa.genero == 'F':
                            femenino += 1
                    context = {
                    'masculino':json.dumps( masculino), 'femenino': json.dumps(femenino), 'total': json.dumps(total),
                    'estatistcas': MENU_ESTATISTICA,  'fotos':request.session['salakiaku']}
                    template = TEMPLATE_ESTATISTICA["estat_transf"]
                    return render(request, template, context)
                
                elif data and tipo != 'Troca' and tipo:
                    transferencia=Transferencia.objects.select_related('agente').filter(agente__patente=patente,data_entrada__contains=data[:-3], situacao=tipo)
                    total = len(transferencia)
                    for item in transferencia:
                        if item.agente.pessoa.genero == 'M':
                            masculino += 1
                        elif item.agente.pessoa.genero == 'F':
                            femenino += 1
                    context = {
                    'masculino':json.dumps( masculino), 'femenino': json.dumps(femenino), 'total': json.dumps(total),
                    'estatistcas': MENU_ESTATISTICA,  'fotos':request.session['salakiaku']}
                    template = TEMPLATE_ESTATISTICA["estat_transf"]
                    return render(request, template, context)
                
                elif data < data_final and tipo == 'Troca' and data_final:
                    trocas=Troca.objects.select_related('agente').filter(Q(primeiro_agente__patente=patente)|Q(segundo_agente__patente=patente),data_entrada__range=(data, data_final))
                    total = len(trocas)
                    for item in trocas:
                        if item.agente.pessoa.genero == 'M':
                            masculino += 1
                        elif item.agente.pessoa.genero == 'F':
                            femenino += 1
                    context = {
                    'masculino':json.dumps( masculino), 'femenino': json.dumps(femenino), 'total': json.dumps(total),
                    'estatistcas': MENU_ESTATISTICA,  'fotos':request.session['salakiaku']}
                    template = TEMPLATE_ESTATISTICA["estat_transf"]
                    return render(request, template, context)
                
                elif data and tipo == 'Troca':
                    trocas=Troca.objects.select_related('agente').filter(Q(primeiro_agente__patente=patente)|Q(segundo_agente__patente=patente),data_entrada__contains=data[:-3])
                    total = len(trocas)
                    for item in trocas:
                        if item.agente.pessoa.genero == 'M':
                            masculino += 1
                        elif item.agente.pessoa.genero == 'F':
                            femenino += 1
                    context = {
                    'masculino':json.dumps( masculino), 'femenino': json.dumps(femenino), 'total': json.dumps(total),
                    'estatistcas': MENU_ESTATISTICA,  'fotos':request.session['salakiaku']}
                    template = TEMPLATE_ESTATISTICA["estat_transf"]
                    return render(request, template, context)
                
                elif tipo != 'Troca':
                    transferencia=Transferencia.objects.select_related('agente').filter(agente__patente=patente, situacao=tipo)
                    total = len(transferencia)
                    for item in transferencia:
                        if item.agente.pessoa.genero == 'M':
                            masculino += 1
                        elif item.agente.pessoa.genero == 'F':
                            femenino += 1
                    context = {
                    'masculino':json.dumps( masculino), 'femenino': json.dumps(femenino), 'total': json.dumps(total),
                    'estatistcas': MENU_ESTATISTICA,  'fotos':request.session['salakiaku']}
                    template = TEMPLATE_ESTATISTICA["estat_transf"]
                    return render(request, template, context)
            #DATA
            elif data:
                if data < data_final and tipo != 'Troca' and tipo and data_final:
                    transferencia=Transferencia.objects.select_related('agente').filter(data_entrada__range=(data, data_final), situacao=tipo)
                    total = len(transferencia)
                    for item in transferencia:
                        if item.agente.pessoa.genero == 'M':
                            masculino += 1
                        elif item.agente.pessoa.genero == 'F':
                            femenino += 1
                    context = {
                    'masculino':json.dumps( masculino), 'femenino': json.dumps(femenino), 'total': json.dumps(total),
                    'estatistcas': MENU_ESTATISTICA,  'fotos':request.session['salakiaku']}
                    template = TEMPLATE_ESTATISTICA["estat_transf"]
                    return render(request, template, context)
                
                elif data and tipo == 'Troca':
                    trocas=Troca.objects.select_related('agente').filter(data_entrada__startswith=data[:-3],situacao=tipo)
                    total = len(trocas)
                    for item in trocas:
                        if item.agente.pessoa.genero == 'M':
                            masculino += 1
                        elif item.agente.pessoa.genero == 'F':
                            femenino += 1
                    context = {
                    'masculino':json.dumps( masculino), 'femenino': json.dumps(femenino), 'total': json.dumps(total),
                    'estatistcas': MENU_ESTATISTICA,  'fotos':request.session['salakiaku']}
                    template = TEMPLATE_ESTATISTICA["estat_transf"]
                    return render(request, template, context)
                
                elif data:
                    transferencia=Transferencia.objects.select_related('agente').filter(data_entrada__startswith=data[:-3])
                    total = len(transferencia)
                    for item in transferencia:
                        if item.agente.pessoa.genero == 'M':
                            masculino += 1
                        elif item.agente.pessoa.genero == 'F':
                            femenino += 1
                    context = {
                    'masculino':json.dumps( masculino), 'femenino': json.dumps(femenino), 'total': json.dumps(total),
                    'estatistcas': MENU_ESTATISTICA,  'fotos':request.session['salakiaku']}
                    template = TEMPLATE_ESTATISTICA["estat_transf"]
                    return render(request, template, context)
            # TIPO
            elif tipo:
                if tipo == 'Troca':
                    trocas=Troca.objects.select_related('agente').filter(situacao=tipo)
                    total = len(trocas)
                    for item in trocas:
                        if item.agente.pessoa.genero == 'M':
                            masculino += 1
                        elif item.agente.pessoa.genero == 'F':
                            femenino += 1
                    context = {
                    'masculino':json.dumps( masculino), 'femenino': json.dumps(femenino), 'total': json.dumps(total),
                    'estatistcas': MENU_ESTATISTICA,  'fotos':request.session['salakiaku']}
                    template = TEMPLATE_ESTATISTICA["estat_transf"]
                    return render(request, template, context)
                
                elif tipo != 'Troca':
                    transferencia=Transferencia.objects.select_related('agente').filter(situacao=tipo)
                    total = len(transferencia)
                    for item in transferencia:
                        if item.agente.pessoa.genero == 'M':
                            masculino += 1
                        elif item.agente.pessoa.genero == 'F':
                            femenino += 1
                    context = {
                    'masculino':json.dumps( masculino), 'femenino': json.dumps(femenino), 'total': json.dumps(total),
                    'estatistcas': MENU_ESTATISTICA,  'fotos':request.session['salakiaku']}
                    template = TEMPLATE_ESTATISTICA["estat_transf"]
                    return render(request, template, context)

    context = {'form':form , 'fotos':request.session['salakiaku']}
    template = TEMPLATE_ESTATISTICA["menu_transfer"]
    return render(request, template, context)


#estatistica baixas
@login_required
def estatistica_baixas(request):
    form = Estatistica_Baixa_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            total_baixa = 0
            total_Reforma = 0
            total_Demissao = 0
            total_Transferencia = 0
            total_Falecimento = 0
            total_Dificiencia = 0
            total_Invalidez = 0
            total_Outro = 0
            patente = form.cleaned_data.get('patente')
            titulo = form.cleaned_data.get('titulo')
            data = form.cleaned_data.get('data')
            data_final = form.cleaned_data.get('data_final')

            if patente:
                if data and data_final:
                    baixa = Baixa.objects.select_related('agente').filter(agente__patente=patente,data_oucorrencia__range=(data, data_final))
                    for cont, p in enumerate(baixa, 1):
                        if p.motivo_baixa == 'Reforma':
                            total_Reforma += 1
                        elif p.motivo_baixa == 'Demissão':
                            total_Demissao += 1
                        elif p.motivo_baixa == 'Transferência':
                            total_Transferencia += 1
                        elif p.motivo_baixa == 'Falecimento':
                            total_Falecimento += 1
                        elif p.motivo_baixa == 'Dificiência Contraída':
                            total_Dificiencia += 1
                        elif p.motivo_baixa == 'Invalidez':
                            total_Invalidez += 1
                        elif p.motivo_baixa == 'Outro':
                            total_Outro += 1

                    context = {
                        'fotos':request.session['salakiaku'], 'total_Reforma':json.dumps(total_Reforma),
                        'total_Demissao':json.dumps(total_Demissao), 'total_Transferencia':json.dumps(total_Transferencia),
                        'total_Falecimento':json.dumps(total_Falecimento), 'total_Dificiencia':json.dumps(total_Dificiencia),
                        'total_Invalidez':json.dumps(total_Invalidez), 'total_Outro':json.dumps(total_Outro),
                        'total_baixas':json.dumps(total_baixa), 'estatistcas': MENU_ESTATISTICA,
                    }
                    template = TEMPLATE_ESTATISTICA["estat_baixa"]
                    return render(request, template, context)
                else:
                    baixa = Baixa.objects.select_related('agente').filter(agente__patente=patente)
                    for cont, p in enumerate(baixa, 1):
                        if p.motivo_baixa == 'Reforma':
                            total_Reforma += 1
                        elif p.motivo_baixa == 'Demissão':
                            total_Demissao += 1
                        elif p.motivo_baixa == 'Transferência':
                            total_Transferencia += 1
                        elif p.motivo_baixa == 'Falecimento':
                            total_Falecimento += 1
                        elif p.motivo_baixa == 'Dificiência Contraída':
                            total_Dificiencia += 1
                        elif p.motivo_baixa == 'Invalidez':
                            total_Invalidez += 1
                        elif p.motivo_baixa == 'Outro':
                            total_Outro += 1
                    context = {
                        'fotos':request.session['salakiaku'], 'total_Reforma':json.dumps(total_Reforma),
                        'total_Demissao':json.dumps(total_Demissao), 'total_Transferencia':json.dumps(total_Transferencia),
                        'total_Falecimento':json.dumps(total_Falecimento), 'total_Dificiencia':json.dumps(total_Dificiencia),
                        'total_Invalidez':json.dumps(total_Invalidez), 'total_Outro':json.dumps(total_Outro),
                        'total_baixas':json.dumps(total_baixa), 'estatistcas': MENU_ESTATISTICA,
                    }
                    template = TEMPLATE_ESTATISTICA["estat_baixa"]
                    return render(request, template, context)
            else:
                if data:
                    baixa = Baixa.objects.select_related('agente').filter(data_oucorrencia__startswith=data[:-3])
                    for cont, p in enumerate(baixa, 1):
                        if p.motivo_baixa == 'Reforma':
                            total_Reforma += 1
                        elif p.motivo_baixa == 'Demissão':
                            total_Demissao += 1
                        elif p.motivo_baixa == 'Transferência':
                            total_Transferencia += 1
                        elif p.motivo_baixa == 'Falecimento':
                            total_Falecimento += 1
                        elif p.motivo_baixa == 'Dificiência Contraída':
                            total_Dificiencia += 1
                        elif p.motivo_baixa == 'Invalidez':
                            total_Invalidez += 1
                        elif p.motivo_baixa == 'Outro':
                            total_Outro += 1

                    context = {
                        'fotos':request.session['salakiaku'], 'total_Reforma':json.dumps(total_Reforma),
                        'total_Demissao':json.dumps(total_Demissao), 'total_Transferencia':json.dumps(total_Transferencia),
                        'total_Falecimento':json.dumps(total_Falecimento), 'total_Dificiencia':json.dumps(total_Dificiencia),
                        'total_Invalidez':json.dumps(total_Invalidez), 'total_Outro':json.dumps(total_Outro),
                        'total_baixas':json.dumps(total_baixa), 'estatistcas': MENU_ESTATISTICA,
                    }
                    template = TEMPLATE_ESTATISTICA["estat_baixa"]
                    return render(request, template, context)

    context = {
        'fotos':request.session['salakiaku'], 'form':form,'estatistcas': MENU_ESTATISTICA}
    template = TEMPLATE_ESTATISTICA["menu_baixa"]
    return render(request, template, context)





#Estatistica da reforma
@login_required
def estatistica_reforma(request):
    form = Estatistica_reforma_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            patente = form.cleaned_data.get('patente')
            tipo = form.cleaned_data.get('tipo')
            data = form.cleaned_data.get('data')
            data_final = form.cleaned_data.get('data_final')
            total_anticipada = 0
            total_Incapacidade =0
            total_acidente = 0
            total_dificiencia = 0
            total_outro = 0
            total_reforma = 0
            if patente and tipo and data:
                reforma = Reforma.objects.select_related('agente').filter(agente__patente=patente, data__startswith=data[:-3], reforma=tipo)
                total_anticipada = len(reforma)
                for x, p in enumerate(reforma):
                    if p.motivo == 'Acidente':
                        total_acidente += 1
                    elif p.motivo == 'Incapacidade':
                        total_Incapacidade += 1
                    elif p.motivo == 'Dificiência Contraída':
                        total_dificiencia += 1
                    elif p.motivo == 'Outro':
                        total_outro += 1
        
                context = {
                    'total_anticipada': json.dumps(total_anticipada),
                    'total_Incapacidade': json.dumps(total_Incapacidade),'total_acidente': json.dumps(total_acidente),
                    'total_dificiencia': json.dumps(total_dificiencia), 'total_outro': json.dumps(total_outro),
                    'total_reforma': json.dumps(total_reforma),'estatistcas': MENU_ESTATISTICA,
                    'fotos':request.session['salakiaku']}
                template = TEMPLATE_ESTATISTICA["estat_reforma"]
                return render(request, template, context)

            elif tipo and data:
                reforma = Reforma.objects.select_related('agente').filter(data__startswith=data[:-3], reforma=tipo)
                total_anticipada = len(reforma)
                for x, p in enumerate(reforma):
                    if p.motivo == 'Acidente':
                        total_acidente += 1
                    elif p.motivo == 'Incapacidade':
                        total_Incapacidade += 1
                    elif p.motivo == 'Dificiência Contraída':
                        total_dificiencia += 1
                    elif p.motivo == 'Outro':
                        total_outro += 1
                context = {
                    'total_anticipada': json.dumps(total_anticipada),
                    'total_Incapacidade': json.dumps(total_Incapacidade),'total_acidente': json.dumps(total_acidente),
                    'total_dificiencia': json.dumps(total_dificiencia), 'total_outro': json.dumps(total_outro),
                    'total_reforma': json.dumps(total_reforma),'estatistcas': MENU_ESTATISTICA,
                    'fotos':request.session['salakiaku']}
                template = TEMPLATE_ESTATISTICA["estat_reforma"]
                return render(request, template, context) 

            elif patente and data:
                reforma = Reforma.objects.select_related('agente').filter(agente__patente=patente, data__startswith=data[:-3])
                total_anticipada = len(reforma)
                for x, p in enumerate(reforma):
                    if p.motivo == 'Acidente':
                        total_acidente += 1
                    elif p.motivo == 'Incapacidade':
                        total_Incapacidade += 1
                    elif p.motivo == 'Dificiência Contraída':
                        total_dificiencia += 1
                    elif p.motivo == 'Outro':
                        total_outro += 1
                context = {
                    'total_anticipada': json.dumps(total_anticipada),
                    'total_Incapacidade': json.dumps(total_Incapacidade),'total_acidente': json.dumps(total_acidente),
                    'total_dificiencia': json.dumps(total_dificiencia), 'total_outro': json.dumps(total_outro),
                    'total_reforma': json.dumps(total_reforma),'estatistcas': MENU_ESTATISTICA,
                    'fotos':request.session['salakiaku']}
                template = TEMPLATE_ESTATISTICA["estat_reforma"]
                return render(request, template, context) 

            elif patente and tipo:
                reforma = Reforma.objects.select_related('agente').filter(agente__patente=patente, reforma=tipo)
                total_anticipada = len(reforma)
                for x, p in enumerate(reforma):
                    if p.motivo == 'Acidente':
                        total_acidente += 1
                    elif p.motivo == 'Incapacidade':
                        total_Incapacidade += 1
                    elif p.motivo == 'Dificiência Contraída':
                        total_dificiencia += 1
                    elif p.motivo == 'Outro':
                        total_outro += 1
        
                context = {
                    'total_anticipada': json.dumps(total_anticipada),
                    'total_Incapacidade': json.dumps(total_Incapacidade),'total_acidente': json.dumps(total_acidente),
                    'total_dificiencia': json.dumps(total_dificiencia), 'total_outro': json.dumps(total_outro),
                    'total_reforma': json.dumps(total_reforma),'estatistcas': MENU_ESTATISTICA,
                    'fotos':request.session['salakiaku']}
                template = TEMPLATE_ESTATISTICA["estat_reforma"]
                return render(request, template, context) 
            elif patente:
                reforma = Reforma.objects.select_related('agente').filter(agente__patente=patente)
                total_anticipada = len(reforma)
                for x, p in enumerate(reforma):
                    if p.motivo == 'Acidente':
                        total_acidente += 1
                    elif p.motivo == 'Incapacidade':
                        total_Incapacidade += 1
                    elif p.motivo == 'Dificiência Contraída':
                        total_dificiencia += 1
                    elif p.motivo == 'Outro':
                        total_outro += 1
        
                context = {
                    'total_anticipada': json.dumps(total_anticipada),
                    'total_Incapacidade': json.dumps(total_Incapacidade),'total_acidente': json.dumps(total_acidente),
                    'total_dificiencia': json.dumps(total_dificiencia), 'total_outro': json.dumps(total_outro),
                    'total_reforma': json.dumps(total_reforma),'estatistcas': MENU_ESTATISTICA,
                    'fotos':request.session['salakiaku']}
                template = TEMPLATE_ESTATISTICA["estat_reforma"]
                return render(request, template, context) 
            elif tipo:
                reforma = Reforma.objects.select_related('agente').filter(reforma=tipo)
                total_anticipada = len(reforma)
                for x, p in enumerate(reforma):
                    if p.motivo == 'Acidente':
                        total_acidente += 1
                    elif p.motivo == 'Incapacidade':
                        total_Incapacidade += 1
                    elif p.motivo == 'Dificiência Contraída':
                        total_dificiencia += 1
                    elif p.motivo == 'Outro':
                        total_outro += 1
        
                context = {
                    'total_anticipada': json.dumps(total_anticipada),
                    'total_Incapacidade': json.dumps(total_Incapacidade),'total_acidente': json.dumps(total_acidente),
                    'total_dificiencia': json.dumps(total_dificiencia), 'total_outro': json.dumps(total_outro),
                    'total_reforma': json.dumps(total_reforma),'estatistcas': MENU_ESTATISTICA,
                    'fotos':request.session['salakiaku']}
                template = TEMPLATE_ESTATISTICA["estat_reforma"]
                return render(request, template, context) 
            elif data:
                reforma = Reforma.objects.select_related('agente').filter(data__startswith=data[:-3])
                total_anticipada = len(reforma)
                for x, p in enumerate(reforma):
                    if p.motivo == 'Acidente':
                        total_acidente += 1
                    elif p.motivo == 'Incapacidade':
                        total_Incapacidade += 1
                    elif p.motivo == 'Dificiência Contraída':
                        total_dificiencia += 1
                    elif p.motivo == 'Outro':
                        total_outro += 1
        
                context = {
                    'total_anticipada': json.dumps(total_anticipada),
                    'total_Incapacidade': json.dumps(total_Incapacidade),'total_acidente': json.dumps(total_acidente),
                    'total_dificiencia': json.dumps(total_dificiencia), 'total_outro': json.dumps(total_outro),
                    'total_reforma': json.dumps(total_reforma),'estatistcas': MENU_ESTATISTICA,
                    'fotos':request.session['salakiaku']}
                template = TEMPLATE_ESTATISTICA["estat_reforma"]
                return render(request, template, context) 

    context = {
        'form': form,'estatistcas': MENU_ESTATISTICA, 'fotos':request.session['salakiaku']}
    template = TEMPLATE_ESTATISTICA["menu_reforma"]
    return render(request, template, context) 



# gerar estatistica de agentes selecionados para formação
@login_required
def estatistica_selecionadoFormacao(request):
    form = Estatistica_AgentesSelecionados_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            patente = form.cleaned_data.get('patente')
            data = form.cleaned_data.get('data')
            titulo = form.cleaned_data.get('titulo')
            total_masculino = 0
            total_femenino = 0
            total_bolsaInterna = 0
            total_bolsaExterna = 0
            total_selecionado = 0
            
            if patente and data:
                selecionado=Selecionado_formacao.objects.select_related('agente').filter(agente__patente=patente,data__startswith=data[:-3])
                total_selecionado = len(selecionado)
                for item in selecionado:
                    if item.razao_posse == 'Bolsa Interna':
                        total_bolsaInterna +=1
                        if item.agente.pessoa.genero == 'M':
                            total_masculino += 1
                        else:
                            total_femenino += 1
                    else:
                        total_bolsaExterna +=1
                        if item.agente.pessoa.genero == 'M':
                            total_masculino += 1
                        else:
                            total_femenino += 1
                context = {
                    'total_bolsaInterna': json.dumps(total_bolsaInterna),'total_bolsaExterna': json.dumps(total_bolsaExterna),
                    'total_masculino': json.dumps(total_masculino), 'total_femenino': json.dumps(total_femenino), 'total_selecionado': json.dumps(total_selecionado),
                    'estatistcas': MENU_ESTATISTICA, 'fotos':request.session['salakiaku']
                }
                template = TEMPLATE_ESTATISTICA["selecionado"]
                return render(request, template, context)

            elif patente:
                selecionado=Selecionado_formacao.objects.select_related('agente').filter(agente__patente=patente)
                total_selecionado = len(selecionado)
                for item in selecionado:
                    if item.razao_posse == 'Bolsa Interna':
                        total_bolsaInterna +=1
                        if item.agente.pessoa.genero == 'M':
                            total_masculino += 1
                        else:
                            total_femenino += 1
                    else:
                        total_bolsaExterna +=1
                        if item.agente.pessoa.genero == 'M':
                            total_masculino += 1
                        else:
                            total_femenino += 1
                context = {
                    'total_bolsaInterna': json.dumps(total_bolsaInterna),'total_bolsaExterna': json.dumps(total_bolsaExterna),
                    'total_masculino': json.dumps(total_masculino), 'total_femenino': json.dumps(total_femenino), 'total_selecionado': json.dumps(total_selecionado),
                    'estatistcas': MENU_ESTATISTICA, 'fotos':request.session['salakiaku']
                }
                template = TEMPLATE_ESTATISTICA["selecionado"]
                return render(request, template, context)

            elif data:
                selecionado=Selecionado_formacao.objects.select_related('agente').filter(data__startswith=data[:-3])
                total_selecionado = len(selecionado)
                for item in selecionado:
                    if item.razao_posse == 'Bolsa Interna':
                        total_bolsaInterna +=1
                        if item.agente.pessoa.genero == 'M':
                            total_masculino += 1
                        else:
                            total_femenino += 1
                    else:
                        total_bolsaExterna +=1
                        if item.agente.pessoa.genero == 'M':
                            total_masculino += 1
                        else:
                            total_femenino += 1
                context = {
                    'total_bolsaInterna': json.dumps(total_bolsaInterna),'total_bolsaExterna': json.dumps(total_bolsaExterna),
                    'total_masculino': json.dumps(total_masculino), 'total_femenino': json.dumps(total_femenino), 'total_selecionado': json.dumps(total_selecionado),
                    'estatistcas': MENU_ESTATISTICA, 'fotos':request.session['salakiaku']
                }
                template = TEMPLATE_ESTATISTICA["selecionado"]
                return render(request, template, context)
    context = {
        'form': form,'estatistcas': MENU_ESTATISTICA, 'fotos':request.session['salakiaku']
    }
    template = TEMPLATE_ESTATISTICA["menu_selecionado"]
    return render(request, template, context) 




@login_required
def estatistica_formacaoConcluida(request):
    form = Estatistica_ConclusaoFormacao_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            patente = form.cleaned_data.get('patente')
            data = form.cleaned_data.get('data')
            tipo = form.cleaned_data.get('tipo')
            data_final = form.cleaned_data.get('data_final')
            total_desistente = 0
            total_aprovados = 0
            total_reprovado = 0
            total_bolsaInterna = 0
            total_bolsaExterna = 0
            total_conclusao = 0

            if patente and data and tipo:
                conclusao=Formacao_conclusao.objects.select_related('agente').filter(agente__patente=patente,data_conclusao__startswith=data[:-3], razao_posse=tipo)
                total_conclusao = len(conclusao)
                for k, p in enumerate(conclusao, 1):
                    if p.aproveitamento == 'Desistente':
                        total_desistente += 1
                        if p.razao_posse == 'Bolsa Interna':
                            total_bolsaInterna += 1
                        else:
                            total_bolsaExterna += 1
                    elif p.aproveitamento == 'Reprovado':
                        total_reprovado += 1
                        if p.razao_posse == 'Bolsa Interna':
                            total_bolsaInterna += 1
                        else:
                            total_bolsaExterna += 1
                    elif p.aproveitamento == 'Aprovado':
                        total_aprovados += 1
                        if p.razao_posse == 'Bolsa Interna':
                            total_bolsaInterna += 1
                        else:
                            total_bolsaExterna += 1
    
                context = {
                    'total_bolsaInterna': json.dumps(total_bolsaInterna), 'total_bolsaExterna': json.dumps(total_bolsaExterna),
                    'total_desistente': json.dumps(total_desistente),  'total_aprovados': json.dumps(total_aprovados),
                    'total_reprovado': json.dumps(total_reprovado), 'total_conclusao': json.dumps(total_conclusao),
                    'estatistcas': MENU_ESTATISTICA,  'fotos':request.session['salakiaku']}
                template = TEMPLATE_ESTATISTICA["conclusao"]
                return render(request, template, context)

            elif patente and tipo:
                conclusao=Formacao_conclusao.objects.select_related('agente').filter(agente__patente=patente, razao_posse=tipo)
                total_conclusao = len(conclusao)
                for k, p in enumerate(conclusao, 1):
                    if p.aproveitamento == 'Desistente':
                        total_desistente += 1
                        if p.razao_posse == 'Bolsa Interna':
                            total_bolsaInterna += 1
                        else:
                            total_bolsaExterna += 1
                    elif p.aproveitamento == 'Reprovado':
                        total_reprovado += 1
                        if p.razao_posse == 'Bolsa Interna':
                            total_bolsaInterna += 1
                        else:
                            total_bolsaExterna += 1
                    elif p.aproveitamento == 'Aprovado':
                        total_aprovados += 1
                        if p.razao_posse == 'Bolsa Interna':
                            total_bolsaInterna += 1
                        else:
                            total_bolsaExterna += 1
    
                context = {
                    'total_bolsaInterna': json.dumps(total_bolsaInterna), 'total_bolsaExterna': json.dumps(total_bolsaExterna),
                    'total_desistente': json.dumps(total_desistente),  'total_aprovados': json.dumps(total_aprovados),
                    'total_reprovado': json.dumps(total_reprovado), 'total_conclusao': json.dumps(total_conclusao),
                    'estatistcas': MENU_ESTATISTICA,  'fotos':request.session['salakiaku']}
                template = TEMPLATE_ESTATISTICA["conclusao"]
                return render(request, template, context)
                
            elif data and tipo:
                conclusao=Formacao_conclusao.objects.select_related('agente').filter(data_conclusao__startswith=data[:-3], razao_posse=tipo)
                total_conclusao = len(conclusao)
                for k, p in enumerate(conclusao, 1):
                    if p.aproveitamento == 'Desistente':
                        total_desistente += 1
                        if p.razao_posse == 'Bolsa Interna':
                            total_bolsaInterna += 1
                        else:
                            total_bolsaExterna += 1
                    elif p.aproveitamento == 'Reprovado':
                        total_reprovado += 1
                        if p.razao_posse == 'Bolsa Interna':
                            total_bolsaInterna += 1
                        else:
                            total_bolsaExterna += 1
                    elif p.aproveitamento == 'Aprovado':
                        total_aprovados += 1
                        if p.razao_posse == 'Bolsa Interna':
                            total_bolsaInterna += 1
                        else:
                            total_bolsaExterna += 1
    
                context = {
                    'total_bolsaInterna': json.dumps(total_bolsaInterna), 'total_bolsaExterna': json.dumps(total_bolsaExterna),
                    'total_desistente': json.dumps(total_desistente),  'total_aprovados': json.dumps(total_aprovados),
                    'total_reprovado': json.dumps(total_reprovado), 'total_conclusao': json.dumps(total_conclusao),
                    'estatistcas': MENU_ESTATISTICA,  'fotos':request.session['salakiaku']}
                template = TEMPLATE_ESTATISTICA["conclusao"]
                return render(request, template, context)
            else:
                conclusao=Formacao_conclusao.objects.select_related('agente').filter(razao_posse=tipo)
                total_conclusao = len(conclusao)
                for k, p in enumerate(conclusao, 1):
                    if p.aproveitamento == 'Desistente':
                        total_desistente += 1
                        if p.razao_posse == 'Bolsa Interna':
                            total_bolsaInterna += 1
                        else:
                            total_bolsaExterna += 1
                    elif p.aproveitamento == 'Reprovado':
                        total_reprovado += 1
                        if p.razao_posse == 'Bolsa Interna':
                            total_bolsaInterna += 1
                        else:
                            total_bolsaExterna += 1
                    elif p.aproveitamento == 'Aprovado':
                        total_aprovados += 1
                        if p.razao_posse == 'Bolsa Interna':
                            total_bolsaInterna += 1
                        else:
                            total_bolsaExterna += 1
                context = {
                    'total_bolsaInterna': json.dumps(total_bolsaInterna), 'total_bolsaExterna': json.dumps(total_bolsaExterna),
                    'total_desistente': json.dumps(total_desistente),  'total_aprovados': json.dumps(total_aprovados),
                    'total_reprovado': json.dumps(total_reprovado), 'total_conclusao': json.dumps(total_conclusao),
                    'estatistcas': MENU_ESTATISTICA,  'fotos':request.session['salakiaku']}
                template = TEMPLATE_ESTATISTICA["conclusao"]
                return render(request, template, context)
    
    context = {
        'form': form, 'estatistcas': MENU_ESTATISTICA,  'fotos':request.session['salakiaku']
        }
    template = TEMPLATE_ESTATISTICA["menu_conclusao"]
    return render(request, template, context)



def retorna_idade(value):
    aux = []
    aux = value.split('-')
    return DATA_ANO - int (aux[0])


#CABEÇARIO DE TODAS AS LISTA NOMINAL
def cabecario_listas():
    dados = []
    buffer = BytesIO()
    #response = HttpResponse(content_type='application/pdf')
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
    angola= Image(logo_angola, width=68, height=73, mask=None, hAlign='CENTER')
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
    

def top_rodape(canvas, doc):
    #p.saveState()
    policia = os.path.join(settings.MEDIA_ROOT, str("policia.png"))
    canvas.drawImage(policia, 1.40 * inch,0.65 * inch, width=40, height=40, mask=None)
    #p.line(0, 0.70 * inch,600, 0.70 * inch)
    canvas.drawString(0.60 *inch, 0.45 * inch,'Comando Províncial de Luanda')

    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2
    )
    ks = random.random() - 2019
    data = 'cpl-salakiaku %s' %(ks)
    qr.add_data(data)
    qr.make(fit=True)
    nome =  str(random.random()) + ".png"
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(settings.MEDIA_ROOT+'/codigo_qr/'+nome)
    canvas.drawImage(settings.MEDIA_ROOT+'/codigo_qr/'+nome, 5.60 * inch,0.65 * inch, width=40, height=40, mask=None)
    canvas.drawString(4.50 *inch, 0.45 * inch,'Salakiaku / Processado por computador')
    


def footer_rodape(canvas, doc):
    pageinfo = "SALAKIAKU"
    canvas.saveState()
    canvas.setFont('Times-Roman',9,'Bloder')
    canvas.drawString(inch, 0.75 * inch, "CPL /  %s" %  pageinfo)
    canvas.restoreState()


# FUNÇÃO QUE VAI CONSTRUIR A PARTE DA TABELA COM TODOS DADOS 
def listar_tabelas(dados, cabeca, lista, doc, response, buffer):
    folha = []
    dados.append(Spacer(1, 20))
    folha = Table([cabeca] + lista)
    folha.setStyle(TableStyle([
            ('GRID', (0, 0), (7, -1), 1.3,  colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
        ]
    ))
    dados.append(folha)

    dados.append(PageBreak())
    doc.build(dados, onFirstPage=top_rodape, onLaterPages=top_rodape)
    response.write(buffer.getvalue())
    buffer.close()



# LISTA NORMAL PONTO PRINCIPAL PATENTE
@login_required
def lista_Transferencia(request):
    form = Lista_Transferencia_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            patente = form.cleaned_data.get('patente')
            genero = form.cleaned_data.get('genero')
            titulo = form.cleaned_data.get('titulo')
            data = form.cleaned_data.get('data')
            data_final = form.cleaned_data.get('data_final')
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
            cabeca = ""
            lista = []
            if genero =='Ambos':
                cabeca = ('AGENTE Nº', 'NOME', 'GENERO', 'PROVINCIA', 'TELEFONE', 'PATENTE') 
                if data < data_final and data_final:
                    lista = [(p.agente.numero_agente, p.agente.pessoa.nome,  p.agente.pessoa.genero, p.agente.pessoa.provincia, p.agente.pessoa.telefone, p.agente.patente)
                    for cont, p in enumerate(Transferencia.objects.select_related('agente').filter(agente__patente=patente,data_entrada__range=(data, data_final)), 1)]
                elif data:
                    lista = [(p.agente.numero_agente, p.agente.pessoa.nome,  p.agente.pessoa.genero, p.agente.pessoa.provincia, p.agente.pessoa.telefone, p.agente.patente)
                    for cont, p in enumerate(Transferencia.objects.select_related('agente').filter(agente__patente=patente,data_entrada__contains=data[:-3]), 1)]
                else:
                    lista = [(p.agente.numero_agente, p.agente.pessoa.nome,  p.agente.pessoa.genero, p.agente.pessoa.provincia, p.agente.pessoa.telefone, p.agente.patente)
                    for cont, p in enumerate(Transferencia.objects.select_related('agente').filter(agente__patente=patente), 1)]
            else:
                cabeca = ('AGENTE Nº', 'NOME',  'PROVINCIA', 'TELEFONE', 'DESTINO') 
                if data < data_final and data_final:
                    lista = [(p.agente.numero_agente, p.agente.pessoa.nome,  p.agente.pessoa.provincia, p.agente.pessoa.telefone, p.orgao_destino)
                    for cont, p in enumerate(Transferencia.objects.select_related('agente').filter(agente__pessoa__genero=genero,agente__patente=patente,data_entrada__range=(data, data_final)), 1)]
                elif data:
                    lista = [(p.agente.numero_agente, p.agente.pessoa.nome,  p.agente.pessoa.provincia, p.agente.pessoa.telefone, p.orgao_destino)
                    for cont, p in enumerate(Transferencia.objects.select_related('agente').filter(agente__pessoa__genero=genero,agente__patente=patente,data_entrada__contains=data[:-3]), 1)]
                else:
                    lista = [(p.agente.numero_agente, p.agente.pessoa.nome,  p.agente.pessoa.provincia, p.agente.pessoa.telefone, p.orgao_destino)
                    for cont, p in enumerate(Transferencia.objects.select_related('agente').filter(agente__pessoa__genero=genero,agente__patente=patente), 1)]
            
            listar_tabelas(dados, cabeca, lista, doc, response, buffer)
            return response
    context = {'normal': form, 'fotos':request.session['salakiaku'], 'estatistcas': MENU_ESTATISTICA}
    template = TEMPLATE_ESTATISTICA["transferencia_pdf"]
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
            cabeca = ('AGENTE Nº', 'NOME', 'GENERO', 'NIVEL ACADEMICO', 'CURSO', 'PATENTE') 
            if nivel_academico:
                lista = [( p.numero_agente, p.pessoa.nome, p.pessoa.genero, p.nivel_academico, p.curso, p.patente) 
                for cont, p in enumerate(Agente.objects.select_related('pessoa').filter(nivel_academico=nivel_academico), 1)  if p.patente == patente ]
            
            listar_tabelas(dados, cabeca, lista, doc, response, buffer)
            return response

    context = {'academico': form, 'fotos':request.session['salakiaku'], 'estatistcas': MENU_ESTATISTICA }
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
            data_final = form.cleaned_data.get('data_final')
            descricao = form.cleaned_data.get('descricao')
            data = form.cleaned_data.get('data')
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
            
            cabeca =""
            lista = [] 
            if anticipada:
                cabeca = ('#', 'NOME', 'GENERO', 'DATA NASCIMENTO', 'IDADE', 'REFORMA', 'PATENTE') 
                if data < data_final and data_final:
                    lista = [(cont, p.agente.pessoa.nome, p.agente.pessoa.genero, p.agente.pessoa.data_nascimento, retorna_idade(p.agente.pessoa.data_nascimento),  p.reforma, p.agente.patente)
                    for cont, p in enumerate(Reforma.objects.select_related('agente').filter(agente__patente=patente,reforma=anticipada, data__range=(data, data_final)), 1)]
                elif data:
                    lista = [(cont, p.agente.pessoa.nome, p.agente.pessoa.genero, p.agente.pessoa.data_nascimento, retorna_idade(p.agente.pessoa.data_nascimento),  p.reforma, p.agente.patente)
                    for cont, p in enumerate(Reforma.objects.select_related('agente').filter(agente__patente=patente,reforma=anticipada, data__contains=data[:-3]), 1)]
                else:
                    lista = [(cont, p.agente.numero_agente, p.agente.pessoa.nome, p.agente.pessoa.genero, p.agente.pessoa.data_nascimento, retorna_idade(p.agente.pessoa.data_nascimento),  p.reforma, p.agente.patente)
                    for cont, p in enumerate(Reforma.objects.select_related('agente').filter(agente__patente=patente,reforma=anticipada), 1)]
                
            else:
                cabeca = ('#', 'AGENTE Nº', 'NOME', 'GENERO', 'DATA NASCIMENTO', 'IDADE', 'PATENTE') 
                if data < data_final and data_final:
                    lista = [(cont, p.agente.numero_agente, p.agente.pessoa.nome, p.agente.pessoa.genero, p.agente.pessoa.data_nascimento, retorna_idade(p.agente.pessoa.data_nascimento), p.agente.patente)
                    for cont, p in enumerate(Reforma.objects.select_related('agente').filter(agente__patente=patente,data__range=(data, data_final)), 1)]
               
                elif data:
                    lista = [(cont, p.agente.numero_agente, p.agente.pessoa.nome, p.agente.pessoa.genero, p.agente.pessoa.data_nascimento, retorna_idade(p.agente.pessoa.data_nascimento), p.agente.patente)
                    for cont, p in enumerate(Reforma.objects.select_related('agente').filter(agente__patente=patente,data__startswith=data[:-3]), 1)]
               
                else:
                    lista = [(cont, p.agente.numero_agente, p.agente.pessoa.nome, p.agente.pessoa.genero, p.agente.pessoa.data_nascimento, retorna_idade(p.agente.pessoa.data_nascimento), p.agente.patente)
                    for cont, p in enumerate(Reforma.objects.select_related('agente').filter(agente__patente=patente), 1)]

            listar_tabelas(dados, cabeca, lista, doc, response, buffer)
            return response

    context = {'reforma': form, 'fotos':request.session['salakiaku'], 'estatistcas': MENU_ESTATISTICA }
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
            data = form.cleaned_data.get('data')
            data_final = form.cleaned_data.get('data_final')
            descricao = form.cleaned_data.get('descricao')
            #  aque e onde começa a criação do pdf
            response = HttpResponse(content_type='application/pdf')
            nome = response['Content-Disposition'] = 'inline; filename={}.pdf'.format(titulo)
            #nome = response['Content-Disposition'] = 'attachment; filename={}.pdf'.format(titulo)
            
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
                cabeca = ('#', 'Nª AGENTE', 'NOME', 'GENERO', 'DATA', 'INVALIDEZ', 'PATENTE') 
                if data < data_final and data_final:
                    lista = [(cont, p.agente.numero_agente, p.agente.pessoa.nome, p.agente.pessoa.genero, p.data_oucorrencia, p.tipo_invalidez, p.agente.patente) 
                    for cont, p in enumerate(Baixa.objects.select_related('agente').filter(motivo_baixa=motivo, data_entrada__range=(data, data_final)), 1) ]
                elif data:
                    lista = [(cont, p.agente.numero_agente, p.agente.pessoa.nome, p.agente.pessoa.genero, p.data_oucorrencia, p.tipo_invalidez, p.agente.patente) 
                    for cont, p in enumerate(Baixa.objects.select_related('agente').filter(motivo_baixa=motivo, data_entrada__startswith=data[:-3]), 1) ]
                else:
                    lista = [(cont, p.agente.numero_agente, p.agente.pessoa.nome, p.agente.pessoa.genero,  p.data_oucorrencia, p.tipo_invalidez, p.agente.patente) 
                    for cont, p in enumerate(Baixa.objects.select_related('agente').filter(motivo_baixa=motivo), 1) ]
            listar_tabelas(dados, cabeca, lista, doc, response, buffer)
            #print(nome[21:])
           
            #FileResponse(response, as_attachment=True, filename='{}.pdf'.format(titulo))
            #context = {'response':nome[21:], 'fotos':request.session['salakiaku'], 'estatistcas': MENU_ESTATISTICA }
            #return render(request, 'estatistica/visualizar_pdf.html', context) 
            return response

    context = {'baixa': form, 'fotos':request.session['salakiaku'], 'estatistcas': MENU_ESTATISTICA }
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
            data = form.cleaned_data.get('data')
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
                if data is not None:
                    lista = [(cont, p.agente.pessoa.nome, p.data, p.motivo, p.pena, p.agente.patente) 
                    for cont, p in enumerate(Disciplina.objects.select_related('agente').filter(motivo=motivo, data__startswith=data[:-3]), 1) ]
                else:
                    lista = [(cont, p.agente.pessoa.nome, p.data, p.motivo, p.pena, p.agente.patente) 
                    for cont, p in enumerate(Disciplina.objects.select_related('agente').filter(motivo=motivo), 1) ]
                    
            listar_tabelas(dados, cabeca, lista, doc, response, buffer)
            return response

    context = {'disciplia': form, 'fotos':request.session['salakiaku'], 'estatistcas': MENU_ESTATISTICA }
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
            data = form.cleaned_data.get('data')
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
                    cabeca = ('#', 'Nª AGENTE', 'NOME', 'PAIS', 'BOLSA', 'CURSO', 'PATENTE')
                    if data is not None:
                        lista = [(cont, p.agente.numero_agente, p.agente.pessoa.nome, p.pais, p.razao_posse,p.curso, p.agente.patente) 
                        for cont, p in enumerate(Selecionado_formacao.objects.select_related('agente').filter(data_entrada__startswith=data[:-3]), 1) ]
                    else:
                        lista = [(cont, p.agente.numero_agente, p.agente.pessoa.nome, p.pais, p.razao_posse,p.curso, p.agente.patente) 
                        for cont, p in enumerate(Selecionado_formacao.objects.select_related('agente').all()) ]
                else:
                    cabeca = ('#', 'NOME', 'PAIS', 'BOLSA', 'CURSO', 'APROVEITAMENTO', 'PATENTE') 
                    if data is not None and tipo:
                        lista = [(cont, p.agente.pessoa.nome, p.pais, p.razao_posse, p.curso, p.aproveitamento, p.agente.patente) 
                        for cont, p in  enumerate(Formacao_conclusao.objects.select_related('agente').filter(aproveitamento=tipo, data_conclusao__endswith = ano).all(), 1) ]
                    else:
                        lista = [(cont, p.agente.pessoa.nome, p.pais, p.razao_posse, p.curso, p.aproveitamento, p.agente.patente) 
                        for cont, p in  enumerate(Formacao_conclusao.objects.select_related('agente').filter(aproveitamento=tipo).all(), 1) ]
            
            listar_tabelas(dados, cabeca, lista, doc, response, buffer)
            return response

    context = {'formacao': form, 'fotos':request.session['salakiaku'], 'estatistcas': MENU_ESTATISTICA }
    template = TEMPLATE_ESTATISTICA["formacao"]
    return render(request, template, context) 
