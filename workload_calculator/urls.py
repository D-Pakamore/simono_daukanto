from django.urls import path
from .views import WorkloadCreateView

urlpatterns = [
    path('create/<int:teacher_id>/', WorkloadCreateView.as_view(), name='workload-create'),
]