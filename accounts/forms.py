from django.contrib.auth.models import User
from django import forms

# class RegisterForm(forms.ModelForm):    #장고에서 제공하느
#     password = forms.CharField(label="Password", widget=forms.PasswordInput)    #비밀번호
#     password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)    #비밀번호 확인

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']

#     #비밀번호 확인 실패시
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords not matched!!')
#         return cd['password2']

    