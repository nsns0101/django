#Project의 Main Controller

from django.contrib import admin
from django.urls import path
from django.conf.urls import include   #include를 쓰기위해 import해야함

urlpatterns = [
    path('', include('elections.urls')),
]
