
# from django.shortcuts import render
# from rest_framework import generics

from rest_framework import viewsets

from housing_app import models
from .serializers import HousingSerializer

class HousingViewSet(viewsets.ModelViewSet):
    queryset = models.housing_data.objects.all()
    serializer_class = HousingSerializer

#**** Below is the first version (per the tutorial)

# class ListHousing(generics.ListCreateAPIView):
#     queryset = models.housing_data.objects.all()
#     serializer_class = HousingSerializer

# class DetailHousing(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.housing_data.objects.all()
#     serializer_class = HousingSerializer