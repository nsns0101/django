from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse                     #
from .forms import SignupForm  # 회원가입 폼
from django.shortcuts import resolve_url
from .models import User  # 유저 모델
from django.shortcuts import redirect  # 리다이렉트
from django.contrib import auth  # 로그인, 로그아웃
from django.contrib.auth.decorators import login_required  # 로그인 한 사용자만 할 수 있도록
from django.contrib.auth.hashers import make_password
from .backends import OpencartBackend
from django.contrib.auth.hashers import make_password
import bcrypt  # 암호, 해독

# from django.contrib.auth.hashers import check_password


# 회원가입
def signup(request):

    # 로그인 중이면 리다이렉트
    try:
        if request.user.user_id:
            return HttpResponseRedirect(resolve_url('/'))
    except:
        pass

    # 회원가입 요청
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        print("POST방식")

        # bcrypt.hashpw(user.password.encode('utf8'), bcrypt.gensalt())     #암호화
        # bcrypt.checkpw(user.password.encode('utf8'), password_encode)     #복호화
        # 폼 자체에서 유효성검사를 하고
        if signup_form.is_valid():  # form.is_valid  모든 form에 데이터가 채워져 있다면
            print("모든값이 채워짐")
            # 아직 db에 저장하지마!(commit이 되야 저장되기 때문)
            user = signup_form.save(commit=False)
            # 유효성 검사 된 것을 email 추가로s 저장
            user.email = signup_form.cleaned_data['email']
            user.password = signup_form.cleaned_data['password']
            user.password_check = signup_form.cleaned_data['password_check']
            # 비밀번호 확인 오류시
            if user.password == user.password_check:
                user.password = bcrypt.hashpw(user.password.encode(
                    'utf8'), bcrypt.gensalt(12))  # 비밀번호 암호화
                user.save()
                return HttpResponseRedirect(resolve_url('/'))
            else:
                return render(request, 'registration/signup.html', {"signup_form": signup_form})
        return render(request, 'home/index.html')
    # #회원가입페이지 GET
    else:
        print('GET방식')
        signup_form = SignupForm()
        return render(request, 'registration/signup.html', {"signup_form": signup_form})


def login(request):
    # 로그인 중이면 리다이렉트
    try:
        if request.user.user_id:
            return HttpResponseRedirect(resolve_url('/'))
    except:
        pass

    if request.method == "GET":
        return render(request, 'registration/login.html')

    elif request.method == "POST":
        # 전송받은 아이디와 비밀번호를 확인
        user_id = request.POST.get('user_id')
        print(user_id)
        password = request.POST.get('password')
        OpencartBackenda = OpencartBackend()
        u = OpencartBackenda.authenticate(user_id, password)
        print(u)
        # 유효성 처리
        res_data = {}
        if not (user_id and password):
            res_data['error'] = "모든 칸을 입력해주세요"
        else:
            # try:
                    # 기존 (DB)에 있는 User모델과 같은 값인지 확인하여 가져옴
                # db_user = User.objects.get(user_id = user_id) #필드명 = 값
                    # 비밀번호가 맞는지 확인한다. 위의 check_password를 참조
            # if password == db_user.password:
                # 응답 데이터 세션에 값 추가. 수신측 쿠키에 저장됨.
                # request.session['user'] = db_user.user_id
            # 'django.contrib.auth.backends.ModelBackend'참고

            auth.login(request, user=u)
            return redirect('/')
            # else:
            #     res_data['error'] = "비밀번호가 틀렸습니다"

            # except:
            # res_data['error'] = "아이디를 확인해주세요"

        # 응답 데이터 res_data를 전달
        return render(request, 'registration/login.html', {"res_data": res_data})


@login_required(login_url='/')  # 로그인 한 유저만 접근 가능
def logout(request):
    auth.logout(request)
    return redirect('/')
