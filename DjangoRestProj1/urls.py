"""restProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from blog.views import *

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'blogs',BlogViewSet)

urlpatterns = [
    url(r'^api/',include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api/register',UserRegisterAPIView.as_view()),
    url(r'^api/login',UserLoginAPIView.as_view()),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
