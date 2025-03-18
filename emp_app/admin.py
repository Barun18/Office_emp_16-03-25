from django.contrib import admin
from . models import Employee,Role,Department 
# i Register my models here.
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)