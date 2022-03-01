from django.http import HttpResponse

def home(request):
    return HttpResponse("it's your home page")

def about(request):
    return HttpResponse("it's your about page")

def contact(request):
    return HttpResponse("it's your contact page")