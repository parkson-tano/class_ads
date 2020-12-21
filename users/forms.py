from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RegUser
from django.forms import ModelForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone']
        


class LoginUser(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200,  widget=forms.PasswordInput())