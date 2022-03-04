from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    text = {
        'name':'Geovani',
        'age':30,
        'phone': 2342445,
        'friend_name': ['fabio','Nam','Jhonatan']
    }
    return render(request,'index.html', text)

def about(request):
    data = 'qualquer dado'
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')