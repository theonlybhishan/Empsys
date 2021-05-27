from django.contrib.auth import forms
from django.shortcuts import render,redirect
from django.contrib import messages 
from .forms import UserRegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login



# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            data = form.cleaned_data
            messages.success(request, f'Account Created for {username}!')
            return redirect('employee')
    else:
        form =UserRegisterForm()
    
    return render(request, 'user/register.html',{'form':form})


def loginUser(request):
    if request.method =='POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data['username'], password=data['password'])
            print(user)
            if user is not None:
                login(request,user)
                return redirect('home')
    
    form = LoginForm()
    context = {
        'form':form
    }
    return render(request, 'user/login.html',context)