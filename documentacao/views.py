from header.includes import *



@login_required
def area_documentacao(request):
    dados = {'documentos': MENU_DOCUMENTO}
    template = TEMPLATE_UTILIZADOR['doc']
    return render(request, template, dados)



@login_required
def foto_js(request):
    dados = {'documentos': MENU_DOCUMENTO}
    return render(request, 'documentacao/testar.html', dados)



def atualizar_documento(request, id):
    docs = Documento.objects.get(id=id)
    form = DocumentoForm(request.POST or None, instance=docs) 
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Dados atualizado com sucesso!....', button='Ok')
            return HttpResponseRedirect(reverse('documentacao:area-documentacao'))

    dados = {'form': form, 'docs': docs, 'documentos': MENU_DOCUMENTO}
    template = TEMPLATE_DOCUMENTO['registar']
    return render(request, template, dados)




def registar_documento(request):
    form = DocumentoForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return True
    else:
        return False

    """dados = {'form': form, 'documentos': MENU_DOCUMENTO}
    template = TEMPLATE_DOCUMENTO['registar']
    return render(request, template, dados)"""




def consultar_documento(request):
    try:
        form = ConsultarDocumentoForms(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                lista = Documento.objects.filter(categoria=form.cleaned_data.get('categoria'))
                dados = {'form': form, 'listar': lista, 'documentos': MENU_DOCUMENTO}
                template = TEMPLATE_DOCUMENTO['consultar']
                return render(request, template, dados)

    except Documento.DoesNotExist:
        print('erro na consulta de documento')

    dados = {'form': form, 'documentos': MENU_DOCUMENTO}
    template = TEMPLATE_DOCUMENTO['consultar']
    return render(request, template, dados)




def listar_documento():
    try:
        lista = Documento.objects.all()
        return lista

    except Exception as e:
        raise Http404("falha ao listar documento %s" % (e))



def eliminar_documento(request):
    if request.method == 'POST':
        dados = dict()
        cod = []
        cod = request.body.decode('utf-8')
        lista = json.loads(cod)
        codigo = lista['codigo']
        id = lista['id']
        if header.views_core.validar_codigo_eliminar(codigo):
            docs = Documento.objects.get(id=id).delete()
            dados = {
                    'validade': True,
                }
            return JsonResponse(dados) 
        else:
            dados = {
                'validade': False,
            }
            return JsonResponse(dados)
   
