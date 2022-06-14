from email import message
from django.shortcuts import  render, redirect
from django.contrib import messages
from .forms import UserForm,LoginForm, EditUserForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.views.generic.base import View



def home(request):
    return render(request,'masterBikes/home.html')

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
