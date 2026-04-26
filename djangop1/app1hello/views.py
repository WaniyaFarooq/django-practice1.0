from django.http import HttpResponse
from django.shortcuts import render
from . import templates

# Create your views here.
def index(request):  #take an arg   arg ->repersent http request 
    #return HttpResponse("Hello, world")
    return render(request,"app1/index.html")

#kab run krna h y function us k liy we have to add url jo visit krny par y function run ho ga
def waniya(request):
    return HttpResponse("Hello,Waniyaa Farooq!")
 

def greet(request,name):
    # instead return HttpResponse(f"HELLO,{name.capitalize()}")
    return render(request,"app1/greet.html",{
        "name":name.capitalize()
    })