import os
from pathlib import Path
from datetime import timedelta
from django.utils.translation import gettext_lazy as _
from core.settings.jazzmin import JAZZMIN_SETTINGS

from dotenv import load_dotenv

load_dotenv()
DEBUG = True
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ['*']

if DEBUG:
    try:
        from .development import *
    except ImportError:
        raise ImportError("Файл development.py не найден")
else:
    try:
        from .production import *
    except ImportError:
        raise ImportError("Файл production.py не найден")

THEME_APPS = [
    "jazzmin",
]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

]

MY_APPS = [
    # приложения
    'app.users',
    'app.pro_activity',
    'app.afisha',
    'app.services',
    'app.page_for_readers',
    'app.activity',
    'app.projects',
    'app.base',
    'app.news',
    'app.supports',
    'app.about_library',
    'app.el_library'
]


LIBRARY_APPS = [
    'modeltranslation',
    "rest_framework",
    "corsheaders",
    'drf_yasg',
    'ckeditor',
    'rest_framework_simplejwt',
    'django_filters',
    'social_django',
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=2),      
    'REFRESH_TOKEN_LIFETIME': timedelta(weeks=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
}


LANGUAGES = [
    ('ru', _('Russian')),
    ('ky', _('Kyrgyz')),
    # ('en', _('English')),

]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'


TRANSLATABLE_MODEL_MODULES = [
    'app.base.models',
    'app.projects.models',
    
]


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),

]

INSTALLED_APPS = [
    *THEME_APPS,
    *DJANGO_APPS,
    *MY_APPS,
    *LIBRARY_APPS,
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'  # URL to jQuery
CKEDITOR_IMAGE_BACKEND = "pillow"  # Путь к пакету Pillow для обработки изображений
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',  # Вы можете настроить свою собственную панель инструментов CKEditor
        'height': 300,
        'width': 800,
    },
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'core.middleware.cors_media_middleware.MediaCORSMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'app.activity.middleware.StatsCountMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]


ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "core.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Bishkek"


USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATIC_URL = "static/"
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/library/library-osh/static'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'nurlanuuulubeksultan@gmail.com'
EMAIL_HOST_PASSWORD = 'dqlqhohdjeewlgdj'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOW_ALL_ORIGINS = True

from corsheaders.defaults import default_methods, default_headers


CORS_ALLOW_HEADERS = list(default_headers)

JAZZMIN_SETTINGS=JAZZMIN_SETTINGS

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'config': {
            'language': 'en',
        },
    },
}

AUTH_USER_MODEL = 'users.User'


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'Frontend/dist/accets'),
# ]

# MEDIA_URL = 'media/'
# MEDIA_ROOT = BASE_DIR / 'media/'


CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    "http://localhost:3000",
    'http://localhost:5173',
    'http://192.168.31.6:5173',
    'https://d3a4-158-181-248-104.ngrok-free.app',
]

CORS_ALLOWED_METHODS = [
    "GET", "POST", 'DELETE', 
]

CORS_ALLOW_HEADERS = [
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    'https://librarygeekspro.webtm.ru',
    'http://192.168.31.6:8000',
    "http://localhost:3000",
    'http://localhost:5173',
    'http://192.168.31.6:5173',
    'https://d3a4-158-181-248-104.ngrok-free.app',
]
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = os.getenv("SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE").split(",")

# SWAGGER_SETTINGS = {
#     'DEFAULT_AUTO_SCHEMA_CLASS': 'your_project.swagger.CustomAutoSchema',
# }

SOCIAL_AUTH_CREATE_USERS = True
SOCIAL_AUTH_ASSOCIATE_BY_EMAIL = True

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)