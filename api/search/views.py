from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializer import PersonSerializer
from .models import *
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.all().order_by('id')
    serializer_class = PersonSerializer

