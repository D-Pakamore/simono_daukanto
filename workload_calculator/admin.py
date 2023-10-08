from django.contrib import admin
from .models import Workload, ContactClasses, ActivityToWorkload

@admin.register(Workload)
class WorkloadAdmin(admin.ModelAdmin):
    list_display = ['contactless_hour_percent', 'contact_hours', 'contactless_hours','total_hours','etat_fraction']
    exclude = []

@admin.register(ContactClasses)
class ContactClassesAdmin(admin.ModelAdmin):
    list_display = ['workload', 'grade_range', 'student_count_range', 'classes_count']
    exclude = []  

@admin.register(ActivityToWorkload)
class ActivityToWorkloadAdmin(admin.ModelAdmin):
    list_display = ['workload', 'yearly_hours']
    exclude = []   