from django.conf.urls import url, include
from django.contrib import admin
#from registrations.views import RegisterFormView, LoginFormView, LogoutView, register_confirm
from django.conf import settings
from registrations.views import LoginFormView, LogoutView
from . import views


urlpatterns = [
#    url(r'^login/$',  views.login, name='login'),
    url(r'^login/$', views.LoginFormView.as_view(), name = 'login'),
#    url(r'^logout/$', views.logout, name='logout'),
    url(r'^logout/$', views.LogoutView.as_view(), name = 'logout'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^accounts/confirm/(?P<activation_key>\w+)', views.register_confirm,),
]



