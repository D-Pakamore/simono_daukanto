from django.db import models

class AdditionalActivity(models.Model):
    ACTIVITY_TYPES = (
        ('MANDATORY', 'Privaloma Veikla mokyklos bendruomenei'),
        ('OPTIONAL', 'Veikla sulygta su mokytoju'),
    )
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    name = models.CharField(max_length=255)
    hours = models.IntegerField()

class ClassTeaching(models.Model):
    CLASS_GRADES = (
        ('1-4', 'Kontaktinės 1-4 kl.'),
        ('5-8', 'Kontaktinės 5-8 kl.'),
    )
    SUTEDENT_COUNTS = (
        ('12-20', '12-20 mokinių klasėje'),
        ('21', '21 ir daugiau mokinių klasėje'),
    )
    class_grade = models.CharField(max_length=1, choices=CLASS_GRADES)
    student_count = models.CharField(max_length=1, choices=SUTEDENT_COUNTS)
    classes_count = models.IntegerField()





