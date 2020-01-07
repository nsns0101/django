from django.shortcuts import render
from .forms import RegisterForm #현재 경로의 forms.py의 RegisterForm class를 import
from .models import User


#회원가입
def register(request):
    #회원가입 요청
    if request.method == 'POST':    
        user_form = RegisterForm(request.POST)
        # print(request)
        # print(user_form)
        if user_form.is_valid():    #form.is_valid  모든 form에 데이터가 채워져 있다면
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request,new_user)

            return render(request, '/', {'new_user'})
    # #회원가입페이지 GET
    else:
        user_form = RegisterForm()
        print("a")
        return render(request, 'registration/register.html')