from django.contrib import admin
from .models import Activity, YearlyHours

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['type', 'name']
    exclude = []

@admin.register(YearlyHours)
class YearlyHoursAdmin(admin.ModelAdmin):
    list_display = ['activity', 'hours']
    exclude = []    

