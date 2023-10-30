from django.shortcuts import render
from .models import Burelis, StudentToBurelis
from django.db.models import Q
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm, ModelChoiceField
from student.models import Student

class BurelisListView(LoginRequiredMixin, ListView):
    model = Burelis
    template_name = 'burelis-list.html'
    login_url = '/accounts/login/'

    def get_queryset(self):
        queryset = Burelis.objects.all()
        search_query = self.request.GET.get('search', '')
    





        # Apply filtering if a search query is provided
        if search_query:
            queryset = queryset.filter(
                Q(pavadinimas__icontains=search_query) |
                Q(mokytojas__first_name__icontains=search_query)
            )

        return queryset
    
class BurelisCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  
        super(BurelisCreateForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Burelis
        fields = ['pavadinimas', 'valandu_skaicius', 'mokytojas', 'diena', 'valanda_nuo_iki', 'vygdimo_vieta']
        labels = {
            'pavadinimas': 'Pavadinimas',
            'valandu_skaicius': 'Valandų skaičius',
            'mokytojas': 'Mokytojas',
            'diena': 'Diena',
            'valanda_nuo_iki': 'Valanda nuo iki',
            'vygdimo_vieta': 'Vygdimo vieta',
        }      
        
    
class BurelisCreateView(CreateView):
    model = Burelis
    template_name = 'burelis-create.html'
    form_class = BurelisCreateForm
    success_url = '/burelis/' 

class BurelisDeleteView(DeleteView):
    model = Burelis
    template_name = 'burelis-confirm-delete.html'
    success_url = '/burelis/'

class BurelisDetailView(DetailView):
    model = Burelis
    template_name = 'burelis-detail.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Burelis.objects.get(id=self.object.id)
        students = Student.objects.all()
        burelis_students = StudentToBurelis.objects.filter(burelis=queryset)
        burelis_students_clean = []

        for burelis_stud in burelis_students:
            # student = Student.objects.get
            burelis_students_clean.append(burelis_stud.student)


        context['burelis'] = queryset
        context['students'] = students
        context['burelis_students'] = burelis_students_clean
        print(context['burelis_students'])

        return context

class BurelisEditForm(ModelForm):
    class Meta:
        model = Burelis
        fields = ['pavadinimas', 'valandu_skaicius', 'mokytojas', 'diena', 'valanda_nuo_iki', 'vygdimo_vieta']
        labels = {
            'pavadinimas': 'Pavadinimas',
            'valandu_skaicius': 'Valandų skaičius',
            'mokytojas': 'Mokytojas',
            'diena': 'Diena',
            'valanda_nuo_iki': 'Valanda nuo iki',
            'vygdimo_vieta': 'Vygdimo vieta',
        }      

class BurelisUpdateView(UpdateView):
    model = Burelis
    form_class = BurelisEditForm
    template_name = 'burelis-update.html'  # Create an HTML template for editing an employee
    success_url = '/burelis/' 

def add_student_to_burelis(request, student_id, burelis_id):
    burelis_instance = Burelis.objects.get(id=burelis_id)
    student_instance = Student.objects.get(id=student_id)

    new_instance = StudentToBurelis(student=student_instance, burelis=burelis_instance)
    new_instance.save()

    burelis_detail_view = BurelisDetailView.as_view()
    return burelis_detail_view(request, pk=burelis_id)

def remove_student_from_burelis(request, student_id, burelis_id):
    burelis_instance = Burelis.objects.get(id=burelis_id)
    student_instance = Student.objects.get(id=student_id)

    target_instance = StudentToBurelis.objects.get(student=student_instance, burelis=burelis_instance)
    target_instance.delete()

    burelis_detail_view = BurelisDetailView.as_view()
    return burelis_detail_view(request, pk=burelis_id)



