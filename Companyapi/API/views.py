from django.shortcuts import render
from rest_framework import viewsets
from API.models import Company
from API.serializers import CompanySerializer

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    