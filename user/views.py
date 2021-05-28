from django.contrib.auth import forms
from django.shortcuts import render,redirect
from django.contrib import messages 
from .forms import UserRegisterForm,LoginForm,ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import LogoutView,LoginView
from django.contrib.auth.decorators import login_required




# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            data = form.cleaned_data
            messages.success(request, f'Account Created for {username}!')
            return redirect('login')
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

def LogoutUser(request):
    #logout_user
    logout(request)
    return redirect('login')

@login_required
def ProfileUser(request):
    if request.method=='POST':
        data= request.POST
        first_name = data['first_name']
        last_name = data['last_name']

        user_obj = User.objects.get(id=request.user.id)
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.save()

        print(user_obj)
        return redirect('profile')
    form = ProfileForm( initial={
     'first_name': request.user.first_name,
     'last_name':request.user.last_name   
    })
    context = {
        'form':form
    }
    return render(request, 'user/profile.html',context)


# def ProfileUser(request):
#     pass
#     if request.method == 'POST':
#         form= ProfileForm(request.method)
#         if form.is_valid():
#             first_name = form.cleaned_data.get('first_name')
#             last_name = form.cleaned_data.get('last_name')
#             print(first_name)
#             print(last_name)

#     else:
#         form = ProfileForm()

