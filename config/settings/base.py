import os
from decouple import config
from environ import Path


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__) - 3


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
]


# Third Party apps
INSTALLED_APPS += [
    'rest_framework',
    'corsheaders',
    'django_celery_beat',
    'django_celery_results',
    'phonenumber_field',
    'taggit',
    'paypal.standard.ipn',
    'django_social_share',
    'storages',
]


# Project apps
INSTALLED_APPS += [
    'accounts.apps.AccountsConfig',
    'shared.apps.SharedConfig',
    'themes.apps.ThemesConfig',
    'wishlist.apps.WishlistConfig',
    'cart.apps.CartConfig',
    'checkout.apps.CheckoutConfig',
    'contact.apps.ContactConfig',
    'about.apps.AboutConfig',
    'policy.apps.PolicyConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# MYSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT')
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Addis_Ababa'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Custom Auth User Model
AUTH_USER_MODEL = 'accounts.CustomUser'


# Cors Headers
CORS_ORIGIN_ALLOW_ALL = True


# Static
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Default Admin Account
DEFAULT_ADMIN_EMAIL = config('ADMIN_EMAIL')
DEFAULT_ADMIN_PASSWORD = config('ADMIN_PASSWORD')
DEFAULT_ADMIN_FIRST_NAME = config('ADMIN_FIRST_NAME', '')
DEFAULT_ADMIN_LAST_NAME = config('ADMIN_LAST_NAME', '')


# Project Name
PROJECT_NAME = 'Art Bootstrap'

# Social Media Links
FACEBOOK_URL = 'https://www.facebook.com/artbootstrap'
TWITTER_URL = 'https://twitter.com/ArtBootstrap'
INSTAGRAM_URL = 'https://instagram.com/artbootstrap'
PINTEREST_URL = 'https://pinterest.com/artbootstrap'


# Celery
CELERY_BROKER_URL = config('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = config('CELERY_BROKER_URL')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE


# Start-up fixtures
FIXTURES = ['categories', 'technology']


# Environment
ENVIRONMENT = config('ENVIRONMENT')


# Paypal
PAYPAL_CURRENCY_CODE = 'USD'


# Sendgrid
SENDGRID_API_KEY = config('SENDGRID_API_KEY')
