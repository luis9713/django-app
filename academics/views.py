from django.shortcuts import render
from django.http import HttpResponse

from academics.models import User

def index(request):
    return HttpResponse("Hello, world. You're at the academics index.")

def listPersons(request):
    return HttpResponse("List of persons")


def list_users(request):
    users= User.objects.all()
    return render(request, 'academics/list_users.html', {'users': users})
# Create your views here.
