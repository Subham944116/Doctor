from django.urls import path
from .views import (
    BookAppointmentView,
    PatientAppointmentListView,
    DoctorAppointmentListView
)

urlpatterns = [
    path("book/", BookAppointmentView.as_view()),
    path("patient/", PatientAppointmentListView.as_view()),
    path("doctor/", DoctorAppointmentListView.as_view()),
]
