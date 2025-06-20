"""
URL configuration for CrudProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from CrudApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('create/',views.create,name='create'),
    path('read/',views.read,name='read'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),

    path('reg/',views.reg,name='reg'),
    path('display/',views.display,name='display'),
    path('up/<int:id>/',views.up,name='up'),
    path('de/<int:id>/',views.de,name='del'),


    path('register/',views.register,name='register'),
    path('signin/',views.signin,name='signin'),

    path('profile/',views.profile,name='profile'),
    path('data/',views.data,name='data'),

    
    path('mail/',views.mail,name='mail'),
    
    path('home/',views.home,name='home'),


]