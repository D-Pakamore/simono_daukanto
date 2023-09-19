from django.db import models
from koefficient_calculator.models import Koefficient

class Teacher(models.Model):
    TEACHING_SUBJECTS = (
        (1, 'Pradinis ugdymas'),
        (2, 'Pagrindinis ir vidurinis ugdymas'),
        (3, 'Dorinis ugdymas'),
        (4, 'Lietuvių kalba, gimtoji kalba'),
        (5, 'Užsienio kalba'),
        (6, 'Matematika'),
        (7, 'Informacinės technologijos'),
        (8, 'Gamtamokslinis ugdymas'),
        (9, 'Socialinis ugdymas'),
        (10, 'Menai, technologijos, lūno kultūra...'),
        (11, 'Neformalusis švietimas'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    koefficient = models.ForeignKey(Koefficient, null=True ,on_delete=models.SET_NULL)
    

