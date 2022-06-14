from django.contrib import admin
from django.urls import path
from .views import home,CustomLoginView,perfil,registro,editarperfil, act_perfil
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',home,name="home"),
    path('perfil/',login_required(perfil),name="perfil"),
    path('registro/',registro,name="registro"),
    path('editarperfil/',login_required(editarperfil),name="editarperfil"),
    path('act_perfil/',login_required(act_perfil),name="act_perfil"),
    path('InicioSesion/', CustomLoginView.as_view(), name='InicioSesion'),
    path('logout/', LogoutView.as_view(template_name='masterBikes/home.html'), name='logout'),
]