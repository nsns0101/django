
from django import forms                        #장고의 form 기능 사용
from django.contrib.auth.forms import UserCreationForm
from .models import User     #장고의 user 모델 사용

    
class SignupForm(forms.ModelForm):
#아이디 필드 추가
    user_id = forms.CharField(label =(""), max_length=30,
            help_text=("Required. 30 characters or fewer. Letters, digits and "),
            error_messages={
                'invalid' : ("This value may contain only letters, numbers")
            },
            widget= forms.TextInput(
                 attrs={            #attrs : HTML에 보여지는 태그의 속성을 정의하는 것
                'class' : 'form-control',   
                'placeholder' : '아이디',    
                'required' : 'True',        #필수입력 default가 True라 써주지 않아도 되긴함
            }))
#이메일 필드 추가
    email = forms.EmailField(label=(""),           #form필드 : 데이터베이스의 필드 구조
        required = True,
        widget=forms.EmailInput(        #widget필드 : 화면에 보여지는 입력 양식
            attrs={            #attrs : HTML에 보여지는 태그의 속성을 정의하는 것
                'class' : 'form-control',   
                'placeholder' : '이메일',    
                'required' : 'True',        #필수입력 default가 True라 써주지 않아도 되긴함
            }
        )
    )
#유저이름 필드 추가
    username = forms.CharField(label =(""), max_length=30,
            help_text=("Required. 30 characters or fewer. Letters, digits and "),
            error_messages={
                'invalid' : ("This value may contain only letters, numbers")
            },
            widget= forms.TextInput(
                 attrs={            #attrs : HTML에 보여지는 태그의 속성을 정의하는 것
                'class' : 'form-control',   
                'placeholder' : '이름',    
                'required' : 'True',        #필수입력 default가 True라 써주지 않아도 되긴함
            }))
    password = forms.CharField(label=(""),
            widget = forms.PasswordInput(
                 attrs={            #attrs : HTML에 보여지는 태그의 속성을 정의하는 것
                'class' : 'form-control',   
                'placeholder' : '비밀번호',    
                'required' : 'True',        #필수입력 default가 True라 써주지 않아도 되긴함
            }
            ))
    password_check = forms.CharField(label=(""),
            widget = forms.PasswordInput(
                 attrs={            #attrs : HTML에 보여지는 태그의 속성을 정의하는 것
                'class' : 'form-control',   
                'placeholder' : '비밀번호 확인',    
                'required' : 'True',        #필수입력 default가 True라 써주지 않아도 되긴함
            }
            ),
            help_text = ("Enter the same password as above, for verification."))   

#성별 필드 추가
    # CHOICES = (('M', '남자'), ('W', '여자'))
    # gender = forms.ChoiceField(
    #     required = True,
    #     widget=forms.RadioSelect, choices=CHOICES, label='성별'
    # )


    class Meta:
        model = User                                                #사용할 모델설정
        fields = {"user_id","username", "email", "password", "password_check"}   #사용할 필드설정
