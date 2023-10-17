from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.forms import ModelForm, ModelChoiceField
from .models import Teacher
from workload_calculator.models import Workload, ActivityToWorkload, ContactClasses
from activities.models import Activity, YearlyHours
from koefficient_calculator.models import Profession, Qualification, Experience, Koefficient
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teacher-list.html'
    login_url = '/accounts/login/'

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
    profession = ModelChoiceField(queryset=Profession.objects.all(), label="Profesija")
    experience = ModelChoiceField(queryset=Experience.objects.all(), label="Patirtis metais")
    qualification = ModelChoiceField(queryset=Qualification.objects.all(), label="Kvalifikacija")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  
        super(TeacherCreateForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name','birth_date', 'phone_number', 'email', 'home_address']
        labels = {
            'first_name': 'Vardas',
            'last_name': 'Pavardė',
            'birth_date': 'Gimimo data',
            'phone_number': 'Telefonas', 
            'email': 'Paštas',
            'home_address': 'Asresas',
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
        experience_id = self.request.POST.get('experience')

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

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher-detail.html'
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #Workload to context
        teacher_id = self.kwargs.get('pk')
        teacher_instance = Teacher.objects.get(id=teacher_id)
        workloads = Workload.objects.filter(teacher=teacher_instance)

        for workload in workloads:
            activities_to_workload = ActivityToWorkload.objects.filter(workload=workload)

            yearly_hours = [YearlyHours.objects.get(id=i.yearly_hours.id) for i in activities_to_workload]

            activity_ids = list(dict.fromkeys([i.activity.id for i in yearly_hours]))
            activities = [Activity.objects.get(id=i) for i in activity_ids]

            for activity in activities:
                for yearly_hour in yearly_hours:
                    if yearly_hour.activity.id == activity.id:
                        activity.yearly_hours = yearly_hour.hours


            workload.contact_classes = ContactClasses.objects.filter(workload=workload.id)
            workload.activities = activities
                


        context['workloads'] = workloads

        return context  
