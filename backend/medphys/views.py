from django.shortcuts import render
from rest_framework import viewsets
from .serializers import radSourceRecSerializer
from .models import radioactiveSourcePackageReception

# Create your views here.

class radSourceRecView(viewsets.ModelViewSet):
    serializer_class = radSourceRecSerializer
    queryset = radioactiveSourcePackageReception.objects.all()
