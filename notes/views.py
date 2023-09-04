from django.shortcuts import render
from django.http import response, HttpRequest, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. This is the first page in project)")
