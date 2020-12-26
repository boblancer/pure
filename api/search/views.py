from django.shortcuts import render
from django.http import HttpResponse
from .serializer import *
from .models import *
from rest_framework import mixins, viewsets, generics
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('id')
    serializer_class = PersonSerializer

class BookView(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, format=None):
        print(request.query_params)
        print("get route")
        b = Book.objects.all().order_by('id')
        res = []
        for i in b:
            res.append(self.serializer_class(i).data)
        return  JsonResponse(res, safe=False)


    def post(self, request, format=None):
        print(fields = self.context.get('request').query_params.get('fields'))
        b = [Book.objects.all().order_by('id')]
        return  Response("ello")
    



