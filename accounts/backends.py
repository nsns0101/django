#'django.contrib.auth.backends.ModelBackend'참고
#비밀번호 암호, 해독 
from hashlib import sha1

from .models import User
from django.contrib.auth.hashers import make_password
import bcrypt

class OpencartBackend:
    # Django 로그인 프로시저가 호출하는 인증 메소드
    def authenticate(self, user_id=None, password=None):
        try:
            # 커스텀 User 모델에서 이메일 주소를 username으로 사용한 경우
            user = User.objects.get(user_id=user_id)
            

            #비밀번호 암호화
            password_encode= bcrypt.hashpw(user.password.encode('utf8'), bcrypt.gensalt())

            #비밀번호 복호화해서 비교   Boolean값 출력
            password_decode = bcrypt.checkpw(user.password.encode('utf8'), password_encode)

            if password_decode:
                return user
            else:
                print('아휴')
                return None

        except User.DoesNotExist:
            print("어?")
            return None

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None