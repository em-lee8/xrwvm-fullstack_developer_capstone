# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPE = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('HYBRID', 'Hybrid'),
        ('ELECTRIC', 'Electric'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPE)
    year = models.IntegerField(default=2023,
         validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
         ])

    def __str__(self):
        return self.name
