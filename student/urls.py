from django.urls import path
from .views import StudentListView, StudentCreateView, StudentDeleteView, StudentDetailView

urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]