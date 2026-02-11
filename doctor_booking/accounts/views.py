from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics
from .perimission import IsDoctor
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import *

# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        serializers = RegisterSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"message":"Registered succesfully....✅"})



class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


class DoctorProfileListCreateView(generics.ListCreateAPIView):
    serializer_class = DoctorProfileSerializer
    permission_classes = [IsAuthenticated, IsDoctor]

    def get_queryset(self):
        return DoctorProfile.objects.filter(
            profile=self.request.user.profile
        )
    def perform_create(self, serializer):
        profile = self.request.user.profile

        if DoctorProfile.objects.filter(profile=profile).exists():
            raise ValidationError("Doctor profile already exists.")

        serializer.save(profile=profile)
    