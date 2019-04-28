from django.urls import path
from . import views

app_name ='utilizador'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_utilizador, name='login'),
    path('accounts/login/', views.login_utilizador, name='login'),
    path('areas_servico/', views.areas_servico, name='areas-servico'),
    path('sair/', views.sair, name='sair'),
    path('adicionar_utilizador/', views.adicionar_Utilizador, name='adicionar-utilizador'),
    path('perfil_utilizador/', views.perfil_utilizador, name='perfil-utilizador'),
    path('listar_utilizador/', views.listar_utilizador, name='listar'),
    path('ativar_conta/<int:id>/', views.ativar_conta, name='ativar'),
    path('desativar_conta/<int:id>/', views.desativar_conta, name='desativar'),
    path('eliminar_conta/<int:id>/', views.eliminar_conta, name='eliminar'),
    path('redifinir_senha/<int:id>/', views.redifinir_senha, name='redifinir-senha'),
    path('alterar_senha_padrao/<int:id>/', views.alterar_senha_padrao, name='alterar-senha-padrao'),
    path('utilizador_home/', views.utilizador_home, name='home'),
    # EXcel avançado---cpl
]
