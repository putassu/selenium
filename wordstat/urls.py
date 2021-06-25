from django.contrib import admin
from django.urls import path, include
from wordstat.views import *
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path("", (get_history)),
]
