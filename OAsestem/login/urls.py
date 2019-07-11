"""OAsestem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^staff/$', views.staff, name='staff'),
    url(r'^staff_add/$', views.staff_add, name='staff_add'),
    url(r'^staff/staff_delete/(?P<id>\d+)/$', views.staff_delete, name='staff_delete'),
    url(r'^staff_search/$', views.search, name='staff_search'),
    url(r'^staff_update/(?P<id>\d+)$', views.update, name='staff_update'),
]
