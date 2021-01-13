from header.includes import *
from pessoal_quadro.models import Pessoa, Agente

# a que teremos o crudo do projecto, que vai fazer solicitando dados no banco de dados


alf = 'abcdefghijklmnopqrstuvxwyz'
numero = '01234567890'
SENHA_PADRAO = 'CPL123'
SENHA_PADRAO_NAOVALIDA = ['cpl123', 'CPL123','123456789','1234567','987654321','12345','cp123']

PATENTENS = [
    'Agente-1ª-Classe',
    'Agente-2ª-Classe',
    'Agente-3ª-Classe',
    '1ª-Subchefe',
    '2ª-Subchefe',
    '3ª-Subchefe',
    'Inspector',
    'Sub-inspetor',
    'Inspector-chefe',
    'Intendente',
    'Superintendente',
    'Sub-comissário',
    'Comissário',
    'Comissário-geral',
    'Comissário-chefe',
]





#FUNÇÃO QUE VAI RETORNA AS CATEGORIAS DAS PATENTE
def categoria_patente(value):
    for idx, dados in enumerate(PATENTENS, start = 1):
        if value == dados and idx >= 1 and idx < 4:
            return 'Classe de Agente'

        elif value == dados and idx >= 4 and idx < 7:
            return 'Classe de subchefe'
       
        elif value == dados and idx >= 7 and idx < 10:
            return 'Classe de oficiais subalterno'

        elif value == dados and idx >= 10 and idx < 12:
            return 'classe de oficiais superiore'

        elif value == dados and idx >= 12 and idx < 16:
            return 'classe de oficiais comissário'




#FUNÇÃO QUE VAI RETORNA O ID DA TABELA PESSOA QUANDO RECEBER O NUMMERO DO BI COMO PARAMETRO
def retorna_numero_bi(value):
   try:
       bi = Pessoa.objects.get(bi=value)
       if bi.id:
           return bi.id
   except Pessoa.DoesNotExist:
       try:
           agente = Agente.objects.get(nip=value)
           return agente.id
       except Agente.DoesNotExist:
           return 0



#função q retorna o id do agente qdo recebe o numero do bi
def retorna_numero_agente(value):
   try:
       if len(value) == 14:
            bi = Pessoa.objects.get(bi=value.upper())
            agente = Agente.objects.get(pessoa_id=bi.id)
            if bi.id is not None and agente.id is not None:
                return agente.id

       elif len(value) > 0 and len(value) < 10:
            try:
                agente = Agente.objects.get(nip=value)
                if agente.nip is not None:
                    return agente.id
            except Agente.DoesNotExist:
                return False

   except Pessoa.DoesNotExist:
       return False



#Função que vai retornaer o bi nip qdo deseja se atualizar dados
def retorna_nip_bi(value):

    try:
        if len(value) == 14:
            pess = Pessoa.objects.get(bi=value.upper())
            if pess.id is not None:
                 return (pess)
        elif len(value) > 0 and len(value) < 10:
            try:
                agente = Agente.objects.get(nip=value)
                if agente.nip is not None:
                    return (agente)
            except Agente.DoesNotExist:
                return False

    except Pessoa.DoesNotExist:
        return False




#função que retorna o numero o id do agente qdo recebe o numero do agente
def retorna_numero_agente_id(value):
    try:
        agente = Agente.objects.get(nip=value)
        if agente.id is not None:
            return agente.id
    except Agente.DoesNotExist:
        try:
            agente = Agente.objects.get(numero_agente=value)
            if agente.id is not None:
                return agente.id
        except Agente.DoesNotExist:
            return False




# função que vai retorna a idade
def retorna_idade(value):
    aux = []
    aux = value.split('-')
    return DATA_ANO - int (aux[0])



#FUNÇÃO QUE VAI GERAR A SENHA, QUANDO CRIAR UM UTILIZADOR
"""def gerar_senha_utilizador():
    cont = 0
    senha = ""
    for cont in range(3):
        k = random.choice(numero)
        senha += k

    for cont in range(3):
        k = random.choice(alf)
        senha += k.upper()

    for cont in range(3):
        k = random.choice(alf)
        senha += k

    return senha"""




#FUNÇÃO QUE VAI GERAR CODIGO DE SEGURANÇA QDO SE DESEJA ALTERAR DADOS SEM PERMISÃO
def gerar_codigo_atualiadr():
    cont = 0
    senha = ""
    for cont in range(2):
        k = random.choice(numero)
        senha += k

    for cont in range(2):
        k = random.choice(alf)
        senha += k

    for cont in range(2):
        k = random.choice(alf)
        senha += k.upper()

    return senha



