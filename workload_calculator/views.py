from django.shortcuts import render
from .models import Workload
from contactless_percent_calculator.models import ContactlessHourPercent
from employees.models import Teacher
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.forms import ModelForm, ModelChoiceField
from django.db.models import Q
from django.shortcuts import get_object_or_404

class WorkloadCreateForm(ModelForm):
    # profession = ModelChoiceField(queryset=Profession.objects.all())

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  
        super(WorkloadCreateForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = ContactlessHourPercent
        fields = ['teaching_subject', 'work_experience_period', 'student_count']
        labels = {
            'teaching_subject': 'Bendrojo ugdymo programos dalykai',
            'work_experience_period': 'Darbo stažas',
            'student_count': 'Mokinių skaičius klasėje',
        } 
        

  
        
    
class WorkloadCreateView(CreateView):
    model = Workload
    template_name = 'workload-create.html'
    form_class = WorkloadCreateForm
    success_url = '/teachers/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        teacher_id = self.kwargs.get('teacher_id')
        teacher = get_object_or_404(Teacher, id=teacher_id)
        print(teacher.koefficient.profession)
        context['teacher'] = teacher

        return context

    def form_valid(self, form):
        # Access the dynamically added field from self.request.POST
        # profession_id = self.request.POST.get('profession')
        # qualification_id = self.request.POST.get('qualification')
        # experience_id = self.request.POST.get('experience')
        teaching_subject = self.request.POST.get('teaching_subject')
        work_experience_period = self.request.POST.get('work_experience_period')
        student_count = self.request.POST.get('student_count')

        contactless_hour_percent_instance = ContactlessHourPercent.objects.get(
            teaching_subject=teaching_subject,
            work_experience_period=work_experience_period,
            student_count=student_count
        )

        print(contactless_hour_percent_instance)

        # koefficient_instance = Koefficient.objects.get(
        #     profession=profession_id,
        #     experience=experience_id,
        #     qualification=qualification_id
        # )

        # teacher = form.save(commit=False)
        # teacher.koefficient = koefficient_instance
        

        return 
