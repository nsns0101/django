#elections app의 Controller
from django.urls import path
from . import views             # .은 현재 폴더  (현재폴더의 views를 import)
urlpatterns = [
    path('', views.index),              #views.py파일의 index메서드 실행
    path('areas/<str:area>/',views.areas),   #area뒤에 string형 모든 글을 적을 수 있음
    path('polls/<str:poll_id>/', views.polls)   #
    
]