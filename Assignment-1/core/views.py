from django.http import HttpResponse
import json
from .models import Event
from django.vies
def home(request):
    return HttpResponse("welcome to home page")

def about(request):
    return HttpResponse("welcome to about page")