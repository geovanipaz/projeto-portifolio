from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def employee(request):
    return HttpResponse("It's Employee page")

def profile(request):
    return HttpResponse("Its Profile page")