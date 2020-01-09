from django.contrib import admin

# Register your models here.
# class MyUserAdmin(UserAdmin):
#     """
#     필드들은 유저 모델을 표시하는데 사용됩니다.
#     auth.User의 특정 필드를 참조하는 UserAdmin을 오버라이드합니다.
#     """

#     #회원 업데이트 폼 연결
#     form = MyUserChangeForm
#     list_display = ('user_id', 'name', 'birthday', 'gender', 'email', 'phone', 'is_staff')
#     list_filter = ('is_staff', 'is_superuser', 'sex')
#     fieldsets = (
#         ('아이디', {'fields': ('user_id', 'password')}),
#         ('개인 정보', {'fields': ('name', 'birthday', 'gender', 'email', 'phone')}),
#         ('권한', {'fields': ('is_staff',)}),
#     )

#     # 회원 추가 폼 연결
#     add_form = MyUserCreationForm
#     add_fieldsets = (
#         ('기본 정보', {'fields': ('user_id', 'password1', 'password2')}),
#         ('추가 정보', {'fields': ('name', 'birthday', 'gender', 'email', 'phone')})
#     )

#     search_fields = ('user_id', 'name',)
#     ordering = ('name',)
#     filter_horizontal = ()

#     # 이제 새로운 UserAdmin을 등록합니다.
#     admin.site.register(MyUser, MyUserAdmin)

#     # 그리고, 우리는 장고의 built-in 허가를 사용하고 있지 않으므로,
#     # admin에서 Group model을 제거합니다.
#     admin.site.unregister(Group)


