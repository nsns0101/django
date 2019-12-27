#Project의 Main Controller

from django.contrib import admin
from django.urls import path
from django.conf.urls import include   #include를 쓰기위해 import해야함
from django.conf.urls import (
    handler400, handler404, handler500
)
urlpatterns = [
    path('', include('elections.urls')),
    path('admin/', admin.site.urls),

]

handler400 = 'elections.views.error_400'
handler404 = 'elections.views.error_404'
handler500 = 'elections.views.error_500'
