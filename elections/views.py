from django.shortcuts import render

from django.http import HttpResponse
from .models import Candidate               #현재 파일경로의 models.py의 Candidate를 import

def index(request):
    candidates = Candidate.objects.all()    #Candidate모델의 모든 행을 변수에 저장
    str = ''
    for candidate in candidates:
        str += "<p>{} 기호{}번({})<br>".format(
            candidate.name,
            candidate.party_number,
            candidate.area)
        str += candidate.introduction + "</p>"

    return HttpResponse(str)
