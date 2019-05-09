from django import forms
from django.forms import ModelForm
from sigrh_cpl.settings import DATA_ANO, DATA_MES
from header.opcoesModel import (ESTADO_CIVIL, GENERO, PATENTE, MOTIVO_BAIXA, MOTIVO_DESPROMOCAO, MOTIVO_REFORMA,
NIVEL_ACADEMICO, IDADE_LIMITE, NOMIACAO_TIPO, NOMIACAO_CATEGORIA, PROVINCIA, ORGAO_COMANDOS, SUSPENSAO, CARGOS_POLICIAL,
MOTIVO_DISCILINAR, MOTIVO_DISCILINAR, PENAS_DISCIPLINAR, INVALIDEZ)
from header.validators import (consultar_bi_existe, validar_comprimento_4, validar_numero_caixa_social, validar_comprimento_3,
 validar_numeros, validar_string, validar_email, validar_bi, consultar_numero_agente, consultar_bi)
from pessoal_quadro.models import Baixa, Feria, Orgao, Pessoa, Agente, Despromocao, Nomiacao_Cargo, Reforma, Patentiamento, Disciplina



class PessoaForm(ModelForm):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_4, validar_string])
    nome_pai = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_4, validar_string])
    nome_mae = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_4, validar_string])
    data_nascimento = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'data-inputmask': "'mask' : '99/99/9999'"}))
    bi = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control bi_mask'}))
    estado_civil = forms.CharField(max_length=20, widget=forms.Select(choices=ESTADO_CIVIL))
    provincia = forms.CharField(max_length=25, widget=forms.Select(choices=PROVINCIA))
    residencia = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_3])
    casa_numero = forms.CharField(max_length=7, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'class': 'form-control', 'data-inputmask': "'mask' : '(+244) 999-999-999'" }))
    email = forms.EmailField(max_length=80, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_email])
    genero = forms.CharField(max_length=12, widget=forms.Select(choices=GENERO))
    class Meta:
        model = Pessoa
        fields = ['nome', 'nome_pai', 'nome_mae', 'data_nascimento', 'bi', 'estado_civil', 'genero'
                  ,'provincia', 'residencia', 'casa_numero', 'telefone', 'email']

    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')
        data = data_nascimento.split('-')
        ano = DATA_ANO - int (data[0])
        if ano < 18:
            raise forms.ValidationError(" E menor de idade não pode fazer parte da policia")
        else:
            return data_nascimento



class AgenteForm(ModelForm):
    numero_contribuite = forms.CharField(max_length=20, widget=forms.TextInput(attrs={ 'class': 'form-control nif_mask'}), validators=[validar_comprimento_3])
    numero_caixa_social = forms.CharField(max_length=20,  widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_numeros, validar_numero_caixa_social])
    nivel_academico = forms.CharField(max_length=20,  widget=forms.Select(choices=NIVEL_ACADEMICO))
    curso = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_4, validar_string])
    funcao = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_3])
    patente = forms.CharField(max_length=100,  widget=forms.Select(choices=PATENTE))
    categoria = forms.CharField(max_length=100, required=False)
    nip = forms.CharField(max_length=8, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}),)
    numero_agente = forms.CharField(max_length=10,  widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validar_comprimento_3, validar_numeros])
    data_igresso = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'data-inputmask': "'mask' : '99/99/9999'"}))
    foto_fardado = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'hidden', 'class': 'form-control', 'id': 'salva2'}))
    foto_civil = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'hidden', 'class': 'form-control', 'id': 'salva1'}))
    #widget=forms.TextInput(attrs={'type': 'hidden'})
    class Meta:
        model = Agente
        fields = ['numero_contribuite', 'numero_caixa_social', 'nivel_academico', 'curso', 'funcao', 'patente', 'categoria', 'numero_agente', 'nip', 'data_igresso', 'foto_fardado', 'foto_civil']

    # VALIDAR O CAMPO  numero_contribuite
    def clean_numero_contribuite(self):
        numero_contribuite = self.cleaned_data.get('numero_contribuite')
        numero_caixa_social = self.cleaned_data.get('numero_caixa_social')
        try:
            valor = Agente.objects.get(numero_contribuite=numero_contribuite)
            if numero_contribuite == numero_caixa_social:
                raise forms.ValidationError(" o numero de contribuite não pode ser igual a da caixa social")
            elif valor.numero_contribuite is not None:
                raise forms.ValidationError(" o numero de contribuite ja existe")
        except Agente.DoesNotExist:
            return numero_contribuite

    #VALIDAR NUMERO DO AGENTE
    def clean_numero_agente(self):
        numero_agente = self.cleaned_data.get('numero_agente')
        nip = self.cleaned_data.get('nip')
        try:
            valor = Agente.objects.get(numero_agente=numero_agente)
            if numero_agente == nip:
                raise forms.ValidationError(" o numero do agente não pode ser igual ao nip")
            elif valor.numero_agente is not None:
                raise forms.ValidationError(" o numero de agente ja existe")
        except Agente.DoesNotExist:
            return numero_agente



