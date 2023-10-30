from django.contrib import admin
from .models import Burelis, StudentToBurelis

@admin.register(Burelis)
class BurelisAdmin(admin.ModelAdmin):
    list_display = ['pavadinimas', 'valandu_skaicius', 'mokytojas', 'diena', 'valanda_nuo_iki', 'vygdimo_vieta']

@admin.register(StudentToBurelis)
class StudentToBurelisAdmin(admin.ModelAdmin):
    list_display = ['burelis', 'student']    
