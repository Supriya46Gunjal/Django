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
     