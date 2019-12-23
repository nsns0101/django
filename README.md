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
