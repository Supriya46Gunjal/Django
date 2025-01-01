from django.db import models

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=50)
    total_flats = models.PositiveBigIntegerField()
    location = models.CharField(max_length=100)
    size = models.IntegerField()
    occupancy = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.name} {self.total_flats} {self.location}{self.size} {self.occupancy}"
    

class Employee(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=50)
    dept_id = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.dept_id}{self.salary}{self.hire_date}"
    
    
