"""NAT_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from adminsys import views as adminsys_views
from index import views as index_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminsys/index', adminsys_views.adminsys),
    path('adminsys/sys404', adminsys_views.sys404),
    path('adminsys/modifyPassword',adminsys_views.modify_password),
    path('adminsys/accountInformation',adminsys_views.account_Information),
    path('adminsys/login', adminsys_views.login),
    path('adminsys/tables', adminsys_views.tables),
    path('adminsys/cards', adminsys_views.cards),
    path('adminsys/charts', adminsys_views.charts),
    path('adminsys/register', adminsys_views.register),
    path('adminsys/forgot-password', adminsys_views.forgot_password),
    path('adminsys/buttons', adminsys_views.buttons),
    path('adminsys/blank', adminsys_views.blank),
    path('adminsys/utilities-color',adminsys_views.utilities_color),
    path('adminsys/utilities-border', adminsys_views.utilities_border),
    path('adminsys/utilities-animation',adminsys_views.utilities_animation),
    path('adminsys/utilities-other',adminsys_views.utilities_other),
    path('index',index_views.index),
]
