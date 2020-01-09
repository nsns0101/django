from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.utils import timezone

class User(AbstractBaseUser):
    user_id = models.CharField(max_length=30)               #아이디
    email= models.TextField(unique=True)                    #이메일
    username = models.CharField(max_length=20)              #이름
    password = models.TextField()                           #비밀번호
    created_at = models.DateTimeField(auto_now_add=True)    #생성날짜
    updated_at = models.DateTimeField(auto_now=True)        #업데이트 날짜
    gender = models.CharField(max_length=1, null=True)      #성별
    last_login = models.DateTimeField(default=timezone.now, verbose_name='last login')
    # is_anonymous = models.BooleanField(default=True)        #현재 로그아웃중인지를 판단 True = 로그아웃
    # is_authenticated = models.BooleanField(default=False)   #현재 로그인 중인지를 판단 False = 로그아웃중
    # salt = models.CharField(verbose_name=('Salt'),max_length=10,blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()
#성별 필드 추가
    # CHOICES = (('M', '남자'), ('W', '여자'))
    # gender = forms.ChoiceField(
    #     required = True,
    #     widget=forms.RadioSelect, choices=CHOICES, label='성별'
    # )
    # class Meta:
    #     model = User                                                #사용할 모델설정
    #     fields = {"user_id","username", "email", "password", "password_check"}   #사용할 필드설정
    def __str__ (self): 
        return self.user_id

    



