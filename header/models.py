from django.db import models
from django.contrib.auth.models import User
from pessoal_quadro.models import Pessoa, Agente


class Codigo(models.Model):
    cadastro = models.CharField(max_length=100,)
    atualizar = models.CharField(max_length=100)
    eliminar = models.CharField(max_length=100)
    listar = models.CharField(max_length=50)
    data = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % (self.id)
