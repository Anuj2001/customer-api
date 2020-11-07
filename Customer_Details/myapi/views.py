from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Customerserializer
from .models import Customer
# Create your views here.

class CustomerSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('name')
    serializer_class = Customerserializer