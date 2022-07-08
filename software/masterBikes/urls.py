from django.contrib import admin
from django.urls import path

from masterBikes.forms import subirbici
from .views import bici, cancelar, historial, historial2, home,CustomLoginView,perfil,registro,editarperfil, act_perfil, formbici, rentar, reparar
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',home,name="home"),
    path('perfil/',login_required(perfil),name="perfil"),
    path('formbici/',login_required(formbici),name="formbici"),
    path('bici/<int:id>',bici,name="bici"),
    path('rentar/', rentar, name="rentar"),
    path('cancelar/<int:id>', cancelar, name="cancelar"),
    path('reparar/<int:id>', reparar, name="reparar"),
    path('historial/', login_required(historial), name="historial"),
    path('historial2/', login_required(historial2), name="historial2"),
    path('registro/',registro,name="registro"),
    path('editarperfil/',login_required(editarperfil),name="editarperfil"),
    path('act_perfil/',login_required(act_perfil),name="act_perfil"),
    path('InicioSesion/', CustomLoginView.as_view(), name='InicioSesion'),
    path('logout/', LogoutView.as_view(template_name='masterBikes/home.html'), name='logout'),
]