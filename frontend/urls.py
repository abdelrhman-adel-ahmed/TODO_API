from django.contrib import admin
from django.urls import include, path

from .views import *

app_name = "frontend"
urlpatterns = [
    path("", list, name="list"),
]
