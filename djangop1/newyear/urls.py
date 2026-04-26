from django.urls import path
from . import views
urlpatterns = [
    path("isnewyear",views.isnewyear,name="isnewyear")
]