#coding:utf8
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
"""
Django settings for netfood project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#7%&5kqx5*!568^@+ssz8nevj=g#sju$=r2tym)jjgkog533(e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'menu',
    'cart',
    'order',
    'banner',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'cart.processors.get_cart_by_session',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)

ROOT_URLCONF = 'netfood.urls'

WSGI_APPLICATION = 'netfood.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),  
)
STATIC_URL = '/static/'
MEDIA_URL = '/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload/')

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Netfood Website Manager',
    'HEADER_DATE_FORMAT': 'Y-m-d',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    'MENU':(
        {'app':'auth','label':u'用户管理','icon':'icon-user'},
        {'app':'menu','label':u'菜单管理','icon':' icon-shopping-cart'},
        {'app':'banner','label':u'广告管理','icon':'icon-picture'},
        {'app':'order','label':u'订单管理','icon':'icon-time'},
        {'label': u'订单监控', 'icon':'icon-eye-open', 'url': '/order/'},
    ),
    # 'SEARCH_URL': '/admin/auth/user/',

    'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),


    # misc
    'LIST_PER_PAGE': 10
}