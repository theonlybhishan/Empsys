from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model= User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)