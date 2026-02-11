from django.urls import path
from .views import * 

urlpatterns = [
        path('register/', RegisterView.as_view()),
        path("doctor/profile/", DoctorProfileListCreateView.as_view()),
]
