from django.shortcuts import render
from rest_framework import generics
from biodata.models import Profile
from biodata.serializers import ProfileSerializer

# Create your views here.
class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
