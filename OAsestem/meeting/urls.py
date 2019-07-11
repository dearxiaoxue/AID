from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='meeting'),
    url(r'^newmeet/$', views.newmeet, name='newmeet'),
    url(r'^selectmeet/$', views.selectmeet, name='selectmeet'),
    url(r'^remindmeet/(?P<page>\d+)/$', views.remindmeet, name='remindmeet'),
    url(r'^uploadmeet/(?P<page>\d+)/$', views.uploadmeet, name='uploadmeet'),
    url(r'^uploadmeet01/(?P<meid>\d+)/$', views.uploadmeet01, name='uploadmeet01'),
    url(r'^updateinfo/(?P<meid>\d+)/$', views.updateinfo, name='updateinfo'),
    url(r'^delinfo/(?P<meid>\d+)/$', views.delinfo, name='delinfo'),
]
