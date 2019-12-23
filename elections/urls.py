from django.urls import path
from . import views             # .은 현재 폴더  (현재폴더의 views를 import)
urlpatterns = [
    path('', views.index),
]