#FUNÇÃO QUE VAI GERAR CODIGO DE SEGURANÇA QDO SE DESEJA ELIMINAR DADOS SEM PERMISÃO
def gerar_codigo_eliminar():
    cont = 0
    senha = ""
    for cont in range(3):
        k = random.choice(alf)
        senha += k

    for cont in range(3):
        k = random.choice(numero)
        senha += k

    for cont in range(2):
        k = random.choice(alf)
        senha += k

    return senha



#FUNÇÃO QUE VAI GERAR CODIGO DE SEGURANÇA QDO SE DESEJA LISTAR DADOS SEM PERMISÃO
def gerar_codigo_listar():
    cont = 0
    senha = ""
    for cont in range(3):
        k = random.choice(alf)
        senha += k

    for cont in range(3):
        k = random.choice(numero)
        senha += k
    return senha




#FUNÇÃO QUE VAI GERAR CODIGO DE SEGURANÇA QDO SE DESEJA REGISTAR DADOS SEM PERMISÃO
def gerar_codigo_cadastro():
    cont = 0
    senha = ""
    for cont in range(3):
        k = random.choice(alf)
        senha += k.upper()

    for cont in range(3):
        k = random.choice(numero)
        senha += k

    return senha



#VIEWS QUE VAI VALIDAR O CODIGO DE ATUALIZAR QDO UTILIZADOR DIGITA, PARA VER SE E IGUAL.
def validar_codigo_atualizar(value):
        cod = value
        try:
            codigo = Codigo.objects.get(atualizar=cod)
            if codigo.atualizar == cod:
                return True
            else:
                return False
        except Codigo.DoesNotExist:
            return False



#VIEWS QUE VAI VALIDAR O CODIGO DE CADASTRO QUANDO UTILIZADOR DIGITA, PARA VER SE E IGUAL.
def validar_codigo_cadastro(value):
        cod = value
        try:
            codigo = Codigo.objects.get(cadastro=cod)
            if codigo.cadastro== cod:
                return True
            else:
                return False
        except Codigo.DoesNotExist:
            return False



#VIEWS QUE VAI VALIDAR O CODIGO DE ELIMINAR QUANDO UTILIZADOR DIGITA O CODIGO DE SEGURANÇA PARA VER SE E IGUAL.
def validar_codigo_eliminar(value):
        cod = value
        try:
            codigo = Codigo.objects.get(eliminar=value)
            if codigo.eliminar== cod:
                return True
            else:
                return False
        except Codigo.DoesNotExist:
            return False



#FUNÇÃO QUE VAI GERAR NOVO CODIGO DE SEGURANÇA QDO FOR SOLICITADO
def novo_codigo_seguranca():
    codigo = Codigo.objects.first()
    codigo.cadastro = gerar_codigo_cadastro()
    codigo.atualizar = gerar_codigo_atualiadr()
    codigo.eliminar = gerar_codigo_eliminar()
    codigo.listar = gerar_codigo_listar()
    codigo.data=DATE_FORMAT
    codigo.save()
    return True



def prepara_foto(request):
    img = request.POST["foto_civil"]
    img2 = request.POST["foto_fardado"]
    nome = str(DATA_HORA_ZONA).split('.')
    foto = []
    foto2 = []
    inicio = img.find(',')
    imagem = img[inicio+1:]
    inicio2 = img2.find(',')
    imagem2 = img2[inicio2+1:]


    with open("./media/foto/"+ str(nome[0]) + "_" + str(random.random()) + ".png", "wb") as fh:
        fh.write(base64.b64decode(imagem))
        foto = str(fh).split('=')
        um = foto[1].replace(">", '')


    with open("./media/foto/"+ str(nome[0]) + "_" + str(random.random()) + ".png", "wb") as gh:
        gh.write(base64.b64decode(imagem2))
        foto2 = str(gh).split('=')
        dois =  foto2[1].replace(">", '')

    um = um.replace("'", '')
    dois = dois.replace("'", '')
    um = um.split('media/')
    dois = dois.split('media/')
    return { um[1], dois[1]}


#função que vai inserir o codigo de segurança pela primeira vez qdo esta vazio a tabela
def inserir_codigo():
    inserir = Codigo.objects.create(cadastro=gerar_codigo_cadastro(), atualizar=gerar_codigo_atualiadr(), eliminar=gerar_codigo_eliminar(), listar=gerar_codigo_listar(), data=DATE_FORMAT)


def rodape_imagem_Vertical(canvas, doc):
    #logo = os.path.join(settings.MEDIA_ROOT, str('logo/folha_simples.png'))
    #canvas.drawImage(logo, 0, 15, width=580, height=764, mask=None)
    page_num = canvas.getPageNumber()
    #text = "Pagina #%s" % page_num
    #canvas.drawRightString(200*mm, 20*mm, text)
