from django.db import models

class TeachingSubject(models.Model):
    subject = models.CharField(max_length=255)
    subject_number = models.IntegerField()

class ContactlessPercent(models.Model):
    YEAR_EXPERIENCES = (
        (1, 'iki 2 metų'),
        (2, '2 ir daugiau metų'),
    )
    STUDENT_COUNTS = (
        (1, 'ne daugiau kaip 11'),
        (2, '12-20'),
        (3, '21 ir daugiau'),
    )
    teaching_subject = models.ForeignKey(TeachingSubject, on_delete=models.CASCADE)
    year_experience = models.IntegerField(choices=YEAR_EXPERIENCES)
    student_count = models.IntegerField(choices=STUDENT_COUNTS)
    contactless_percent = models.FloatField()