from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
# Create your models here.      #이 외에도 주민등록번호, 우편번호, 전화번호 등
class MyUser(AbstractBaseUser,PermissionsMixin):
    name= models.CharField(max_length=20, verbose_name ='이름')      
    email= models.EmailField(max_length=30, unique=True, verbose_name ='이메일')                   
    user_id = models.CharField(max_length=20, unique=True, verbose_name ='아이디') 
    password = models.CharField(max_length=20)  
    # gender = models.BooleanField(max_length=1, verbose_name='성별')  
    # address = models.TextField(verbose_name='주소')                
    # phone = models.IntegerField(max_length=11,verbose_name='핸드폰')
    # birthday = models.CharField(max_length=8, verbose_name='생일')               
    data_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입일')
    # is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
    # is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')


    # objects = MyUserManager()

    #유저 모델에서 필드의 이름을 설명하는 string. 유니크 식별자로 사용
    USERNAME_FIELD = 'user_id'

    #createsuperuser 커맨드로 유저를 생성할 때 나타날 필드 이름 목록
    REQUIRED_FIELDS = ['name']

    def get_short_name(self):
        return self.user_id
    
    def get_full_name(self):
        return self.user_id

    def get_username(self):
        return self.user_id

#User Model을 관리해줄 Manager
class MyUserManager(BaseUserManager):
    """
    전달된 데이터로 유저를 생성하고 저장합니다.
    """
    def create_user(self, user_id, name, password):
        if not user_id:
            raise ValueError('아이디를 적어주세요')

        user = self.model(
            user_id = user_id,
            name = name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, user_id, name, password):
        """
        전달된 데이터로 관리자를 생성하고 저장합니다.
        처음은 manage.py를 이용해서 만듬(createsuperuser)
        """
        user = self.create_user(user_id,name,password)
        user.is_superuser = True
        user.save(using=self._db)
        return user

