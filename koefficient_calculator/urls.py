from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfessionToExperienceViewSet, ProfessionToQualificationViewSet, KoefficientListView, KoefficientEditView, KoefficientCreateView

router = DefaultRouter()
router.register(r'profession-to-experience', ProfessionToExperienceViewSet)
router.register(r'profession-to-qualification', ProfessionToQualificationViewSet)

urlpatterns = [
    # Include the router's URLs in your project's URLs
    path('', include(router.urls)),
    path('koefficients/', KoefficientListView.as_view(), name='koefficient-list'),
    path('koefficients/<int:pk>/edit/', KoefficientEditView.as_view(), name='koefficient-edit'),
    path('koefficients/create/', KoefficientCreateView.as_view(), name='koefficient-create'),
]