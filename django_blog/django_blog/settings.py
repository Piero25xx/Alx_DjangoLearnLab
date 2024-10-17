Task Description:
Build upon your initial setup by adding authentication functionalities to your django_blog project. This task involves setting up user registration, login, logout, and a simple profile management system.

Step 1: Set Up User Authentication Views
Authentication Views:
Utilize Django’s built-in authentication views and forms to handle user login and logout. For registration and profile management, custom views will be created.
Extend Django’s UserCreationForm for the registration form to include additional fields like email.
Step 2: Create Templates for Authentication
Templates for User Interactions:
Develop HTML templates for login, registration, logout, and user profile pages. Ensure these templates are styled using the provided CSS.
Templates should include forms for user input and should provide feedback for authentication errors or confirmations.
Step 3: Configure URL Patterns
Authentication URLs:
Define URL patterns in blog/urls.py to handle paths for login (/login), logout (/logout), registration (/register), and profile management (/profile).
Use Django’s path() function and the include() function to organize these URLs efficiently.
Step 4: Implement Profile Management
Profile Management Features:
Develop a view that allows authenticated users to view and edit their profile details. This view should handle POST requests to update user information.
Ensure the user can change their email and optionally extend the user model to include more fields like a profile picture or bio.
Step 5: Test and Secure the Authentication System
Testing and Security:
Thoroughly test the registration, login, logout, and profile editing functionalities to ensure they work correctly and securely.
Ensure that all forms are using CSRF tokens to protect against CSRF attacks.
Passwords should be handled securely using Django’s built-in hashing algorithms.
Step 6: Documentation
Authentication Documentation:
Provide detailed documentation on how the authentication system works, including descriptions of each part of the authentication process and how users interact with it.
Include instructions on how to test each authentication feature.
Deliverables:
Code Files: Include all Python code for the authentication views, forms, and updated models if necessary.
Template Files: Provide all HTML templates related to user authentication.
Documentation: Detailed explanation of the authentication system, including setup instructions and user guides.Task Description:
Build upon your initial setup by adding authentication functionalities to your django_blog project. This task involves setting up user registration, login, logout, and a simple profile management system.

Step 1: Set Up User Authentication Views
Authentication Views:
Utilize Django’s built-in authentication views and forms to handle user login and logout. For registration and profile management, custom views will be created.
Extend Django’s UserCreationForm for the registration form to include additional fields like email.
Step 2: Create Templates for Authentication
Templates for User Interactions:
Develop HTML templates for login, registration, logout, and user profile pages. Ensure these templates are styled using the provided CSS.
Templates should include forms for user input and should provide feedback for authentication errors or confirmations.
Step 3: Configure URL Patterns
Authentication URLs:
Define URL patterns in blog/urls.py to handle paths for login (/login), logout (/logout), registration (/register), and profile management (/profile).
Use Django’s path() function and the include() function to organize these URLs efficiently.
Step 4: Implement Profile Management
Profile Management Features:
Develop a view that allows authenticated users to view and edit their profile details. This view should handle POST requests to update user information.
Ensure the user can change their email and optionally extend the user model to include more fields like a profile picture or bio.
Step 5: Test and Secure the Authentication System
Testing and Security:
Thoroughly test the registration, login, logout, and profile editing functionalities to ensure they work correctly and securely.
Ensure that all forms are using CSRF tokens to protect against CSRF attacks.
Passwords should be handled securely using Django’s built-in hashing algorithms.
Step 6: Documentation
Authentication Documentation:
Provide detailed documentation on how the authentication system works, including descriptions of each part of the authentication process and how users interact with it.
Include instructions on how to test each authentication feature.
Deliverables:
Code Files: Include all Python code for the authentication views, forms, and updated models if necessary.
Template Files: Provide all HTML templates related to user authentication.
Documentation: Detailed explanation of the authentication system, including setup instructions and user guides."""
Django settings for django_blog project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k+qni^4tg@&5+g0au#o7kh&1+%4z99=+og%drs9d+jd4!l)-8!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
     'taggit',

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

ROOT_URLCONF = 'django_blog.urls'
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

WSGI_APPLICATION = 'django_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'piero',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Authentication settings
LOGIN_REDIRECT_URL = '/profile/'  # Redirects users to the profile page after login
LOGOUT_REDIRECT_URL = '/login/'   # Redirects users to login page after logout
LOGIN_URL = '/login/'


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
