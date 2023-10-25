from django.db import models
from contactless_percent_calculator.models import ContactlessHourPercent
from activities.models import Activity, YearlyHours
from employees.models import Teacher

class Workload(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    contactless_hour_percent = models.ForeignKey(ContactlessHourPercent, models.CASCADE)
    contact_hours = models.IntegerField(null=True)
    contactless_hours = models.IntegerField(null=True)
    total_hours = models.IntegerField(null=True)
    etat_fraction = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class ActivityToWorkload(models.Model):
    workload = models.ForeignKey(Workload, null=True, on_delete=models.CASCADE)
    yearly_hours = models.ForeignKey(YearlyHours, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    

class ContactClasses(models.Model):
    CLASS_GRADES = (
        ('1-4', 'Kontaktinės 1-4 kl.'),
        ('5-8', 'Kontaktinės 5-8 kl.'),
    )
    SUTEDENT_COUNTS = (
        ('12-20', '12-20 mokinių klasėje'),
        ('21', '21 ir daugiau mokinių klasėje'),
    )
    workload = models.ForeignKey(Workload, default=None, null=True, on_delete=models.CASCADE)
    grade_range = models.CharField(max_length=100, choices=CLASS_GRADES)
    student_count_range = models.CharField(max_length=100, choices=SUTEDENT_COUNTS)
    classes_count = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)





