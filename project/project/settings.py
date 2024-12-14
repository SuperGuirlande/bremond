from pathlib import Path
import environ
import os


BASE_DIR = Path(__file__).resolve().parent.parent

# ENVIRON #
env = environ.Env()
environ.Env.read_env(env_file=str(BASE_DIR / 'project' / '.env'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'main',
    'blog',
    'realisations',
    'message_form',
    'recrutement',
    'tailwind',
    'theme',
    'django_ckeditor_5',
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'project/templates'],
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

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

# TIMEZONE
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

# STATIC & MEDIA #
STATIC_URL = '/static/'
STATICFILES_DIR = [
    BASE_DIR / 'static',
    BASE_DIR / 'main' / 'static',
    BASE_DIR / 'accounts' / 'static',
    BASE_DIR / 'blog' / 'static',
    BASE_DIR / 'recrutement' / 'static',
    ]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# USER MODEL #
AUTH_USER_MODEL = 'accounts.CustomUser'

# LOGIN
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'admin_index'

# EMAIL SETTINGS #
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('SMTP_HOST')
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = env('SMTP_PASS')
DEFAULT_FROM_EMAIL = 'contact@agencecodemaster.com'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# TAILWIND CSS
TAILWIND_APP_NAME = 'theme'
NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"

# CK EDITOR 5
customColorPalette = [
    {
        'color': 'hsl(4, 90%, 58%)',
        'label': 'Red'
    },
    {
        'color': 'hsl(340, 82%, 52%)',
        'label': 'Pink'
    },
    {
        'color': 'hsl(291, 64%, 42%)',
        'label': 'Purple'
    },
    {
        'color': 'hsl(262, 52%, 47%)',
        'label': 'Deep Purple'
    },
    {
        'color': 'hsl(231, 48%, 48%)',
        'label': 'Indigo'
    },
    {
        'color': 'hsl(207, 90%, 54%)',
        'label': 'Blue'
    },
]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],

        },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
        'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                    'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable',],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
            'tableProperties', 'tableCellProperties' ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading' : {
            'options': [
                { 
                    'model': 'paragraph', 
                    'title': 'Paragraph', 
                    'class': 'ck-heading_paragraph' 
                },
                { 
                    'model': 'heading1', 
                    'view': 'h1', 
                    'title': 'Heading 1', 
                    'class': 'ck-heading_heading1' 
                },
                { 
                    'model': 'heading2', 
                    'view': 'h2', 
                    'title': 'Heading 2', 
                    'class': 'ck-heading_heading2' 
                },
                { 
                    'model': 'heading3', 
                    'view': 'h3', 
                    'title': 'Heading 3', 
                    'class': 'ck-heading_heading3' 
                }
            ]
        },
        'fontFamily': {
            'options': [
                'Playfair Display, serif',
                'Arial, sans-serif',
                'Courier New, monospace',
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}

CKEDITOR_5_FILE_UPLOAD_PERMISSION = "any"