class OrgaoForm(ModelForm):
    bi = forms.CharField(max_length=14, required=False, widget=forms.TextInput(attrs={'class': 'form-control bi_agente'}), validators=[validar_bi])
    orgao_colocacao = forms.CharField(required=False, widget=forms.Select(choices=ORGAO_COMANDOS))
    #localizacao = forms.CharField(max_length=40, required=False, widget=forms.TextInput(attrs={'placeholder': 'Localização'}),)
    data_colocacao = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'data-inputmask': "'mask' : '99/99/9999'"}))
    dispacho = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'data-inputmask': "'mask' : '9999/99'"}))
    #unidade = forms.CharField(max_length=90, required=False, widget=forms.TextInput(attrs={'placeholder': 'Unidade'}))
    class Meta:
        model = Orgao
        fields = ['orgao_colocacao', 'data_colocacao', 'dispacho']



class BaixaForm(ModelForm):
    bi = forms.CharField(max_length=14, required=True, widget=forms.TextInput(attrs={'class': 'form-control bi_agente'}), validators=[validar_bi,consultar_bi_existe])
    data_entrada = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'data-inputmask': "'mask' : '99/99/9999'"}))
    data_oucorrencia = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'data-inputmask': "'mask' : '99/99/9999'"}))
    motivo_baixa = forms.CharField(max_length=60, widget=forms.Select(choices=MOTIVO_BAIXA))
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'length':1000}))
    dispacho = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'data-inputmask': "'mask' : '9999/99'"}))
    tipo_invalidez = forms.CharField(max_length=30, required=False,  widget=forms.Select(choices=INVALIDEZ))
    class Meta:
        model = Baixa
        fields = ['data_entrada', 'data_oucorrencia', 'motivo_baixa', 'descricao', 'dispacho', 'tipo_invalidez']

    



class DespromocaoForm(ModelForm): 
    bi = forms.CharField(max_length=14, required=True, widget=forms.TextInput(attrs={'class': 'form-control, bi_agente'}), validators=[validar_bi,consultar_bi_existe])
    data = forms.CharField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'data-inputmask': "'mask' : '99/99/9999'"}))
    motivo = forms.CharField(max_length=30, widget=forms.Select(choices=MOTIVO_DESPROMOCAO))
    suspensao = forms.CharField(max_length=200, widget=forms.Select(choices=SUSPENSAO))
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'length':2000}))
    dispacho = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'data-inputmask': "'mask' : '9999/99'"}))
    class Meta:
        model = Despromocao
        fields = ['data', 'motivo', 'suspensao', 'descricao', 'dispacho']

    def clean_data(self):
        data = self.cleaned_data.get('data')
        data1 = data.split('-')
        if int (data1[0]) < DATA_ANO:
            raise forms.ValidationError(" A data não é valida, verifica..")
        return data



class FeriaForm(ModelForm):
    numero_agente = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[consultar_numero_agente, validar_comprimento_3, validar_numeros])
    data_inicio = forms.CharField(widget=forms.DateInput(attrs={'class': 'datepicker form-control'}))
    data_fim = forms.CharField(widget=forms.DateInput(attrs={'class': 'datepicker form-control'}))
    situacao = forms.CharField(max_length=30)
    class Meta:
        model = Feria
        fields = ['data_inicio', 'data_fim', 'situacao']



