from django import forms
from .models import Productos, Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class categoria(forms.ModelForm):
    
    class Meta:
        model = Productos
        fields = '__all__'

class CreatUserForm(UserCreationForm):
   

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')

class Contacto(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'