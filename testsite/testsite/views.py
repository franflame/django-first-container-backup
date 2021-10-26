from django.http import HttpResponse
from . import urls

def index(request):
    return HttpResponse("Hello, world. You're at Isaac's index page.")

def alternate(request):
    return HttpResponse("This is the alternate page.")