from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect  #Response와 Redirect할 수 있게 선언
from .models import Candidate, Poll, Choice               #현재 파일경로의 models.py의 Candidate를 import
import datetime                                           #날짜 함수를 쓰기 위해 선언해야함
from django.db.models import Sum                          #Sum 함수를 쓰기 위해 선언해야함

def index(request):
    candidates = Candidate.objects.all()    #Candidate모델의 모든 행을 변수에 저장
    context = {'candidates' : candidates}   #context에 'condidates'라는 key로 변수 candidates를 저장
    return render(request, 'elections/index.html', context)  #elections/index.html에 context 객체를 전달

#출마지역
def areas(request, area):   #area는 areas.html에서 하이퍼링크로 누른 area가 들어옴
    today = datetime.datetime.now()       #현재 시간

    #get은 찾고자하는 값이 없을 때 error를 발생. 그래서 try~except문으로 감싸주어야함
    try:
        #start_date__lte = today           => start_date <= today
        #end_date__gte = today             => end_date >= today
        #get은 하나의 객체만 리턴함
        poll = Poll.objects.get(area = area, start_date__lte = today, end_date__gte = today) # get에 인자로 조건을 전달해줍니다. 
        candidates = Candidate.objects.filter(area = area) # Candidate의 area와 매개변수 area가 같은 객체만 불러오기
    except:
        poll = None
        candidates = None

    context = {
        'candidates' : candidates,
        'area' : area,
        'poll' : poll
    }
    return render(request, 'elections/area.html', context)

#
def polls(request, poll_id):
    poll = Poll.objects.get(pk = poll_id)   #Poll객체를 구분하는 기본키인 poll_id를 담음
    selection = request.POST['choice']      #choice는 html의 form의 name과 관련
                                            #보낸 candidate_id를 받음

    try:    #두번째 투표인 경우
        #
        choice = Choice.objects.get(poll_id = poll.id, candidate_id = selection)
        choice.votes += 1   #투표 1증가
        choice.save()       #votes +1된 값을 db에 저장

    except: #try의 get문의 반환값이 없을 때(최초로 투표할 경우)
        #최초로 투표하는 경우, DB에 저장된 Choice객체가 없기 때문에 Choice를 새로 생성   
        choice = Choice(poll_id = poll.id, candidate_id = selection, votes = 1)
        choice.save()

    return HttpResponseRedirect("/areas/{}/results".format(poll.area))   #밑의 results의 area에 poll.area에 들어감

def results(request, area):
    candidates = Candidate.objects.filter(area = area)

    polls = Poll.objects.filter(area = area)    

    poll_results = []
    for poll in polls:
        result = {}                             #result 초기화
        result['start_date'] = poll.start_date  #연관배열에 시작날짜 입력
        result['end_date'] = poll.end_date      #연관배열에 종료날짜 입력
        #투표한 것을 Choice 모델에 저장하였고(45~48줄) 그 안에서 poll_id와 같은 것들을 가져옴
        total_votes = Choice.objects.filter(poll_id = poll.id).aggregate(Sum('votes'))

        poll_results.append(result)             #poll_results배열에 추가

        context = {
        'candidates' : candidates, 
        'area' : area,
        'poll_results' : poll_results
        }
    return render(request, 'elections/result.html', context)
