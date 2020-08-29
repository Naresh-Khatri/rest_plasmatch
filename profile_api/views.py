from django.shortcuts import render
from . import models
from . import serializers
#from .permissions import UpdateOwnProfile, UpdateOwnTodo


from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class DonorProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DonorProfileSerializer
    queryset = models.DonorProfile.objects.all()


class PatientProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PatientProfileSerializer
    queryset = models.PatientProfile.objects.all()


class CustomObtainAuthToken(ObtainAuthToken):

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'email': user.email,
            'name': user.name,
            'avatar': user.avatar,
        })
