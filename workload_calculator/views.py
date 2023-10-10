from django.shortcuts import render
from .models import Workload, ContactClasses, ActivityToWorkload
from activities.models import Activity, YearlyHours
from contactless_percent_calculator.models import ContactlessHourPercent
from employees.models import Teacher
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.forms import ModelForm, ModelChoiceField, Form, ModelChoiceField
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse

def calc_contact_hours(contact_classes: ContactClasses):
    contact_hours = 0

    for class_instance in contact_classes:
        if class_instance.grade_range == '1-4':
            multiplier = 35
        elif class_instance.grade_range == '5-8':
            multiplier = 37

        contact_hours += multiplier * class_instance.classes_count

    return contact_hours  

def calc_activity_hours(yearly_hours_instances: YearlyHours):
    activity_hours = 0

    for yearly_hour_instance in yearly_hours_instances:
        if yearly_hour_instance.activity.id == 1:
            activity_hours += yearly_hour_instance.hours * 2
        else:
            activity_hours += yearly_hour_instance.hours

    return activity_hours    

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

class ContactClassesCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  
        super(ContactClassesCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ContactClasses
        fields = ['grade_range', 'student_count_range', 'classes_count']
        labels = {
            'grade_range': 'Klasės',
            'student_count_range': 'Studentų skaičius',
            'classes_count': 'Klasių kiekis',
        }     
        

class YearlyHoursForm(Form):
    activity = ModelChoiceField(queryset=Activity.objects.all())
    yearly_hours = ModelChoiceField(queryset=YearlyHours.objects.none())

def get_yearly_hours(request):
    activity_id = request.GET.get('activity_id')
    yearly_hours = YearlyHours.objects.filter(activity_id=activity_id)
    yearly_hours_data = [{'id': x.id, 'hours': x.hours} for x in yearly_hours]

    return JsonResponse({'yearly_hours': yearly_hours_data})    
  
        
    
class WorkloadCreateView(CreateView):
    model = Workload
    template_name = 'workload-create.html'
    form_class = WorkloadCreateForm
    success_url = '/employees/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #Teacher to context
        teacher_id = self.kwargs.get('teacher_id')
        teacher = get_object_or_404(Teacher, id=teacher_id)
        context['teacher'] = teacher

        #extra form to context
        context['contact_classes_form'] = ContactClassesCreateForm()
        context['yearly_hours_form'] = YearlyHoursForm()

        return context
    
    def post(self, request, *args, **kwargs):
        # Check which form was submitted based on the presence of specific fields.
        if 'teaching_subject' in request.POST:
            main_form = True
            form = WorkloadCreateForm(request.POST)

            teaching_subject = request.POST.get("teaching_subject")
            work_experience_period = request.POST.get("work_experience_period")
            student_count = request.POST.get("student_count")
            teacher = request.POST.get("teacher")
            yearly_hours_ids = [int(i) for i in request.POST.get("yearly_hours_multiple").split(",")]
            

            yearly_hours_instances = [YearlyHours.objects.get(id=i) for i in yearly_hours_ids]
            teacher_instance = Teacher.objects.get(id=teacher)
            contactless_hour_percent_instance = ContactlessHourPercent.objects.get(
                teaching_subject=teaching_subject,
                work_experience_period=work_experience_period,
                student_count=student_count
            )
            contact_classes_instances = ContactClasses.objects.filter(workload=None)

            activity_hours = calc_activity_hours(yearly_hours_instances)
            contact_hours: int = calc_contact_hours(contact_classes_instances)
            contactless_hours = contact_hours * ( contactless_hour_percent_instance.percent / 100 )

            total_hours = activity_hours + contact_hours + contactless_hours
            etat_fraction = total_hours * 100 / 1512 / 100

            new_workload_instance = Workload(
                teacher=teacher_instance,
                contactless_hour_percent=contactless_hour_percent_instance,
                contact_hours=contact_hours,
                contactless_hours=contactless_hours,
                total_hours=total_hours,
                etat_fraction=round(etat_fraction, 2)
            )

            new_workload_instance.save()

            for contact_class_instance in contact_classes_instances:
                contact_class_instance.workload = new_workload_instance
                contact_class_instance.save()

            for yearly_hour_instance in yearly_hours_instances:
                new_activity_to_workload = ActivityToWorkload(
                    workload = new_workload_instance,
                    yearly_hours = yearly_hour_instance
                )

                new_activity_to_workload.save()

        elif 'grade_range' in request.POST:
            main_form = False
            form = ContactClassesCreateForm(request.POST)
            
            grade_range = request.POST.get("grade_range")
            student_count_range = request.POST.get("student_count_range")
            classes_count = request.POST.get("classes_count")

            conact_classes_instance = ContactClasses(
                workload=None,
                grade_range=grade_range,
                student_count_range=student_count_range,
                classes_count=classes_count,
            )

            conact_classes_instance.save()
        else:
            # Handle other cases or errors.
            return HttpResponseRedirect(reverse('your_failure_view_name'))
        
        if not main_form:
            return HttpResponse(status=204)

        if form.is_valid():
            # Process the form data here.

            # Redirect to a success page or URL.
            return HttpResponseRedirect(self.success_url)

        # If form is not valid, re-render the template with the form.
        return self.render_to_response(self.get_context_data(form=form))
