from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the academics index.")

def listPersons(request):
    return HttpResponse("List of persons")

# Create your views here.
