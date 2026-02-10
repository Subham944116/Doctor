from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        serializers = RegisterSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"message":"Registered succesfully"})
        