from django.db import models
from employees.models import Teacher

class Student(models.Model):
    name = models.CharField(max_length=30)
    surename = models.CharField(max_length=30)
    student_class = models.ForeignKey('StudentClass', null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name + " " + self.surename
    
    class Meta:
        ordering = ['name']

class StudentClass(models.Model):
    class_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.class_name

class StudentClassToTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)