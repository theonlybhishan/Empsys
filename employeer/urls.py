from django.urls import path
from .import views

appname= "employeer"

urlpatterns = [
    path('', views.employeer, name='employeer')
]
