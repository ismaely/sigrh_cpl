from django import template
from django.contrib.auth.models import User
from pessoal_quadro.models import Pessoa
from utilizador.models import Previlegio


register = template.Library()


@register.simple_tag
def retornaCategoria(id):
    user = Previlegio.objects.get(id=int(id))
    return '%s' % user.nome
