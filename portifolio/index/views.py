from django.shortcuts import render
from .models import about

# Create your views here.

def home(request):
    aboutdata = about.objects.all()
    context = {
        'about':aboutdata
    }
    return render(request,'index.html', context)

def about(request):
    
    
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')