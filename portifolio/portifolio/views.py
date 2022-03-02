from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def about(request):
    data = 'qualquer dado'
    return HttpResponse(data)

def contact(request):
    return HttpResponse("it's your contact page")