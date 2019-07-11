from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^log_in/$', views.log_in, name='log_in'),
    url(r'^log_back/$', views.log_back, name='log_back'),
    url(r'^find_one/$', views.find_one, name='find_one'),
    url(r'^find_all/$', views.find_all, name='find_all'),
    url(r'^alter/$', views.alter, name='alter'),
    url(r'^alter_server/$', views.alter_server, name='alter_server'),
    url(r'^get_session/$', views.get_session, name='get_session'),
    url(r'^find_user_all/$', views.find_user_all),
]
