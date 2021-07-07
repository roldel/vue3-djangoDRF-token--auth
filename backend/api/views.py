from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def home(request):
    pass


@api_view()
def responsetest(request):
    return Response({"message": "Hello, world!"})