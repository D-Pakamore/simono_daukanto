from django.urls import path
from .views import BurelisListView, BurelisCreateView, BurelisDeleteView, BurelisDetailView, BurelisUpdateView, add_student_to_burelis, remove_student_from_burelis, get_burelis_csv

urlpatterns = [
    path('', BurelisListView.as_view(), name='burelis-list'),
    path('create/', BurelisCreateView.as_view(), name='burelis-create'),
    path('burelis/<int:pk>/delete/', BurelisDeleteView.as_view(), name='burelis-delete'),
    path('burelis/<int:pk>/update/', BurelisUpdateView.as_view(), name='burelis-update'),
    path('burelis/<int:pk>/', BurelisDetailView.as_view(), name='burelis-detail'),
    path('burelis-csv/<int:pk>/', get_burelis_csv, name='burelis-csv'),
    path('add-student-to-burelis/<int:student_id>/<int:burelis_id>/', add_student_to_burelis, name='add-student-to-burelis'),
    path('remove-student-from-burelis/<int:student_id>/<int:burelis_id>/', remove_student_from_burelis, name='remove-student-from-burelis'),
]