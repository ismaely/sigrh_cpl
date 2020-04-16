from django.urls import path
from . import views
from hashlib import blake2b

app_name ='utilizador'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_utilizador, name='login'),
    path(blake2b(b'accounts/login').hexdigest()+'/', views.login_utilizador, name='login'),
    path(blake2b(b'areas_servico').hexdigest()+'/', views.areas_servico, name='areas-servico'),
    path(blake2b(b'sair').hexdigest()+'/', views.sair, name='sair'),
    path(blake2b(b'adicionar_utilizador').hexdigest()+'/', views.adicionar_Utilizador, name='adicionar-utilizador'),
    path(blake2b(b'perfil_utilizador').hexdigest()+'/', views.perfil_utilizador, name='perfil-utilizador'),
    path(blake2b(b'listar_utilizador').hexdigest()+'/', views.listar_utilizador, name='listar'),
    path(blake2b(b'ativar_conta').hexdigest()+'/<int:id>/', views.ativar_conta, name='ativar'),
    path(blake2b(b'desativar_conta').hexdigest()+'/<int:id>/', views.desativar_conta, name='desativar'),
    path(blake2b(b'eliminar_conta').hexdigest()+'/<int:id>/', views.eliminar_conta, name='eliminar'),
    path(blake2b(b'redifinir_senha').hexdigest()+'/<int:id>/', views.redifinir_senha, name='redifinir-senha'),
    path(blake2b(b'alterar_senha_padrao').hexdigest()+'/<int:id>/', views.alterar_senha_padrao, name='alterar-senha-padrao'),
    path(blake2b(b'alterar_senha_utilizador').hexdigest()+'/<int:id>/', views.alterar_senha_utilizador, name='alterar-senha-utilizador'),
    path(blake2b(b'utilizador_home').hexdigest()+'/', views.utilizador_home, name='home'),
    # EXcel avançado---cpl
]
