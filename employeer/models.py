from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class Employeer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=False)
