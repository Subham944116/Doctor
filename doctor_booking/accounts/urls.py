from django.urls import path
from .views import * 

urlpatterns = [
        path('register/', RegisterView.as_view()),
        path("doctor/profile/", DoctorProfileListCreateView.as_view()),
        path("profile/", ProfileView.as_view(), name="profile"),
]
