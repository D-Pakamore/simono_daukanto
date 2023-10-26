from django.db import models
from koefficient_calculator.models import Koefficient

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=100, blank=True)
    home_address = models.CharField(max_length=255, blank=True)
    #auto calc
    koefficient = models.ForeignKey(Koefficient, null=True, blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    
    class Meta:
        ordering = ['first_name']
    

