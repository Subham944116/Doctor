from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=Profile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username','password', 'role']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        role = validated_data.pop('role')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user,role=role)
        return user
      
class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields =  ["specialization", "experience_years"]
    