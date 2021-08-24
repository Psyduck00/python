from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

#view function
def home(request):
    return HttpResponse("This is the home page")
