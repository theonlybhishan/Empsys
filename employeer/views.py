from django.shortcuts import redirect, render
from .forms import EmployeerForm
# Create your views here.


def employeer(request):
    # if request.method =='POST':
    #     form= EmployeerForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         return redirect('/EMPLOYEER')
    form = EmployeerForm
    context = {
        'form':form
    }
    return render(request, 'employeer.html', context)