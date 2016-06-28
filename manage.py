import os
import sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=True,
    ALLOWED_HOSTS=[],
    SECRET_KEY='fuc(668qq@wbj4k!@8=$3fn!1omga1xl!ga(s6miz-dq9bdv$0',
    ROOT_URLCONF='urls',
    INSTALLED_APPS=(
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'users',
    ),
    MIDDLEWARE_CLASSES=(
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'synergy',
            'USER': 'synuser',
            'PASSWORD': 'synergy',
            'HOST': 'localhost',
            'PORT': '',
        }
    },
    STATIC_URL='/static/',
    TEMPLATES=[
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
    ],
    STATICFILES_DIRS=(os.path.join(BASE_DIR, 'static'),)
)

application = get_wsgi_application()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
