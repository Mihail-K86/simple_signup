from django.contrib import admin
from django.urls import path, include
from appointment.views import AppointmentView
from .views import IndexView
app_name="appointment"
urlpatterns = [
    path('', AppointmentView.as_view(), name='make_appointment'),
    path('', IndexView.as_view()),
]
