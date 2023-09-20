from django.contrib import admin
from .models import Workload

@admin.register(Workload)
class WorkloadAdmin(admin.ModelAdmin):
    list_display = ['contactless_hour_percent', 'yearly_contact_hours', 'contactless_hours','total_hours','etato_dalis']
    exclude = []