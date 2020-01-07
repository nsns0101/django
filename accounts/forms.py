
from django import forms
from .models import MyUser
from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm
)
# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(label='password')
#     password_check = forms.CharField(label='password_check')
#     print(password)
#     print(password_check)
#     class Meta:
#         model = MyUser
#         fields = ['name', 'email','user_id', 'password', ]#'gender', 'address', 'phone'
#         widgets = {
#             'name' : forms.TextInput(attrs={
#                 'class' : 'form-control', 
#                 'placeholder' : '20자 이내로 입력가능합니다'
#             }),
#             'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
#             'user_id': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder' : '30자 이내로 입력가능합니다'
#             }),
#             'password' : forms.PasswordInput(attrs={'class' : 'form-control'}),
#         }
#         labels = {
#             'name' : '닉네임',
#             'email' : '이메일',
#             'password' : '비밀번호'
#         }
#     # def clean_password2(self):
#     #     cd = self.cleaned_data
#     #     if cd['password'] != cd['password2']:
#     #         raise forms.ValidationError('패스워드가 일치하지 않습니다.')
#     #     return cd['password2']

#     def __init__(self, *args, **kwargs):
#         super(RegisterForm, self).__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs['maxlength'] = 20
#         self.fields['user_id'].widget.attrs['maxlength'] = 30
    
class MyUserCreationForm(UserCreationForm):
    # custom Form Field
    # 기존의 gender 필드를 대체함
    CHOICE = (('M', '남자'), ('W', '여자'))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICE, label='성별')

    class Meta:
        model = MyUser
        fields = ('user_id',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password don`t match')

        return password2

    def save(self, commit=True):
        # 비밀번호를 해시형태로 저장
        user = super(MyUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


    class MyUserChangeForm(UserChangeForm):
        # 유저 업데이트 폼
        # 모든 필드 포함, 비밀번호는 해시로 표시

        password = ReadOnlyPasswordHashField(label="비밀번호")
        class Meta:
            model = MyUser
            fields = ('user_id',)
