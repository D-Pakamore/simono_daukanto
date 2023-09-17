from django.db import models


class Profession(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.value

class Qualification(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.value


class ProfessionToExperience(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)

class ProfessionToQualification(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)

class Koefficient(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    value = models.FloatField(max_length=255)

    def __str__(self) -> str:
        return str(self.value)