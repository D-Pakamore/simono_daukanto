from django.db import models
from employees.models import Teacher
from student.models import Student

class Burelis(models.Model):
    pavadinimas = models.CharField(max_length=255)
    valandu_skaicius = models.IntegerField()
    mokytojas = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    diena = models.CharField(max_length=255)
    valanda_nuo_iki = models.CharField(max_length=255)
    vygdimo_vieta = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.pavadinimas

class StudentToBurelis(models.Model):
    burelis = models.ForeignKey(Burelis, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
