#home app의 Controller
from django.urls import path
from . import views             # .은 현재 폴더  (현재폴더의 views를 import)

app_name = 'home'  #layout.html참고

urlpatterns = [
    path('', views.index, name = 'home'),    #views.py파일의 index메서드 실행   name는 layout.html 참고
    # path('areas/<str:area>/',views.areas),   #area뒤에 string형 모든 글을 적을 수 있음
    # path('areas/<str:area>/results/',views.results),
    # path('polls/<str:poll_id>/', views.polls)   #

    
]