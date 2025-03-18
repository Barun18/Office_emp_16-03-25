
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('View_all_employee',views.View_all_employee,name='View_all_employee'),
    path('Add_employee',views.Add_employee,name='Add_employee'),
    path('Remove_an_employee',views.Remove_an_employee,name='Remove_an_employee'),
    path('Remove_an_employee/<int:emp_id>',views.Remove_an_employee,name='Remove_an_employee'),
    path('Filter_employee',views.Filter_employee,name='Filter_employee'),
    
]