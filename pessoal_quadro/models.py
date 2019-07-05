from django.db import models
from header.opcoesModel import ( GENERO, PATENTE, ESTADO_CIVIL, MOTIVO_BAIXA, MOTIVO_DESPROMOCAO, 
NIVEL_ACADEMICO, NOMIACAO_TIPO, NOMIACAO_CATEGORIA, MOTIVO_REFORMA, PROVINCIA, ORGAO_COMANDOS, SUSPENSAO, 
CARGOS_POLICIAL, PENAS_DISCIPLINAR, MOTIVO_DISCILINAR, INVALIDEZ, AREAS_FORMACAO)
from sigrh_cpl.settings import DATE_FORMAT





class Pessoa(models.Model):
    nome = models.CharField(max_length=100,)
    nome_pai = models.CharField(max_length=100, blank=True, null=True, default="--")
    nome_mae = models.CharField(max_length=100, blank=True, null=True, default="--")
    data_nascimento = models.CharField(max_length=20)
    bi = models.CharField(max_length=20, unique=True)
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL)
    genero = models.CharField(max_length=12, choices=GENERO)
    provincia = models.CharField(max_length=25, choices=PROVINCIA)
    residencia = models.CharField(max_length=50, null=True, default="--")
    telefone = models.CharField(max_length=30)
    email = models.EmailField(max_length=60, blank=True, null=True, default="cpl@gmail.com")
    municipio = models.CharField(max_length=30, null=True, default="--")

    def __str__(self):
        return '%s' % (self.bi)



class Agente(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    numero_contribuite = models.CharField(max_length=20)
    numero_caixa_social = models.CharField(max_length=20)
    nivel_academico = models.CharField(max_length=20, choices=NIVEL_ACADEMICO)
    curso = models.CharField(max_length=80, null=True, default="--")
    patente = models.CharField(max_length=60, choices=PATENTE)
    categoria = models.CharField(max_length=100)
    numero_agente = models.IntegerField(unique='true')
    nip = models.CharField(max_length=20, blank=True, null=True, default="--")
    data_igresso = models.CharField(max_length=20)
    foto_fardado = models.FileField(upload_to="foto/", blank=True, null=True, default="user.jpg")
    foto_civil = models.FileField(upload_to="foto/", blank=True, null=True, default="user.jpg")
    area_formacao = models.CharField(max_length=30,  null=True, default="--")

    def __str__(self):
        return '%d' % (self.numero_agente)




class Orgao(models.Model):
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, to_field='id', parent_link=True)
    orgao_colocacao = models.CharField(max_length=60, null=True, default="cpl", choices=ORGAO_COMANDOS)
    data_colocacao = models.CharField(max_length=20,  blank=True, null=True, default=DATE_FORMAT)
    dispacho = models.CharField(max_length=18,  blank=True, null=True, default="Sem despacho")

    def __str__(self):
        return '%d' % (self.id)




class Baixa(models.Model):
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, parent_link=True)
    data_entrada = models.CharField(max_length=20, null=True, default=DATE_FORMAT)
    data_oucorrencia = models.CharField(max_length=20)
    motivo_baixa = models.CharField(max_length=30, choices=MOTIVO_BAIXA)
    descricao = models.CharField(max_length=420, null=True, default="Não descrita")
    dispacho = models.CharField(max_length=18)
    tipo_invalidez = models.CharField(max_length=50, null=True, choices=INVALIDEZ, default="Não descrita")

    def __str__(self):
        return '%d' % (self.id)




class Despromocao(models.Model): 
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, parent_link=True)
    data = models.CharField(max_length=20)
    motivo = models.CharField(max_length=30 )
    suspensao = models.CharField(max_length=500, choices=SUSPENSAO)
    descricao = models.CharField(max_length=1000, null=True, default="#######")
    dispacho = models.CharField(max_length=18, default="Sem despacho")

    def __str__(self):
        return '%d' % (self.id)




class Feria(models.Model):
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, to_field='id', parent_link=True)
    data_inicio = models.CharField(max_length=20)
    data_fim = models.CharField(max_length=20)
    situacao = models.CharField(max_length=70, blank=True, null=True, default="licença de feria")

    def __str__(self):
        return '%d' % (self.id)


class Reforma(models.Model):
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, to_field='id', parent_link=True)
    motivo = models.CharField(max_length=100, blank=True, null=True, default="Outro", choices=MOTIVO_REFORMA)
    reforma = models.CharField(max_length=20, blank=True, null=True, default="sim")
    data = models.CharField(max_length=10, null=True, default=DATE_FORMAT)
    dispacho = models.CharField(max_length=18, null=True, default="Sem despacho")
    descricao = models.CharField(max_length=3500, null=True, default="Sem descrição")

    def __str__(self):
        return '%d' % (self.id)



class Nomiacao_Cargo(models.Model):
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, to_field='id', parent_link=True)
    cargo = models.CharField(max_length=200, choices=CARGOS_POLICIAL)
    data = models.CharField(max_length=20)
    tipo = models.CharField(max_length=100, choices=NOMIACAO_TIPO)
    categoria = models.CharField(max_length=100, choices=NOMIACAO_CATEGORIA)
    dispacho = models.CharField(max_length=18, null=True, default="Sem despacho")
    descricao = models.CharField(max_length=3500, null=True, default="#######")

    def __str__(self):
        return '%d' % (self.id)



class Patentiamento(models.Model):
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, to_field='id', parent_link=True)
    dispacho = models.CharField(max_length=18, null=True, default="Sem despacho")
    data = models.CharField(max_length=20, null=True, default=DATE_FORMAT)




class Disciplina(models.Model):
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, to_field='id', parent_link=True)
    numero_processo = models.CharField(max_length=10)
    data = models.CharField(max_length=20)
    motivo = models.CharField(max_length=4000, choices=MOTIVO_DISCILINAR)
    pena = models.CharField(max_length=800, choices=PENAS_DISCIPLINAR)
    dispacho = models.CharField(max_length=18, null=True, default="Sem despacho")
    descricao = models.CharField(max_length=9500, null=True, default=" ")
    arquivo = models.FileField(upload_to="disciplina/%Y/", blank=True, null=True)

    def __str__(self):
        return '%d' % (self.id)




class Falecimento(models.Model):
    baixa = models.ForeignKey(Baixa, on_delete=models.CASCADE, to_field='id', parent_link=True)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, to_field='id', parent_link=True)
    cimiteiro = models.CharField(max_length=50, null=True, default="--")
    numero_campa = models.CharField(max_length=5, null=True, default="--")
    data_enterro = models.CharField(max_length=20, null=True, default=DATE_FORMAT)

