from django.shortcuts import render

from django.http import HttpResponse
from .models import Candidate               #현재 파일경로의 models.py의 Candidate를 import

def index(request):
    candidates = Candidate.objects.all()    #Candidate모델의 모든 행을 변수에 저장
    context = {'candidates' : candidates}   #context에 'condidates'라는 key로 변수 candidates를 저장
    return render(request, 'elections/index.html', context)  #elections/index.html에 context 객체를 전달

#출마지역
def areas(request, area):   #area는 areas.html에서 하이퍼링크로 누른 area가 들어옴
    return HttpResponse(area)

