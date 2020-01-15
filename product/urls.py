# Project의 Main Controller

from django.urls import path
from . import views  # django 내장 로그인 기능사용하기 위해 선언


urlpatterns = [
    path('all', views.product_all, name='prodcut_all'),
    # 카테고리별 사이트로 여기서 해야하나?
    # 옷도 엄청 종류가 많고 음식도 종류가 많은데 앱으로 둘지?
    path('man_fashion', views.man_fashion, name='man_fashion'),  # 남성 옷
    # path('woman_fashion', views.woman_fashion, name = 'woman_fashion')  #여성 옷
    # path('food', views.food, name = food)

]