class Nomiacao_cargoForm(ModelForm):
    bi = forms.CharField(max_length=14, required=True, widget=forms.TextInput(attrs={'class': 'form-control bi_agente'}), validators=[validar_bi, consultar_bi_existe])
    cargo = forms.CharField(max_length=200, widget=forms.Select(choices=CARGOS_POLICIAL))
    data = forms.CharField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'data-inputmask': "'mask' : '99/99/9999'"}))
    tipo = forms.CharField(max_length=60, widget=forms.Select(choices=NOMIACAO_TIPO))
    categoria = forms.CharField(max_length=60, widget=forms.Select(choices=NOMIACAO_CATEGORIA))
    dispacho = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'data-inputmask': "'mask' : '9999/99'"}))
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'length':3500}))
    class Meta:
        model = Nomiacao_Cargo
        fields = ['cargo', 'data', 'tipo', 'categoria', 'dispacho', 'descricao']

    def clean_cargo(self):
        cargo = self.cleaned_data.get('cargo')
        if cargo is None:
            raise forms.ValidationError(" Esta campo não pode ser vazio")
        return cargo



class Reforma_anticipadaForm(ModelForm):
    bi = forms.CharField(max_length=14, required=True, widget=forms.TextInput(attrs={'class': 'form-control bi_agente'}), validators=[validar_bi,consultar_bi_existe])
    motivo = forms.CharField(required=True, widget=forms.Select(choices=MOTIVO_REFORMA))
    reforma = forms.CharField(max_length=30, required=False )
    data = forms.CharField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'name': 'date'}))
    dispacho = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'data-inputmask': "'mask' : '9999/99'"}))
    descricao = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control', 'length':3500}))
    class Meta:
        model = Reforma
        fields = ['motivo', 'reforma', 'data', 'dispacho', 'descricao']

    def clean_motivo(self):
        motivo = self.cleaned_data.get('motivo')
        if motivo is None:
            raise forms.ValidationError(" Esta campo não pode ser vazio")
        return motivo



class Busca_IdadeForm(forms.Form):
    categoria = forms.CharField(max_length=20, label="Idade", widget=forms.Select(choices=IDADE_LIMITE, attrs={'type': 'search'}))




class Atualizar_patenteForm(ModelForm):
    bi = forms.CharField(max_length=14, required=True, widget=forms.TextInput(attrs={'class': 'form-control bi_agente'}), validators=[validar_bi])
    patente = forms.CharField(max_length=100, widget=forms.Select(choices=PATENTE))
    dispacho = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'data-inputmask': "'mask' : '9999/99'"}))
    data = forms.CharField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'data-inputmask': "'mask' : '99/99/9999'"}))
    class Meta:
        model = Patentiamento
        fields = ['dispacho', 'data']



class DisciplinaForm(ModelForm):
    bi = forms.CharField(max_length=14, required=True, widget=forms.TextInput(attrs={'class': 'form-control bi_agente'}), validators=[validar_bi,consultar_bi_existe])
    numero_processo = forms.CharField(max_length=30, required=False )
    data = forms.CharField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'name': 'date'}))
    motivo = forms.CharField(required=True, widget=forms.Select(choices=MOTIVO_DISCILINAR))
    pena = forms.CharField(required=True, widget=forms.Select(choices=PENAS_DISCIPLINAR))
    dispacho = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'data-inputmask': "'mask' : '9999/99'"}))
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'length':3500}))
    arquivo = forms.ImageField(required=False)
    class Meta:
        model = Disciplina
        fields = ['numero_processo', 'data', 'motivo', 'pena',  'dispacho', 'descricao', 'arquivo']

    


class BiForm(forms.Form):
    #patente = forms.CharField(max_length=100, widget=forms.Select(choices=PATENTE))
    bi = forms.CharField(max_length=14, required=True, validators=[validar_bi])


