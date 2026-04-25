from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):  #take an arg   arg ->repersent http request 
    return HttpResponse("Hello, world")

#kab run krna h y function us k liy we have to add url jo visit krny par y function run ho ga