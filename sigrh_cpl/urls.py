"""sigrh_cpl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
# from django.shortcuts import render
from django.conf.urls import (
handler400, handler403, handler404, handler500
)
import utilizador
#from header.views_core import custom_404, custom_500, custom_403, custom_504




urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('utilizador.urls')),
    path('pessoal_quadro/', include('pessoal_quadro.urls')),
    path('transferencia/', include('transferencia.urls')),
    path('formacao/', include('formacao.urls')),
    path('documentacao/', include('documentacao.urls')),
    path('estatistica/', include('estatistica.urls')),
    path('robots.txt/', lambda x: HttpResponse("User-Agent: *\nDisallow", content_type="text/plain"), name="robots_file"),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)



#handler404 = 'utilizador.views.handler404'
#handler500 = 'utilizador.views.handler500'

