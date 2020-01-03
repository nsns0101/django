#Project의 Main Controller

from django.urls import path
from django.contrib.auth import views  #django 내장 로그인 기능사용하기 위해 선언
from .views import register     #현재경로의 views.py의 register class import

urlpatterns = [
    path('login/', views.LoginView.as_view(), name = 'login'),          #로그인
    path('logout/', views.LogoutView.as_view(template_name = 'registration/logout.html'), name = 'logout'),    #로그아웃
    path('register/', register, name='register'),
]


