from django.shortcuts import render
from . import templates
import datetime

# Create your views here.
def isnewyear(request):
     now = datetime.datetime.now()
     return render(request,"newyear/isnewyear.html",{
         "n":now.month ==1 and now.day ==1
     })