from django.db import models
from pessoal_quadro.models import Pessoa, Agente
from header.opcoesModel import APROVEITAMENTO, RAZAO_DA_POSSE, INSTITUICAO, PAIS_PRESPECTIVA, CURSOS_POLICIAL
from sigrh_cpl.settings import DATA_ANO, DATE_FORMAT




""" Modelo selecionado dos que vão fazer Formação."""
class Selecionado_formacao(models.Model):
    pass
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, parent_link=True)
    curso = models.CharField(max_length=900, choices=CURSOS_POLICIAL)
    dispacho = models.CharField(max_length=20, blank=True, null=True, default="Sem despacho")
    data = models.CharField(max_length=40, null=True, default=DATE_FORMAT)
    razao_posse = models.CharField(max_length=40, null=True, default="Bolsa Interna", choices=RAZAO_DA_POSSE)
    instituicao = models.CharField(max_length=900, null=True, default=" ", choices=INSTITUICAO)
    pais = models.CharField(max_length=100, null=True, default="Angola", choices=PAIS_PRESPECTIVA)
    

    def __str__(self):
        return '%d' % (self.id)



""" Modelo da formação dos que terminarm."""
class Formacao_conclusao(models.Model):
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, parent_link=True)
    curso = models.CharField(max_length=900)
    dispacho = models.CharField(max_length=20, blank=True, null=True, default="Sem despacho")
    aproveitamento = models.CharField(max_length=40, blank=True, null=True, default="Não avaliado", choices=APROVEITAMENTO)
    data_conclusao = models.CharField(max_length=20)
    comprovativo = models.FileField(upload_to="formacao/%Y/", blank=True, null=True, default="sem nenhum justificativo")
    razao_posse = models.CharField(max_length=40, null=True, default="Bolsa Interna")
    #ultima_funcao = models.CharField(max_length=40, null=True, default="CPL")
    pais = models.CharField(max_length=40, null=True, default="Angola")
    instituicao = models.CharField(max_length=900)

    def __str__(self):
        return '%d' % (self.id)



""" Modelo que vai marca presença do agente na formação """
class Presenca(models.Model):
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, parent_link=True)
    selecionado= models.ForeignKey(Selecionado_formacao, on_delete=models.CASCADE, parent_link=True)
    data = models.CharField(max_length=20, null=True, default=DATE_FORMAT)

    def __str__(self):
        return '%d' % (self.id)
