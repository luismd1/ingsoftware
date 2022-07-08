import datetime
from email import message
from django.shortcuts import  render, redirect
from django.contrib import messages

from masterBikes.models import Bici, Venta
from .forms import UserForm,LoginForm, EditUserForm, subirbici
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.views.generic.base import View



def home(request):
    lista = Bici.objects.all()
    data = {'lista':lista}
    return render(request,'masterBikes/home.html', data)

def perfil(request):
    return render(request,'masterBikes/perfil.html')

def InicioSesion(request):
    return render(request,'masterBikes/InicioSesion.html')


def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            nick1 = form.cleaned_data['username']
            messages.success(request, f'Usuario {nick1} creado con exito')
            return redirect('home')
    else:
        form = UserForm()

    contexto = { 'form' : form }

    return render(request,'masterBikes/registro.html', contexto)


def editarperfil(request):
    user = User.objects.filter(id=request.user.id).first()
    form = EditUserForm(instance = user)

    return render(request,'masterBikes/editarperfil.html',{'form':form, 'user':user})

def act_perfil(request):
    user = User.objects.get(id=request.user.id)
    form = UserForm(request.POST, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Perfil actualizado con exito')
        return redirect(to="perfil")


class CustomLoginView(LoginView):
    template_name = 'masterBikes/InicioSesion.html'
    form_class = LoginForm
# Create your views here.

def formbici(request):
    form = subirbici()
    data = {'form':form}
    if request.method == 'POST':
        form = subirbici(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bicicleta subida con exito')
            return redirect(to="home")
        else:
            messages.error(request, 'Error al subir la bicicleta')
            return redirect(to="formbici")
    return render(request,'masterBikes/subirbici.html', data)

def bici(request, id):
    bici = Bici.objects.get(pk=id)
    data = {'bici':bici}
    return render(request,'masterBikes/bici.html', data)

def rentar(request):
    ide = request.POST.get('idBici')
    bici = Bici.objects.get(pk=ide)
    fecha_ini = request.POST.get('datefield')
    fecha_fin = request.POST.get('datefield2')
    pago = request.POST.get('metodo')
    cantidad2 = request.POST.get('cantidad')
    precio2 = bici.precio * cantidad2

    Venta.objects.create(idBici=bici, cliente = request.user, fecha = fecha_ini, fechaTermino = fecha_fin, formadepago = pago, cantidad = cantidad2, precio = precio2)    
    return redirect(to="home")