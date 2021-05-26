from django.contrib.auth import forms
from django.shortcuts import render,redirect
from django.contrib import messages 
from .forms import UserRegisterForm


# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('employee')
    else:
        form =UserRegisterForm()
    
    return render(request, 'user/register.html',{'form':form})