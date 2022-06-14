from cProfile import label
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User



class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-white','placeholder':'Contraseña','id':'reg-pass'}))
    password2 = forms.CharField(label='Confirmas contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-white','placeholder':'Contraseña','id':'reg-pass2'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white',
                'placeholder': 'Nombre de usuario',
                'id': 'reg-usu'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-dark text-white',
                'placeholder': 'Correo electrónico',
                'id': 'reg-email'})
        }





class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario',
                                widget=forms.TextInput(attrs={'class': 'form-control bg-dark text-dark','placeholder':'Nombre de usuario'}))
    password = forms.CharField(label='Contraseña',
                                widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-white','placeholder':'Contraseña'}))



class EditUserForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña nueva',widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-white','placeholder':'Contraseña','id':'reg-pass'}))
    password2 = forms.CharField(label='Contraseña confirmar',widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-white','placeholder':'Contraseña','id':'reg-pass2'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {k: "" for k in fields}
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña actual',
            'password2': 'Contraseña nueva',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-dark',
                'placeholder': 'Nombre de usuario',
                'id': 'reg-usu'}),
        }