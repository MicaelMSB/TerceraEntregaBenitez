
from django.shortcuts import render
from .models import *
from django.views import View
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import AvatarFormulario


def inicio(req):
    try:

        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "inicio.html", {"url": avatar.imagen.url})
    except:
        return render(req, "inicio.html")
def loginView(req):

    if req.method == 'POST':
        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            password = data["password"]

            user = authenticate(username=usuario, password=password)
            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido a SanviShop {usuario}"})
            else:
                return render(req, "inicio.html", {"mensaje": f"Los datos ingresados son incorrectos"})
        else: 
            return render(req, "inicio.html", {"mensaje": f"El formulario es invalido"})

    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario})
    
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese email")
    age = forms.IntegerField(label="Ingrese su edad")

    error_messages = {
        'password_mismatch': "Las contraseñas no coinciden.",
        'password_too_similar': "La contraseña no puede ser demasiado similar a tu información personal.",
        'password_length': "La contraseña debe tener al menos 8 caracteres.",
        'password_common': "La contraseña no puede ser una contraseña común.",
        'password_numeric': "La contraseña no puede ser completamente numérica.",
        'invalid_age': "Debes ser mayor de 18 años para registrarte.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Ingrese nombre de usuario"
        self.fields['password1'].label = "Ingrese contraseña"
        self.fields['password2'].label = "Repita la contraseña"

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age < 18:
            raise forms.ValidationError(self.error_messages['invalid_age'])
        return age

def register(req):
    if req.method == 'POST':
        miFormulario = RegistrationForm(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            miFormulario.save()
            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito"})
        else:
            errores = miFormulario.errors
            return render(req, "inicio.html", {"miFormulario": miFormulario, "errores": errores})
    else:
        miFormulario = RegistrationForm()
        return render(req, "registro.html", {"miFormulario": miFormulario})
@login_required    
def editar_perfil(req):
    usuario = req.user
    if req.method == 'POST':
        miFormulario = UserChangeForm(req.POST, instance=req.user)
        form_password = PasswordChangeForm(user=usuario, data=req.POST)
        if miFormulario.is_valid() and form_password.is_valid():
            data = miFormulario.cleaned_data
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.email = data['email']
            usuario.save()
            form_password.save()
            return render(req, "inicio.html", {"mensaje": "Perfil y contraseña actualizados con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Error al actualizar perfil o contraseña"})
    else:
        miFormulario = UserChangeForm(instance=req.user)
        form_password = PasswordChangeForm(user=usuario)
        return render(req, "editar_perfil.html", {"miFormulario": miFormulario, "form_password": form_password})
    
@login_required  
def agregar_avatar(req):
    if req.method == 'POST':
        miFormulario = AvatarFormulario(req.POST, req.FILES)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            avatar = Avatar(user=req.user, imagen=data["imagen"])
            avatar.save()
            return render(req, "inicio.html", {"mensaje": f"Avatar actualizado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": f"Formulario Inválido"})
    else:
        miFormulario = AvatarFormulario()
        return render(req, "agregar_avatar.html", {"miFormulario": miFormulario})