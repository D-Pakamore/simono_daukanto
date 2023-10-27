from django.urls import path
from .views import TeacherListView, TeacherCreateView, TeacherDeleteView, TeacherDetailView, TeacherUpdateView, add_class_to_teacher, remove_class_from_teacher

urlpatterns = [
    path('', TeacherListView.as_view(), name='teacher-list'),
    path('create/', TeacherCreateView.as_view(), name='teacher-create'),
    path('employee/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher-delete'),
    path('employee/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher-update'),
    path('employee/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),

    path('add-class-to-teacher/<int:class_id>/<int:teacher_id>/', add_class_to_teacher, name='add-class-to-teacher'),
    path('remove-class-from-teacher/<int:class_id>/<int:teacher_id>/', remove_class_from_teacher, name='remove-class-from-teacher'),
]