from django.http import HttpResponse

def home(request):
    return HttpResponse("it's your home page")

def about(request):
    data = 'qualquer dado'
    return HttpResponse(data)

def contact(request):
    return HttpResponse("it's your contact page")