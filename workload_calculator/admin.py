from django.contrib import admin
from .models import Workload

@admin.register(Workload)
class WorkloadAdmin(admin.ModelAdmin):
    list_display = ['contactless_hour_percent', 'contact_hours', 'contactless_hours','total_hours','etat_fraction']
    exclude = []