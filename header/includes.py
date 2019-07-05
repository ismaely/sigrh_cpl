from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, HttpRequest, Http404, HttpResponse, FileResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from django.core import serializers
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from passlib.hash import pbkdf2_sha256
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.loader import get_template
from django.contrib.auth.models import User
from http import cookies
import json
import re
import cv2
import base64
import random
from django.template import Context, loader
from django.db.models import Count

from sigrh_cpl.settings import (DATA_ANO, DATA_MES, DATE_FORMAT, DATA_HORA_ZONA, MEDIA_ROOT, MEDIA_URL,
 STATICFILES_DIRS, STATIC_URL, DATE_INPUT_FORMATAR, MAX_UPLOAD_SIZE, CONTENT_TYPES)
import sweetify
#biblioteca para cria PDF
import os
from io import BytesIO
import reportlab
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Line
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, cm, letter, landscape
from reportlab.platypus import (Image, PageBegin, PageBreak, Paragraph, Table, TableStyle, SimpleDocTemplate,
 Spacer, NextPageTemplate, Frame, PageTemplate)
from reportlab.rl_config import defaultPageSize
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from django.conf import settings
from django.urls import path

#DOCUMENTAÇÃO
from documentacao.models import Documento
from documentacao.forms import DocumentoForm, ConsultarDocumentoForms
import documentacao

#UTILIZADOR
from utilizador.forms import UtilizadorForm, LoginForm, Troca_senhaPadrao_Form


#HEADER O SEGUNDO CORAÇÃO DA APLICAÇÃO
from header.models import Codigo
from header.rotas import(TEMPLATE_UTILIZADOR, TEMPLATE_PESSOAQUADRO, TEMPLATE_DOCUMENTO, TEMPLATE_FORMACAO, 
TEMPLATE_ESTATISTICA, TEMPLATE_TRANSFERENCIA)
from header.opcoesModel import ( MENU_PESSOAL_QUADRO, MENU_DOCUMENTO, MENU_FORMACAO, MENU_ESTATISTICA, MENU_TRANSFERENCIA, MENU_PESSOAL_QUADRO, MENU_PERFIL,
CARGOS_POLICIAL, PENAS_DISCIPLINAR, AREAS_FORMACAO , Mecanica, Electricidade, Construcao_Civil, Informatica, Administracao, Saude,
CIENCIAS_SOCIAIS, SAUDE, DIREITO, ECONOMIA, LETRAS, ENGENHARIA, CIENCIA, BENGO, BENGUELA, BIE, CABINDA, CUANDO_CUBANGO, CUNENE, HUAMBO, HUILA, CUANZA_NORTE, CUANZA_SUL, LUANDA, 
LUNDA_NORTE, LUNDA_SUL, MALANJE, MOXICO, NAMIBE, UIGE, ZAIRE)
from header.validators import( verficar_bi_numero_agente, validar_data_nascimento_igresso_colocacao,
verficar_id_nomiacao )
import header



#PESSOAL E QUADRO 
from pessoal_quadro.models import (Pessoa, Agente, Baixa, Despromocao, Feria, Orgao, Reforma,
Nomiacao_Cargo, Patentiamento, Disciplina, Falecimento)
from pessoal_quadro.forms import (PessoaForm, AgenteForm, BaixaForm, DespromocaoForm, FeriaForm,
OrgaoForm, Nomiacao_cargoForm, Atualizar_patenteForm, Reforma_anticipadaForm, DisciplinaForm, FalecimentoForm)
from pessoal_quadro.forms_atualizar import PessoaForm_atualizar, AgenteForm_atualizar, OrgaoForm_atualizar
from pessoal_quadro.views import  cabecarioFicha



#FORMAÇÃO
from formacao.models import Formacao_conclusao, Selecionado_formacao, Presenca
from formacao.forms import SelecionarForm, FormacaoConlusao_Form

#ESTATISTICA
from estatistica.forms import (NivelAcademico_Form, NormalPatente_Form, BaixaLista_Form,
ReformaLista_Form, DisciplinarLista_Form, FormacaoLista_Form)

#TRANSFERENCIA
from transferencia.models import Transferencia, Troca
from transferencia.forms import TransferenciaForm, TrocaForm



