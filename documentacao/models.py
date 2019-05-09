from django.db import models
from header.opcoesModel import DOCUMENTO_CATEGORIA
import datetime
from django.template.defaultfilters import filesizeformat
from django.contrib.contenttypes.models import ContentType

# Modelo do Documento.

class Documento(models.Model):
    numero_ordem = models.CharField(max_length=40)
    data_entrada = models.CharField(max_length=20)
    categoria = models.CharField(max_length=60, choices=DOCUMENTO_CATEGORIA)
    descricao = models.CharField(max_length=600)
    arquivo = models.FileField(upload_to="arquivos/%Y/",  blank=True, null=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return "%s" % (self.nome)

