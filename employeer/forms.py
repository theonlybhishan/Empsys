from django.db.models import fields
from django.forms import ModelForm, models
from .models import Employeer

class EmployeerForm(ModelForm):
    class Meta:
        model= Employeer
        fields =['first_name','last_name','email']