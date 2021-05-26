from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home, name='home'),
    path('', views.employee, name= 'employee'),
    path('employee_update/<int:id>',views.employee_update, name='update'),
    path('employee_delete/<int:id>',views.employee_delete, name='delete')
    
]