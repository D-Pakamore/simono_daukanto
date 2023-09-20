from django.contrib import admin
from .models import ContactlessHourPercent

@admin.register(ContactlessHourPercent)
class ContactlessHourPercentAdmin(admin.ModelAdmin):
    list_display = ['teaching_subject', 'work_experience_period', 'student_count', 'percent']
    exclude = []    
