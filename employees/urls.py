from django.urls import path
from .views import TeacherListView, TeacherCreateView, TeacherDeleteView

urlpatterns = [
    path('', TeacherListView.as_view(), name='teacher-list'),
    path('create/', TeacherCreateView.as_view(), name='teacher-create'),
    path('employees/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher-delete'),
]