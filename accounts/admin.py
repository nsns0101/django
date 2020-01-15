from django.contrib import admin
from .models import User

#     # 이제 새로운 UserAdmin을 등록합니다.
admin.site.register(User)

#     # 그리고, 우리는 장고의 built-in 허가를 사용하고 있지 않으므로,
#     # admin에서 Group model을 제거합니다.
#     admin.site.unregister(Group)
