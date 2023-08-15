from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointment/', include(('appointment.urls', 'appointment'), namespace='appointment')),
    path('accounts/', include('allauth.urls')),
]