from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from student.models import Student
from burelis.models import StudentToBurelis

def calculate_students_to_burelis_percent():
    all_students = Student.objects.all()

    students_count = len(all_students)
    students_with_burelis_count = 0

    for student in all_students:
        student_bureliai = StudentToBurelis.objects.filter(student=student)

        if len(student_bureliai) != 0:
            print('found')
            students_with_burelis_count += 1

    students_without_burelis = students_count - students_with_burelis_count
    students_without_burelis_percent = students_without_burelis / students_count * 100

    return students_without_burelis_percent



class HomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        print(user.username)

        # Add custom data to the context
        context['nav_endpoints'] = [
            {
                'label': 'Mokytojai',
                'endpoint': ''
            }
        ]

        context['user'] = user
        context['student_without_burelis_percent'] = round(calculate_students_to_burelis_percent(), 1)
        return context   