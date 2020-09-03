from django.contrib import admin
from django.urls import path, include
from . import views

from rest_framework import routers


router = routers.DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('DonorProfile', views.DonorProfileViewSet)
router.register('PatientProfile', views.PatientProfileViewSet)
router.register('SendMessage', views.MessageViewSet)


urlpatterns = [
    path('', include(router.urls))
]
