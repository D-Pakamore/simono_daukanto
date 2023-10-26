from django.contrib import admin
from .models import Student, StudentClass, StudentClassToTeacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surename', 'student_class']
    exclude = []

@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
    list_display = ['class_name']
    exclude = []

@admin.register(StudentClassToTeacher)
class StudentClassToTeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'student_class']
    exclude = []
