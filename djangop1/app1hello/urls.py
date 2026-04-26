from django.urls import path

from . import views


urlpatterns =[
    path("",views.index, name="index"),
     path("waniya",views.waniya, name="waniya"),
      path("<str:name>",views.greet, name= "greet"),
]