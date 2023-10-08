from django.urls import path
from .views import WorkloadCreateView, get_yearly_hours

urlpatterns = [
    path('create/<int:teacher_id>/', WorkloadCreateView.as_view(), name='workload-create'),
    path('get_yearly_hours/', get_yearly_hours, name='get_yearly_hours'),
]