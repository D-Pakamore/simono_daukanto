from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'birth_date', 'phone_number', 'email', 'home_address', 'koefficient']
    exclude = []
