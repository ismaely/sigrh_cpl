from django.db import models
from pessoal_quadro.models import Agente
from header.opcoesModel import SITUACAO_TRANSFERENCIA, ORGAO_COMANDOS
from sigrh_cpl.settings import DATA_ANO, DATE_FORMAT





class Transferencia(models.Model):
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, parent_link=True)
    orgao_destino = models.CharField(max_length=500, choices=ORGAO_COMANDOS)
    data_entrada = models.CharField(max_length=20)
    #data = models.CharField(max_length=20, null=True, default=DATE_FORMAT)
    dispacho = models.CharField(max_length=20, null=True, default="Sem dispacho")
    motivo = models.TextField(max_length=5000, blank=True, null=True)
    arquivo = models.FileField(upload_to="transferencia/%Y/", blank=True, null=True)
    numero_guia = models.CharField(max_length=10, null=True, default=00)
    situacao = models.CharField(max_length=30, null=True, default="Espera")

    def __str__(self):
        return '%d' % (self.id)



"""class Pedido(models.Model):
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, parent_link=True)
    destino = models.CharField(max_length=100)
    data_entrada = models.CharField(max_length=20,  null=True, default=DATE_FORMAT)
    situacao = models.CharField(max_length=40, blank=True, null=True, default="deferido", choices=SITUACAO_TRANSFERENCIA)
    motivo = models.TextField(max_length=500, blank=True, null=True)
    arquivo = models.FileField(upload_to="transferencia/%Y/", blank=True, null=True)

    def __str__(self):
        return '%d' % (self.id)"""



class Troca(models.Model):
    primeiro_agente = models.ForeignKey(Agente, on_delete=models.CASCADE, parent_link=True, related_name="primeiro_troca")
    segundo_agente = models.ForeignKey(Agente, on_delete=models.CASCADE, parent_link=True, related_name="segundo_troca")
    origem_primeiro = models.CharField(max_length=100, choices=ORGAO_COMANDOS)
    destino_primeiro = models.CharField(max_length=100,  null=True, choices=ORGAO_COMANDOS)
    origem_segundo = models.CharField(max_length=100, null=True )
    destino_segundo = models.CharField(max_length=100, null=True )
    data = models.CharField(max_length=20,  null=True, default=DATE_FORMAT)
    motivo = models.TextField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return '%d' % (self.id)
    