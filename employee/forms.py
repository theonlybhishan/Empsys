from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Person
# class EmployeerForm(forms.Form):
#     name = forms.CharField( max_length=100)
#     email= forms.EmailField(required=True)
    
class EmployeeForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name','last_name','address']
