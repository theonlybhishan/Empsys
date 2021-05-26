from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Person

def home(request):
    employee= Person.objects.all().count
    context={
        'employee': employee
    }
    return render (request,'employee/home.html',context)

def employee(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        address = data['address']

        obj = Person.objects.create(first_name = first_name,last_name= last_name, email = email, address = address)
        print(first_name)
        if obj:
            return redirect('/')
        return HttpResponse("employee is not created")
        # return render(request, 'employee/index.html')
    else:
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
    return render(request, 'employee/index.html',context)

def employee_update(request,id):
    person = Person.objects.get(id=id)
    if request.method=='POST':
        data = request.POST
        person.first_name = data['first_name']
        person.last_name = data['last_name']
        person.address = data['address']
        person.email = data['email']
        person.save()
        print(person)
        return redirect('/')

    context={
        'person':person
    }

    return render(request, 'employee/employee_update.html',context)

def employee_delete(request,id):
    person = Person.objects.get(id=id)
    if request.method=='POST':
        person.delete()
        return redirect('/')
    
    context={
        'person':person
    }
        
    return render(request,'employee/employee_delete.html',context)