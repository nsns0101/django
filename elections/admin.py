from django.contrib import admin

from .models import Candidate   #현재 파일경로의 models에서 Candidate모델을 import


admin.site.register(Candidate)      #admin경로에 접속시 Elections앱 안에 Candidate가 생길 것임