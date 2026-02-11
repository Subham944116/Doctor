from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Appointment
from .serializers import AppointmentSerializer
from accounts.perimission import IsPatient, IsDoctor
# Create your views here.


class BookAppointmentView(APIView):
    permission_classes = [IsAuthenticated, IsPatient]

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(patient=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
class PatientAppointmentListView(APIView):
    permission_classes = [IsAuthenticated, IsPatient]

    def get(self, request):
        appointments = Appointment.objects.filter(patient=request.user)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

 
class DoctorAppointmentListView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor]

    def get(self, request):
        appointments = Appointment.objects.filter(doctor=request.user)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)