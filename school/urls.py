
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('employees/', include('employees.urls')),
    path('koefficients/', include('koefficient_calculator.urls')),
    path('api/', include('koefficient_calculator.urls')),
    path('workload/', include('workload_calculator.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
