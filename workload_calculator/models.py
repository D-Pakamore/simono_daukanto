from django.db import models
from contactless_percent_calculator.models import ContactlessHourPercent
from activities.models import Activity
from employees.models import Teacher

class Workload(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    contactless_hour_percent = models.ForeignKey(ContactlessHourPercent, models.CASCADE)
    yearly_contact_hours = models.IntegerField(null=True)
    contactless_hours = models.IntegerField(null=True)
    total_hours = models.IntegerField(null=True)
    etato_dalis = models.FloatField(null=True)

class ActivityToWorkload(models.Model):
    workload = models.ForeignKey(Workload, null=True, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    

class ContactClasses(models.Model):
    wrokload = models.ForeignKey(Workload, null=True, on_delete=models.CASCADE)
    CLASS_GRADES = (
        ('1-4', 'Kontaktinės 1-4 kl.'),
        ('5-8', 'Kontaktinės 5-8 kl.'),
    )
    SUTEDENT_COUNTS = (
        ('12-20', '12-20 mokinių klasėje'),
        ('21', '21 ir daugiau mokinių klasėje'),
    )
    class_grade = models.CharField(max_length=100, choices=CLASS_GRADES)
    student_count = models.CharField(max_length=100, choices=SUTEDENT_COUNTS)
    classes_count = models.IntegerField()





