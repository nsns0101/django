#Project의 Main Controller

from django.urls import path
from . import views  #django 내장 로그인 기능사용하기 위해 선언


urlpatterns = [
    path('login/', views.login, name = 'login'),          #로그인
    path('logout/', views.logout, name = 'logout'),       #로그아웃
    path('register/', views.signup, name='signup'),
]


