from django.db import models
from koefficient_calculator.models import Koefficient

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    koefficient = models.ForeignKey(Koefficient, null=True ,on_delete=models.SET_NULL)
    

