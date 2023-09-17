from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.forms import ModelForm, ModelChoiceField
from .models import Employee
from koefficient_calculator.models import Profession, Qualification, Experience, Koefficient
from django.db.models import Q

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee-list.html'

    def get_queryset(self):
        # Fetch the employees and their related coefficients
        queryset = Employee.objects.select_related('koefficient__profession', 'koefficient__experience', 'koefficient__qualification')
        
                # Get the search query parameter from the URL
        search_query = self.request.GET.get('search', '')

        # Apply filtering if a search query is provided
        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query)
            )

        return queryset
    

class EmployeeCreateForm(ModelForm):
    profession = ModelChoiceField(queryset=Profession.objects.all())

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  
        super(EmployeeCreateForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name']
        labels = {
            'first_name': 'Vardas',
            'last_name': 'Pavardė',
        }      
        
    
class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee-create.html'
    form_class = EmployeeCreateForm
    success_url = '/employees/'

    def form_valid(self, form):
        # Access the dynamically added field from self.request.POST
        profession_id = self.request.POST.get('profession')
        qualification_id = self.request.POST.get('qualification')
        experience_id = self.request.POST.get('experience')

        koefficient_instance = Koefficient.objects.get(
            profession=profession_id,
            experience=experience_id,
            qualification=qualification_id
        )

        employee = form.save(commit=False)
        employee.koefficient = koefficient_instance

        return super().form_valid(form) 

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    success_url = '/employees/'
