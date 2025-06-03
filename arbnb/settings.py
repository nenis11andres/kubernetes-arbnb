from pathlib import Path
import os
from dotenv import load_dotenv
import ldap
from django_auth_ldap.config import LDAPSearch

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-+(c0s0&az+@r3x8bdfeb79o_sn3s7iedm@yfv2&#2p4ccz9yln'
DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "http://andres.work.gd",
    "http://localhost:8000",
    'http://192.168.49.2:30672',
    'http://127.0.0.1:60873',
    "http://a101ff6150481453d897998e75a75c41-871376667.us-east-1.elb.amazonaws.com",

]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios_app',
    'alojamientos_app',
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

ROOT_URLCONF = 'arbnb.urls'

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

WSGI_APPLICATION = 'arbnb.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'arbnb'),
        'USER': os.getenv('DB_USER', 'andresop'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

AUTH_USER_MODEL = 'usuarios_app.Usuario'
LOGIN_REDIRECT_URL = '/mis_alojamientos/'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==========================================
#               CONFIG LDAP
# ==========================================

AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_LDAP_SERVER_URI = "ldap://ldap-service"  # o ldap://ldap si es nombre del contenedor
AUTH_LDAP_BIND_DN = "cn=admin,dc=andres,dc=work,dc=gd"
AUTH_LDAP_BIND_PASSWORD = "admin"  # Usa la real si no es esa

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "ou=usuarios,dc=andres,dc=work,dc=gd",
    ldap.SCOPE_SUBTREE,
    "(uid=%(user)s)"
)

AUTH_LDAP_ALWAYS_UPDATE_USER = True

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    # "email": "mail",  ← Descomenta si tienes el atributo `mail`
}

# ==========================================
