from header.includes import *


def home(request):
    template = header.rotas.TEMPLATE_UTILIZADOR['home']
    return render(request, template)



@login_required(login_url='/login/')
def areas_servico(request):
    dados = {}
    template =  header.rotas.TEMPLATE_UTILIZADOR['areas_servico']
    return render(request, template, dados)



def perfil_utilizador(request):
    try:
        lista = []
        id =0
        #lista = Agente.objects.get(id=int(id))
        dados = {'lista': lista, 'perfil': MENU_PERFIL}
        #template =  header.rotas.TEMPLATE_UTILIZADOR['utilizador_perfil']
        #return render(request, template, dados)
    except Exception as e:
        raise e
    template =  header.rotas.TEMPLATE_UTILIZADOR['utilizador_perfil']
    return render(request, template, dados)
   

def utilizador_home(request):
    dados = {'perfil': MENU_PERFIL}
    template =  header.rotas.TEMPLATE_UTILIZADOR['utilizador_perfil']
    return render(request, template, dados)
 


#views que vai listar utilizador do sistema..
@login_required
def listar_utilizador(request):
    try:
        lista = []
        agente = {}
        lista = User.objects.all()
        for n in lista:
            agente[n.first_name] = Agente.objects.get(id=int(n.first_name))
        context = {'lista': lista, 'agente':agente, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
        template = header.rotas.TEMPLATE_UTILIZADOR['listar']
        
    except Exception as e:
        print("erro na listagem do " + e)
    return render(request, template, context)



@login_required
def ativar_conta(request, id):
    if id > 0:
        user = User.objects.get(id=id)
        user.is_active = 1
        user.save()
        sweetify.sweetalert(request, 'Conta Ativada com sucesso ...', type="success", button='Ok', timer='3600')
        return HttpResponseRedirect(reverse('utilizador:listar'))
    else:
        sweetify.sweetalert(request, 'Falha não foi possivel ...', type="error", button='Ok', timer='3600')
        return HttpResponseRedirect(reverse('utilizador:listar'))


@login_required
def desativar_conta(request, id):
    if id > 0:
        user = User.objects.get(id=id)
        user.is_active = 0
        user.save()
        sweetify.sweetalert(request, 'Conta Desativada com sucesso ...', type="success", button='Ok', timer='3600')
        return HttpResponseRedirect(reverse('utilizador:listar'))
    else:
        sweetify.sweetalert(request, 'Falha não foi possivel ...', type="error", button='Ok', timer='3600')
        return HttpResponseRedirect(reverse('utilizador:listar'))
    


def eliminar_conta(request, id):
    if id > 0:
        user = User.objects.filter(id=id).delete()
        sweetify.sweetalert(request, 'Conta Eliminada com sucesso...', type="success", button='Ok', timer='3600')
        return HttpResponseRedirect(reverse('utilizador:listar'))
    else:
        sweetify.sweetalert(request, 'Falha não foi possivel ...', type="error", button='Ok', timer='3600')
        return HttpResponseRedirect(reverse('utilizador:listar'))



def redifinir_senha(request, id):
    if id > 0:
        user = User.objects.get(id=id)
        #novo = User.objects.create_user(username=user.nome,first_name=user.agente.id,last_name=0, email=user.categoria,password=header.views_core.SENHA_PADRAO)
        user.set_password(header.views_core.SENHA_PADRAO)
        user.save()
        sweetify.sweetalert(request, 'Senha Alterada com sucesso...', type="success", button='Ok', timer='3600')
        return HttpResponseRedirect(reverse('utilizador:listar'))
    else:
        sweetify.sweetalert(request, 'Falha não foi possivel alterar...', type="error", button='Ok', timer='3600')
        return HttpResponseRedirect(reverse('utilizador:listar'))



#FUNÇÃO QUE VAI RECEBER A A NOVA SENHA, PARA ALTERAR A SENHA PADRÃO
def alterar_senha_padrao(request, id):
    form = Troca_senhaPadrao_Form(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            senha = form.cleaned_data.get('senhaNova')
            user = User.objects.get(id=id)
            user.set_password(senha)
            user.last_name = 1
            user.save()
            return HttpResponseRedirect(reverse('utilizador:login'))
        else:
            form = Troca_senhaPadrao_Form(None)
            template = header.rotas.TEMPLATE_UTILIZADOR['troca_padrao']
            return render(request, template, {'form': form, 'id': id})

    
    template = header.rotas.TEMPLATE_UTILIZADOR['troca_padrao']
    return render(request, template, {'form': form, 'id': id})
            


#views que vai adicionar utilizador no sistema, a conta pode ser criada com bi o numero de agente
@login_required
def adicionar_Utilizador(request):
    form = UtilizadorForm(request.POST or None)
    nome = ""
    agente = ""
    pessoa = ""
    todos = []
    if request.method == 'POST':
        if form.is_valid():
            categoria = form.cleaned_data.get('categoria')
            bi_nip =form.cleaned_data.get('bi')
            senha = header.views_core.SENHA_PADRAO
            troca_senha = 0
            if len(bi_nip) == 14:
                try:
                    pessoa = Pessoa.objects.get(bi=bi_nip)
                    agente = Agente.objects.get(id=pessoa.id)
                except Exception as e:
                    messages.warning(request, 'O Numero não é valido..')
                    dados = {'form': form, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
                    template = header.rotas.TEMPLATE_UTILIZADOR['utilizador']
                    return render(request, template, dados)
                todos = pessoa.nome.split(' ')
                nome = todos[0]
                total = len(todos)
                for index, item in enumerate(todos, start=1):
                    quantos = nome.count('.', 0, len(nome))
                    if quantos == 0:
                        nome +="."
                    elif index == total:
                        nome = todos[0].lower()
                        nome +="."
                        nome +=todos[1].lower().lower()
                        try:
                            utilizador = User.objects.get(username=nome)
                            if utilizador.id is not None:
                                nome = todos[0].lower()
                                nome +="."
                                nome += str(agente.numero_agente)
                                user = User.objects.create_user(username=nome,first_name=agente.id,last_name=troca_senha, email=categoria,password=senha)
                                break
                        except User.DoesNotExist:
                            user = User.objects.create_user(username=nome,first_name=agente.id,last_name=troca_senha, email=categoria,password=senha)
                            break
                    else:
                        nome +=item
                        nome = nome.lower()
                        try:
                            utilizador = User.objects.get(username=nome)
                            if utilizador.id is not None:
                                nome = todos[0].lower()
                                nome +="."
                        except User.DoesNotExist:
                            user = User.objects.create_user(username=nome,first_name=agente.id,last_name=troca_senha, email=categoria,password=senha)
                            break
            else:
                try:
                    agente = Agente.objects.get(nip=bi_nip)
                except Exception as e:
                    messages.warning(request, 'O Numero não é valido..')
                    dados = {'form': form, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
                    template = header.rotas.TEMPLATE_UTILIZADOR['utilizador']
                    return render(request, template, dados)
                pessoa = agente.pessoa.nome      
                todos = pessoa.split(' ')
                nome = todos[0]
                total = len(todos)
                for index, item in enumerate(todos, start=1):
                    quantos = nome.count('.', 0, len(nome))
                    if quantos == 0:
                        nome +="."
                    elif index == total:
                        nome = todos[0].lower()
                        nome +="."
                        nome +=todos[1].lower()
                        try:
                            utilizador = User.objects.get(username=nome)
                            if utilizador.id is not None:
                                nome = todos[0].lower()
                                nome +="."
                                nome += str(agente.numero_agente)
                                user = User.objects.create_user(username=nome,first_name=agente.id,last_name=troca_senha, email=categoria,password=senha)
                                break
                        except User.DoesNotExist:
                            user = User.objects.create_user(username=nome,first_name=agente.id,last_name=troca_senha, email=categoria,password=senha)
                            break
                    else:
                        nome +=item
                        nome = nome.lower()
                        try:
                            utilizador = User.objects.get(username=nome)
                            if utilizador.id is not None:
                                nome = todos[0].lower()
                                nome +="."
                        except User.DoesNotExist:
                            user = User.objects.create_user(username=nome,first_name=agente.id,last_name=troca_senha, email=categoria,password=senha)
                            break
                
            context={'agente':agente, 'nome':nome, 'senha':senha, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
            template = header.rotas.TEMPLATE_UTILIZADOR['sucesso']
            sweetify.sweetalert(request, 'Conta criado com sucesso..', type="success", button='Ok', timer='3600')
            #messages.success(request, 'Conta do Utilizador criado com sucesso...')
            return render(request, template, context)

    
    dados = {'form': form, 'pessoalQuadro': MENU_PESSOAL_QUADRO}
    template = header.rotas.TEMPLATE_UTILIZADOR['utilizador']
    return render(request, template, dados) 



def criptografia(cpyt):
    chave = pbkdf2_sha256.encrypt(cpyt, rounds=120000, salt_size=30)
    return chave




def verfica_password(senha_bd, senha_post):
    if pbkdf2_sha256.verify(senha_post, senha_bd):
        return True
    else:
        return False




#views que vai permitir o usario fazer login no sistema CPL0302 ANTIGA NOVA CPL0203
def login_utilizador(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                lista = []
                senha = form.cleaned_data.get('senha')
                nome = form.cleaned_data.get('nome_utilizador')
                user = authenticate(username=nome,password=senha)
                utilizador = User.objects.get(username=nome)
                if user is not None:
                    if user.is_active and int(utilizador.last_name) == 1:
                        login(request, user)
                        #sta = Agente.objects.filter(id=int(utilizador.first_name))
                        lista = serializers.serialize("json", Agente.objects.filter(id=int(utilizador.first_name)))
                        sofia = json.loads(lista)
                        request.session['salakiaku'] = sofia
                        template = header.rotas.TEMPLATE_UTILIZADOR['areas']
                        return HttpResponseRedirect(reverse(template))
                    else:
                        form = Troca_senhaPadrao_Form(request.POST or None)
                        template = header.rotas.TEMPLATE_UTILIZADOR['troca_padrao']
                        return render(request, template, {'form': form, 'id': utilizador.id})
                    
                elif not utilizador.is_active:
                    messages.warning(request, 'A sua conta esta Desativada...')
                    
                else:
                    messages.warning(request, 'Dados errados do utilizador...')
                    
        except User.DoesNotExist:
            messages.warning(request, 'A conta não existe...')
            
    dados = {'form': form}
    template = header.rotas.TEMPLATE_UTILIZADOR['login']
    return render(request, template, dados)




@login_required
def sair(request):
    try:
        logout(request)
        return HttpResponseRedirect(reverse('utilizador:sair'))
    except Exception as e:
        raise Http404("erro a terminar a sessão %s " % (e))
