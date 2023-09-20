from django.db import models
from koefficient_calculator.models import Koefficient

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    koefficient = models.ForeignKey(Koefficient, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    

