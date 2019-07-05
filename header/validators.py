from django.core.exceptions import ValidationError
import validators
from pessoal_quadro.models import Agente, Pessoa, Nomiacao_Cargo, Baixa, Reforma
from formacao.models import Selecionado_formacao, Formacao_conclusao
from transferencia.models import Transferencia, Troca
from django.contrib import messages
import sweetify
import re
from django.contrib.auth.decorators import login_required
import header





def validar_baixa(request):
    try:
        bix = header.views_core.retorna_numero_agente(request.POST['bi'])
        bx = Baixa.objects.get(agente_id=bix)
        if bx.motivo_baixa == 'Reforma' or bx.motivo_baixa == 'Falecimento':
            #messages.warning(request," Não pode! ja existe uma baixa com as mesma carateristica..")
            foto = str(bx.agente.foto_fardado)
            sweetify.error(request, 'Não pode! ja existe uma baixa com as mesma carateristica!...', imageUrl='../static/asset/img/user.jpg',  persistent='Ok', timer='4000')
            return False
        else:
            return True
    except Exception as e:
        return True



def validar_reforma_anticipada(request):
    try:
        bix = header.views_core.retorna_numero_agente(request.POST['bi'])
        ref = Reforma.objects.get(agente_id=bix)
        if ref.reforma == 'Anticipada':
            messages.warning(request," Não pode! ja existe na reforma..")
            return False
        else:
            return True
    except Exception as e:
        return True



def validar_pedido_transferencia(request):
    try:
        bi = request.POST['bi']
        bix = header.views_core.retorna_numero_agente(bi)
        bis = Transferencia.objects.get(agente_id=bix)
        if bis.id is not None:
            messages.warning("Ja existe uma transferencia a espera com esses dados....")
            return False
    except Transferencia.DoesNotExist:
        return True




def validar_selecionar_formacao(request):
        bi = request.POST['bi']
        id = header.views_core.retorna_numero_agente(bi)
        try:
            seleciona = Selecionado_formacao.objects.get(agente_id=id)
            if seleciona.id is not None:
                #messages.warning(request, 'O agente ja existe na lista selecionado para uma formação, Para continuar deve remover da lista ...')
                sweetify.error(request, 'O agente ja existe na lista, selecionado para uma formação, para continua deve ser removido da lista....', persistent='Ok', timer='6000')
                return False
        except Selecionado_formacao.DoesNotExist:
            return True



def verficar_falecimento(request, value = None):
    try:
        baixa = Baixa.objects.get(agente_id=value)
        if baixa.motivo_baixa == 'Falecimento':
            messages.warning(request, 'Não pode adicionar o agente; O agente ja é falecido')
            return False
        else:
            return True
    except Baixa.DoesNotExist:
        return True
    



def validar_conclusao_formacao(request):
        bi = request.POST['bi']
        #pessoa = Pessoa.objects.get(bi=bi.upper())
        agente = header.views_core.retorna_numero_agente(bi)
        try:
            seleciona = Selecionado_formacao.objects.get(agente_id=agente)
            if seleciona.id is not None:
                return True
        except Selecionado_formacao.DoesNotExist:
            messages.warning(request, 'O agente não existe na lista dos selecionados, não pode ser adicionado a conclusão da formação ...')
            return False



def validar_data_nascimento_igresso_colocacao(request):
    nascimento = request.POST['data_nascimento']
    igresso = request.POST['data_igresso']
    colocacao = request.POST['data_colocacao']
    nascimento = nascimento.split("-")
    igresso = igresso.split("-")
    colocacao = colocacao.split("-")
    igress = int (igresso[0]) - int (nascimento[0])
    if nascimento[0] > igresso[0] or nascimento[0] > colocacao[0]:
        messages.warning(request, ' O ano de nascimento não poder ser maior que ano de igresso, nem ano de Colocação....')
        return False
    elif igresso[0] > colocacao[0] or igress < 18:
        messages.warning(request, ' a data de igresso não é valida pelo ano de Colocação....')
        return False
    elif igress < 18:
        messages.warning(request, ' A data de igresso diz que vc é menor de idade, na data de nascimento....')
        return False
    else:
        return True



def verficar_bi_numero_agente(request):
    try:
        bi = request.POST['bi_id']
        numero_agente = request.POST['numero_agente_id']
        pessoa = Pessoa.objects.get(bi=bi)
        if pessoa.bi is not None:
            agente = Agente.objects.get(numero_agente=numero_agente)
            if agente.pessoa_id == pessoa.id:
                return True
            else:
                messages.warning(request, ' O Bi e o numero de agente não pertence a mesma pessoa...')
                return False
    except Pessoa.DoesNotExist:
        messages.warning(request, ' Não existe agente com esse numero de bi e numero de agente...')
        return False



