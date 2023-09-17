from django.contrib import admin
from .models import Profession, Experience, Qualification, ProfessionToExperience, ProfessionToQualification, Koefficient

@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ['name']
    exclude = []

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']
    exclude = []

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']
    exclude = []

@admin.register(ProfessionToExperience)
class ProfessionToExperienceAdmin(admin.ModelAdmin):
    list_display = ['profession', 'experience']
    exclude = []

@admin.register(ProfessionToQualification)
class ProfessionToQualificationAdmin(admin.ModelAdmin):
    list_display = ['profession', 'qualification']
    exclude = []    

@admin.register(Koefficient)
class KoefficientAdmin(admin.ModelAdmin):
    list_display = ['profession', 'experience', 'qualification', 'value']
    exclude = []
