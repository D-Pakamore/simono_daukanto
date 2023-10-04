from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.forms import ModelForm, ModelChoiceField
from .models import Teacher
from koefficient_calculator.models import Profession, Qualification, Experience, Koefficient
from django.db.models import Q

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher-list.html'

    def get_queryset(self):
        # Fetch the employees and their related coefficients
        queryset = Teacher.objects.select_related('koefficient__profession', 'koefficient__experience', 'koefficient__qualification')
        
                # Get the search query parameter from the URL
        search_query = self.request.GET.get('search', '')

        # Apply filtering if a search query is provided
        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query)
            )

        return queryset
    

class TeacherCreateForm(ModelForm):
    profession = ModelChoiceField(queryset=Profession.objects.all())

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  
        super(TeacherCreateForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name']
        labels = {
            'first_name': 'Vardas',
            'last_name': 'Pavardė',
        }      
        
    
class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'teacher-create.html'
    form_class = TeacherCreateForm
    success_url = '/employees/'

    def form_valid(self, form):
        # Access the dynamically added field from self.request.POST
        profession_id = self.request.POST.get('profession')
        qualification_id = self.request.POST.get('qualification')
        experience_years = int(self.request.POST.get('work_experience_years'))

        if experience_years < 2:
            experience_value = "iki 2"
        elif experience_years >= 2 and experience_years < 5:
            experience_value = "nuo 2 iki 5"
        elif experience_years >= 5 and experience_years < 10:
            experience_value = "nuo 5 iki 10"
        elif experience_years >= 10 and experience_years < 15:
            experience_value = "nuo 10 iki 15"
        elif experience_years >= 15 and experience_years < 20:
            experience_value = "nuo 15 iki 20"
        elif experience_years >= 20 and experience_years < 25:
            experience_value = "nuo 20 iki 25"
        elif experience_years > 25:
            experience_value = "daugiau kaip 25"

        experience_id = Experience.objects.get(value=experience_value).id

        koefficient_instance = Koefficient.objects.get(
            profession=profession_id,
            experience=experience_id,
            qualification=qualification_id
        )

        teacher = form.save(commit=False)
        teacher.koefficient = koefficient_instance

        return super().form_valid(form) 

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teacher_confirm_delete.html'
    success_url = '/employees/'
