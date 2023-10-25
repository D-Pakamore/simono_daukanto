from django.db import models

class Activity(models.Model):
    TYPES = (
        ('Privaloma Veikla', 'Privaloma Veikla'),
        ('Sulygstama veikla', 'Sulygstama Veikla'),
    )
    type = models.CharField(max_length=50, choices=TYPES)
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class YearlyHours(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    hours = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.hours)
