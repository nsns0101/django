#Project의 Main Controller

from django.contrib import admin
from django.urls import path
from django.conf.urls import include   #include를 쓰기위해 import해야함
from django.conf.urls import (
    handler400, handler404, handler500
)

handler400 = 'home.views.error_400'
handler404 = 'home.views.error_404'
handler500 = 'home.views.error_500'


urlpatterns = [
    path('admin/', admin.site.urls),        #admin
    path('', include('home.urls')),         #쇼핑몰 홈페이지
    path('accounts/', include('accounts.urls')),    #로그인 페이지
]


