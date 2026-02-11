from rest_framework import serializers
from .models import Appointment
from django.contrib.auth.models import User


class AppointmentSerializer(serializers.ModelSerializer):

    patient = serializers.CharField(
        source="patient.username",
        read_only=True
    )

    class Meta:
        model = Appointment
        fields = [
            "id",
            "patient",
            "doctor",
            "date",
            "start_time",
            "end_time",
        ]
        read_only_fields = ["patient"]
