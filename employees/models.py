from django.db import models
from koefficient_calculator.models import Koefficient
from koefficient_calculator.models import Profession, Qualification
from contactless_percent_calculator.models import ContactlessHourPercent

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    work_experience_years = models.IntegerField()
    profession = models.ForeignKey(Profession, null=True, on_delete=models.SET_NULL)
    qualification = models.ForeignKey(Qualification, null=True, on_delete=models.SET_NULL)
    #auto calc
    koefficient = models.ForeignKey(Koefficient, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    

