from django.shortcuts import render
from . import templates
tasks = ["cook","study","tvd"]

# Create your views here.

def index(request):
    return render(request,"tasks/index.html",{"tasks":tasks})

def add(request):
    return render(request,"tasks/add.html",{
        "tasks":tasks
    })