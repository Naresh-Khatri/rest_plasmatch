from . import models

from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id','email', 'password', 'first_name', 'last_name', 'age',
                    'gender', 'city', 'phone_no')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': { 'input_type': 'password' }
            }
        }


class DonorProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DonorProfile
        fields = '__all__'


class PatientProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PatientProfile
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Message
        fields = '__all__'
