from django.db import models

# 선거 모델
class Candidate(models.Model):      #모델 등록을 위해 models.Model을 상속받아야함
    name = models.CharField(max_length=10)  #이름 문자의 최대길이는 10
    introduction = models.TextField()       #정보 문자열의 길이 제한이 없음
    area = models.CharField(max_length=15)  #국적
    party_number = models.IntegerField(default=1)  #기호 default값은 숫자 1