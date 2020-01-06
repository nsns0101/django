from django.db import models

# Create your models here.
class User(models.Model):
    name= models.CharField(max_length=20)       #이름
    email= models.TextField()                   #이메일
    gender = models.BooleanField(default=True)  #성별
    user_id = models.CharField(max_length=30)   #아이디
    password = models.CharField(max_length=20)  #비밀번호
    address = models.TextField()                #주소
    phone = models.IntegerField()               #휴대폰 번호

#이 외에도 주민등록번호, 우편번호, 전화번호 등
