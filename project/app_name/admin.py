from django.contrib import admin
from .models import Building,Employee

# Register your models here.
@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name','total_flats','location','occupancy','size')
    search_fields = ('name','location')
    list_filter = ('total_flats','occupancy','size')
    fields = ('name','total_flats','location','occupancy','size')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id','name','dept_id','salary','hire_date')
    search_fields = ('emp_id','name','dept_id')
    list_filter = ('salary','hire_date')
    fields = ('emp_id','name','dept_id','salary','hire_date')
