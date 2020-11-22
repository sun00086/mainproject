"""mainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from firstWEB import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/index', views.index),
    path('index/list_all', views.listAll),
    path('index/add_new', views.addnew),
    path('index/find',views.find),
    path('index/result', views.result),
    path('index/login', views.login),
    path('index/register', views.register),
    path('index/register_done', views.register_done),
    path('index/addnew_done', views.addnew_done),
    path('index/content',views.current_content),
    path('index/login_done',views.login_done),


]
