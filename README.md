---
Django 프로젝트 기본

#프로젝트 파일 생성
django-admin startproject <파일명>

#서버 실행
python manage.py runserver

#app 만들기
python manage.py startapp <앱이름>

#migrations 파일 생성
python manage.py makemigrations

#DB에 migrations파일 연결
python manage.py migrate

#유저 생성
python manage.py createsuperuser

#shell로 DB조작 + 사용법
python manage.py shell      #php의tinker역할
   => from elections.models import Candidate       #elections/models.py의 Candidate 모델을 import
   => Candidate.objects.all()      #Candidate 모델을 검색(__str__로 name만 검색됨)
   => new_candidate = Candidate(name = "루비오")    #"루비오"라는 name을 가진 행을 생성
   => new_candidate.save()         #DB에 저장
   => Candidate.objects.all()      #모델 검색시 "루비오"가 추가 되어 있을 것임
   => no1 = Candidate.objects.filter(party_number = 1) #party_number이 1인 행을 no1에 저장 (filter은 mysql의 where문)
   => no1   #위에서 가져온 데이터가 출력됨 __str__로 인해서 name만 뜰 것임
   => no1[0].party_number 또는 no1[0].introduction으로 검색 가능    #배열로 붙이는 것은 29번째줄에서 여러행을 받았을 수도 있으니 default는 배열


#DB를 MySql로 셋팅하기(settings.py 참고)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   #쓸 DB
        'NAME': 'mysite',                       #DB명
        'USER' : 'root',                        #SQL ID
        'PASSWORD' : 'node',                    #SQL PASSWORD
        'HOST' : 'localhost',                   #HOST
        'PORT' : '',                            #PORT(생략시 localhost:8000)
        'CHARSET' : 'utf8',                     #utf8설정
        'COLLATION' : 'utf8_general_ci',
    }
}

#MySql UTF-8 설정방법(MySql에서 실행)
set character_set_client =utf8;

set character_set_connection = utf8;

set character_set_database = utf8;

set character_set_filesystem = utf8;

set character_set_results = utf8;

set character_set_server = utf8;

