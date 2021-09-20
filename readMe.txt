This is the seed project built with Phthon Django-Rest-Framework. The authentication mode is session. 
This project follow official practice. The next project will go on some innovation.

The Setup Guide for Django Restful Framework From Scratch
1 Install Phthon-v3.7.9

2 Run the following commands to install libraries:
pip install Django djangorestframework requests
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

Run "pip list" command to show the library version:
Django              3.2.7
django-filter       2.4.0
djangorestframework 3.12.4

3 Run the following commands to create the new project:
django-admin startproject DjangoRestProj1
cd DjangoRestProj1

4 Run the following commands to create the new app in the new project:
django-admin startapp blog

5 Modify DjangoRestProj1/settings.py to add INSTALLED_APPS and REST_FRAMEWORK as following:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'blog',
]

#add to your settings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

6 Modify blog/models.py to implement data models.

7 Crate blog/serializers.py to implement serializer for data models.

8 Create blog/permissions.py to assigin permission.

9 Modify blog/views.py to implement restful API.

10 Modify DjangoRestProj1/urls.py to config router.

11 Run the following commands to initial database:
python manage.py makemigrations
python manage.py migrate

12 Run the following command to start the API server:
python manage.py runserver

13 Test with tools, Use chrome to test restful API, Install and use Chrome Extension:PostWoman Http Test.
test case 1, user register:
URL: http://localhost:8000/register
Method:Post
Fotmat:Custom--application/json
JSon: {"username":"ICELEE", "password":"mypass", "name":"icelee"}

test case 2, add blog, you will get error because you haven't logged in:
URL: http://localhost:8000/blogs/
Method:Post
Fotmat:Custom--application/json
JSon: {"title":"My first blog", "body":"Oh Ya, Nice"}

test case 3, user login:
URL: http://localhost:8000/login/
Method:Post
Fotmat:Custom--application/json
JSon: {"username":"ICELEE", "password":"mypass"}

test case 4, add blog, you will get succeeded this time:
URL: http://localhost:8000/blogs/
Method:Post
Fotmat:Custom--application/json
JSon: {"title":"My second blog", "body":"Oh Ya, Nice"}
