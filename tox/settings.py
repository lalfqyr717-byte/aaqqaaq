import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('TOX_SECRET_KEY', 'django-insecure-4rc1h-=_3*78&qadbxka2(edjn*lld_t4^3-t(r!7^+kv=ns@+')
DEBUG = os.environ.get('TOX_DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.environ.get('TOX_ALLOWED_HOSTS', '127.0.0.1,localhost,moq.up.railway.app').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
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

ROOT_URLCONF = 'tox.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'tox.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ar-iq'
TIME_ZONE = 'Asia/Baghdad'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.environ.get('TOX_STATIC_ROOT', BASE_DIR / 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / 'assets']

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

CSRF_TRUSTED_ORIGINS = [origin for origin in os.environ.get('TOX_CSRF_TRUSTED_ORIGINS', '').split(',') if origin]

if not DEBUG:
    SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', 'False') == 'True'
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'False') == 'True'
    CSRF_COOKIE_SECURE = os.environ.get('CSRF_COOKIE_SECURE', 'False') == 'True'
    SECURE_HSTS_SECONDS = int(os.environ.get('SECURE_HSTS_SECONDS', '0'))
    SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get('SECURE_HSTS_INCLUDE_SUBDOMAINS', 'False') == 'True'
    SECURE_HSTS_PRELOAD = os.environ.get('SECURE_HSTS_PRELOAD', 'False') == 'True'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'