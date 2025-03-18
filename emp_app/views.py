from django.shortcuts import render,redirect,HttpResponse
from .models import Department,Role,Employee
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    
    return render(request,"index.html")

def View_all_employee(request):
    emps=Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,"View_all_employee.html",context)


def Remove_an_employee(request,emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully.")
        except:
            return HttpResponse("Please Enter a valid Emp ID.")
    emps = Employee.objects.all()

    #context = {
      #  'emps':emps
   # }
    return render(request,"Remove_an_employee.html",{'emps':emps}) #WE can also passobjects(emps) in this way. 


def Add_employee(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        phone =int(request.POST['phone'])
        salary =int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
       # hire_date = int(request.POST["hire_date"])
        #location = request.POST["location"]
        new_emp = Employee(first_name=first_name,last_name=last_name,dept_id=dept,role_id=role,
                           phone=phone,salary=salary,bonus=bonus,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added Successful.")
    elif request.method == "GET":
        return render(request,'Add_employee.html')
    else :
        return HttpResponse("An Exception Occured, employee has not been added.")


def Filter_employee(request):
    if request.method == "POST":
        name = request.POST['first_name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            #emps = emps.filter(dept__name=dept) # If we don't want to add __icontains with it.
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        return render(request,"View_all_employee.html",{'emps':emps})
    elif request.method == "GET":
        return render(request,"Filter_employee.html")  
    else:
        return  HttpResponse("An Exception Occur")  
 

