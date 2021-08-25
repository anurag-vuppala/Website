"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from mywebsite.apps.public.views import index
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
import mywebsite

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('mywebsite.apps.public.urls')),
    path("accounts/", include('mywebsite.apps.accounts.urls')),
   
    # path("", views.index, name="index"),
    # path("profile", include('mywebsite.apps.accounts.urls'), name="profile"),
    # # log in
    # path("login",include('mywebsite.apps.accounts.urls'),name="login",),
    # path("logout", include('mywebsite.apps.accounts.urls'), name="logout"),
 
]
