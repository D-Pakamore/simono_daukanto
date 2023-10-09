from django.urls import path
from .views import TeacherListView, TeacherCreateView, TeacherDeleteView, TeacherDetailView

urlpatterns = [
    path('', TeacherListView.as_view(), name='teacher-list'),
    path('create/', TeacherCreateView.as_view(), name='teacher-create'),
    path('employee/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher-delete'),
    path('employee/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
]