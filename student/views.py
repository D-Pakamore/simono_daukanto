from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.forms import ModelForm, ModelChoiceField
from .models import Student, StudentClass, StudentClassToTeacher
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student-list.html'
    login_url = '/accounts/login/'

    def get_queryset(self):
        # Fetch the employees and their related coefficients
        queryset = Student.objects.all()
        
                # Get the search query parameter from the URL
        search_query = self.request.GET.get('search', '')

        # Apply filtering if a search query is provided
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(surename__icontains=search_query) |
                Q(student_class__class_name__icontains=search_query)
            )

        return queryset
    
    def get_context_data(self, **kwargs):
        student_classes = StudentClass.objects.all()
        context = super().get_context_data(**kwargs)

        # Add custom data to the context

        context['student_classes'] = student_classes
        return context  
    
class StudentCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  
        super(StudentCreateForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Student
        fields = ['name', 'surename','student_class']
        labels = {
            'name': 'Vardas',
            'surename': 'Pavardė',
            'student_class': 'Klasė',
        }      
        
    
class StudentCreateView(CreateView):
    model = Student
    template_name = 'student-create.html'
    form_class = StudentCreateForm
    success_url = '/student/' 

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student-confirm-delete.html'
    success_url = '/student/'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student-detail.html'
    context_object_name = 'student'

class StudentEditView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'student-edit.html'  # Create an HTML template for editing an employee
    success_url = '/student/'    