#FUNÇÃO QUE VALIDA SE O BI EXISTE E RETORNA ERRO SE EXISTIR CASO CONTRAIO TRUE
def consultar_bi(value):
    try:
        bi = Pessoa.objects.get(bi=value.upper())
        if bi.bi is not None:
            raise ValidationError("Ja existe agente com esse numero de bi no sistema ")
            #return False
    except Pessoa.DoesNotExist:
        return True


#FUNÇÃO QUE VALIDA SE O BI OU NIP SE EXISTE E RETORNA TRUE SE EXISTE , CASO CONTRARIO ERRO
def consultar_bi_existe(value):
    try:
        bis = Pessoa.objects.get(bi=value.upper())
        if bis.bi is not None:
            return True
    except Pessoa.DoesNotExist:
        try:
            agente = Agente.objects.get(nip=value)
            if agente.nip is not None:
                return True
        except Agente.DoesNotExist:
            try:
                b = Pessoa.objects.filter(bi=value.upper())
                if b is not None:
                    return True
            except Pessoa.DoesNotExist:
                try:
                    agente = Agente.objects.filter(nip=value)
                    if len(agente) >  0:
                        return True
                except Agente.DoesNotExist:
                    raise ValidationError("Numero do Nip ou Bi, Não existe....")



def consultar_bi_True_False(value):
    try:
        bis = Pessoa.objects.get(bi=value.upper())
        if bis.bi is not None:
            return (True, bis.data_nascimento)
    except Pessoa.DoesNotExist:
        return (False, None)




#@login_required
def consultar_numero_agente(value):
    try:
        ng = Agente.objects.get(numero_agente=value)
    except Agente.DoesNotExist:
        raise ValidationError(" Não existe agente com esse numero no sistema.!")



#@login_required
def validar_comprimento_4(value):
    if value is None or len(value) < 4:
        raise ValidationError(
            ('Não é valido, informa um nome valido'),
            code='invalid',
        )


#@login_required
def validar_email(value):
    if not validators.email(value):
        raise ValidationError(
            ('Não é valido, informa um email valido'),
            code='invalid',
        )


#função que esta validar o BI e o nip do agente
def validar_bi(value):
    try:
        numero = 0
        letra = 0
        xl = 0
        prog = re.compile(".")
        bi = re.findall(prog, value)
        if len(value) == 14:
            while xl < len(bi):
                if bi[xl].isdigit():
                    numero = numero + 1
                else:
                    letra = letra + 1
                xl = xl + 1
            nove = bi[9]
            deze = bi[10]
            if len(bi) != 14 or letra != 2 or numero != 12:
                raise ValidationError(
                    ('O numero do Bi não é valido, são 14 digtos incluindo 2 letra '),
                )
            elif not nove.isalpha() or not deze.isalpha():
                raise ValidationError(
                    ('O numero do Bi não é valido, são 14 digtos incluindo 2 letra '),
                )
        else:
            while xl < len(bi):
                if bi[xl].isdigit():
                    numero += numero
                else:
                    if len(value) > 2 and len(value) < 9:
                        x = 0
                    else:
                        raise ValidationError(
                            ('O numero de indentificação não é valido..'),
                        )
                        break
                xl = xl + 1
    except IndexError:
        raise ValidationError(
                ('O numero do Bi não é valido.! erro'),
            )


def validar_comprimento_3(value):
    if len(value) < 3:
        raise ValidationError(
            'Não é valido, o tamanho é muito curto'
        )


def validar_numeros(value):
    if not value.isnumeric():
        raise ValidationError(
            'Não é valido, digita numeros validos'
        )


def validar_string(value):
    sf = value.join(" ")
    if value.isdigit():
        raise ValidationError(
            'Não é valido, digita apenas letras'
        )


#VALIDAR CAIXA SOCIAL   
def validar_numero_caixa_social(value):
    try:
        valor = Agente.objects.get(numero_caixa_social=value)
        if valor.numero_caixa_social is not None:
            raise ValidationError(" o numero da caixa social ja existe")
    except Agente.DoesNotExist:
        return True


# VALIDAR O REGISTO DE NOMIAÇÃO
def verficar_id_nomiacao(request):
    try:
        bi = request.POST['bi']
        pessoa = Pessoa.objects.get(bi=bi)
        if pessoa.id is not None:
            nomi = Nomiacao_Cargo.objects.get(agente_id=pessoa.id)
            if nomi.id is not None:
                #messages.warning(request, 'Ja existe uma nomiação no sistema deste agente!.. Apenas actualiza ou elimina o registo...')
                return (False, nomi)
            else:
                return (True, None)
    except Exception as e:
        try:
            agente = Agente.objects.get(nip=bi)
            if agente.agente_id is not None:
                nomi = Nomiacao_Cargo.objects.get(agente_id=agente.id)
                if nomi.id is not None:
                    return (False, nomi)
            else:
                return (True, None)
        except Exception as e:
            return (True, None)
