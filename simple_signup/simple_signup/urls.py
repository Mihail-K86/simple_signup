from django.contrib import admin
from django.urls import path, include
# from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    path('appointment/', include(('appointment.urls', 'appointment'), namespace='appointment')),
    # path('', IndexView.as_view()),
]