from django.db import models
from django.contrib.auth.models import User




class Previlegio(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.id)
