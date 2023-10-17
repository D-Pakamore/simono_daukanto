from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.forms import ModelForm, ModelChoiceField
from rest_framework import viewsets, filters
from .models import ProfessionToExperience, ProfessionToQualification, Experience, Qualification, Koefficient
from .serializers import ProfessionToExperienceSerializer, ProfessionToQualificationSerializer, ExperienceSerializer, QualificationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin



class KoefficientListView(LoginRequiredMixin, ListView):
    model = Koefficient
    template_name = 'koefficient-list.html'
    login_url = '/accounts/login/'

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        queryset = Koefficient.objects.all()

        # Apply filtering if a search query is provided
        if search_query:
            queryset = queryset.filter(
                Q(profession__name__icontains=search_query) |
                Q(qualification__value__icontains=search_query) |
                Q(experience__value__icontains=search_query)
            )

        return queryset
    
class KoefficientEditView(UpdateView):
    model = Koefficient
    fields = '__all__'
    template_name = 'koefficient-edit.html'  # Create an HTML template for editing an employee
    success_url = '/employees/koefficients/'

class KoefficientCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  
        super(KoefficientCreateForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Koefficient
        fields = '__all__'
        # labels = {
        #     'first_name': 'Vardas',
        #     'last_name': 'Pavardė',
        # }  

class KoefficientCreateView(CreateView):
    model = Koefficient
    template_name = 'koefficient-create.html'
    form_class = KoefficientCreateForm
    success_url = '/employees/'

#api
class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class QualificationViewSet(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

class ProfessionToExperienceViewSet(viewsets.ModelViewSet):
    queryset = ProfessionToExperience.objects.all()
    serializer_class = ProfessionToExperienceSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['profession']

class ProfessionToQualificationViewSet(viewsets.ModelViewSet):
    queryset = ProfessionToQualification.objects.all()
    serializer_class = ProfessionToQualificationSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['profession']

