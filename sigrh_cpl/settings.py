"""
SALEKIAKU -> TRABALHA O QUE É TEU OU ACREDITA NO QUE TEU...
SALAKIAKU
For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.utils import timezone
from datetime import date
import datetime
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kg(c4!q-+z16p%notic5v7%db1fwh0_-j19kh)@23-m072_h^t'


ALLOWED_HOSTS = ['salakiaku.com','www.salakiaku.com','127.0.0.1','192.168.43.159']
#SECURE_PROXY_SSL_HEADER =('HTTP_X_FORWARDED_PROTO', 'https')
#MODULOS DE SEGURANÇA PARA REQUEST. BASTA ATIVAR

#SECURE_SSL_REDIRECT = True
#SECURE_BROWSER_XSS_FILTER = True
#CSRF_COOKIE_NAME = 'salakiaku'
#SESSION_COOKIE_SECURE = True
#Se deve usar o HTTPOnlysinalizador no cookie da sessão. Se isso estiver definido como True, 
# o JavaScript do lado do cliente não poderá acessar o cookie da sessão.
#SESSION_COOKIE_HTTPONLY = True
#SESSION_EXPIRE_AT_BROWSER_CLOSE = True

#CSRF_COOKIE_SECURE  = True
X_FRAME_OPTIONS = 'DENY'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

TEMPLATE_DEBUG = True

APPEND_SLASH = True



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sessions.backends.signed_cookies',
    'sweetify',
    'header',
    'pessoal_quadro',
    'utilizador',
    'transferencia',
    'formacao',
    'documentacao',
    'estatistica',
    'chartjs',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'sigrh_cpl.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sigrh_cpl.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'salakiaku',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
        'autocommit': True,
    },
    }
}

#acrecentado  para uso no algoritmo das senhas
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'pt-PT'
LANGUAGES = (
    ('pt', u'Português'),
    ('en-us', u'English (US)'),
    ('de', u'Deutsch'),
    ('en-gb', u'English (UK)'),
    ('es', u'Español'),
    ('fr', u'Français'),
    
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
#STATIC_ROOT = '{}/static'.format(BASE_DIR)
MEDIA_ROOT = '{}/media'.format(BASE_DIR)
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
LOGIN_REDIRECT_URL = '/login/' 
LOGOUT_REDIRECT_URL = '/'

# Aque é onde esto a pegar a hora e as datas que esto a usar para alguns casos 
DATE_FORMAT = date.today()
DATA_ANO = timezone.now().year
DATA_MES = timezone.now().month
DATA_HORA_ZONA = timezone.now()
DATE_INPUT_FORMATAR = ('%d/%m/%Y')

