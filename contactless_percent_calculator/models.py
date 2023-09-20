from django.db import models

class ContactlessHourPercent(models.Model):
    TEACHING_SUBJECTS = (
        ('Pradinis ugdymas', 'Pradinis ugdymas'),
        ('Pagrindinis ir vidurinis ugdymas', 'Pagrindinis ir vidurinis ugdymas'),
        ('Dorinis ugdymas', 'Dorinis ugdymas'),
        ('Lietuvių kalba, gimtoji kalba', 'Lietuvių kalba, gimtoji kalba'),
        ('Užsienio kalba', 'Užsienio kalba'),
        ('Matematika', 'Matematika'),
        ('Informacinės technologijos', 'Informacinės technologijos'),
        ('Gamtamokslinis ugdymas', 'Gamtamokslinis ugdymas'),
        ('Socialinis ugdymas', 'Socialinis ugdymas'),
        ('Menai, technologijos, kūno kultūra...', 'Menai, technologijos, kūno kultūra...'),
        ('Neformalusis švietimas', 'Neformalusis švietimas'),
    )
    WORK_EXPERIENCE_PERIODS = (
        ('iki 2 metų', 'iki 2 metų'),
        ('daugiau nei 2 metai', 'daugiau nei 2 metai'),
    )
    BORAD_STUDENT_COUNTS = (
        ('ne daugiau kaip 11', 'ne daugiau kaip 11'),
        ('12-20', '12-20'),
        ('21 ir daugiau', '21 ir daugiau')
    )
    teaching_subject = models.CharField(max_length=255, choices=TEACHING_SUBJECTS)
    work_experience_period = models.CharField(max_length=255, choices=WORK_EXPERIENCE_PERIODS)
    student_count = models.CharField(max_length=255, choices=BORAD_STUDENT_COUNTS)
    percent = models.FloatField()

    def __str__(self) -> str:
        return self.percent