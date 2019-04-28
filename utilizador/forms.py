from django import forms
from django.forms import ModelForm
from header.opcoesModel import AREA_TRABALHO, CATEGORIA_USUARIO 
from header.validators import validar_comprimento_4, validar_bi, consultar_bi, consultar_numero_agente, verficar_bi_numero_agente
from pessoal_quadro.models import Pessoa
import header
from django.contrib.auth.models import User



class UtilizadorForm(forms.Form):
    
    categoria = forms.CharField(max_length=20 ,widget=forms.Select(choices=CATEGORIA_USUARIO ))
    bi= forms.CharField(max_length=14, required=True, validators=[validar_bi])
    
    def clean_bi(self):
        try:
            bi = self.cleaned_data.get('bi')
            if len(bi) == 14:
                pessoa = header.views_core.retorna_numero_bi(bi) 
                utilizador = User.objects.get(first_name=pessoa)
                if utilizador.id is not None:
                    raise forms.ValidationError("Ja existe um utilizador com esta conta")
            else:
                agente = header.views_core.retorna_numero_agente_id(bi)
                utilizador = User.objects.get(first_name=agente)
                if utilizador.id is not None:
                    raise forms.ValidationError("Ja existe um utilizador com este Nip")
        except User.DoesNotExist:
            return bi



class LoginForm(forms.Form):
    senha = forms.CharField(max_length=20, label="Senha:", required=True, widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    nome_utilizador = forms.CharField(max_length=70, label="Nome de utilizador:", required=True, widget=forms.TextInput(attrs={'placeholder': 'Nome de utilizador'}))



class Troca_senhaPadrao_Form(forms.Form):
    senhaPadrao = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'password Antiga'}))
    senhaNova = forms.CharField(max_length=20,  required=True, widget=forms.PasswordInput(attrs={'placeholder': 'password Nova'}))
    confirmaSenha = forms.CharField(max_length=20,  required=True, widget=forms.PasswordInput(attrs={'placeholder': 'confirma a nova password'}))

    def clean_senha_padrao(self):
        senhaPadrao = self.cleaned_data.get('senhaPadrao')
        if senhaPadrao != header.views_core.SENHA_PADRAO:
            raise forms.ValidationError("A senha padrão não esta correta")
        else:
            return senhaPadrao
    
    def clean_senhaNova(self):
        senhaNova = self.cleaned_data.get('senhaNova')
        if len(senhaNova) < 7:
            raise forms.ValidationError(" A senha tem que ser maior que 6 caracter")
        elif senhaNova in header.views_core.SENHA_PADRAO_NAOVALIDA:
            raise forms.ValidationError("A senha não pode ser semelhante a senha padrão")
        else:
            return senhaNova

    def clean_confirmaSenha(self):
        senhaNova = self.cleaned_data.get('senhaNova')
        confirmaSenha = self.cleaned_data.get('confirmaSenha')
        if confirmaSenha != senhaNova:
            raise forms.ValidationError(" A senha é diferente da Nova")
        else:
            return confirmaSenha