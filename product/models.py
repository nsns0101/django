from django.db import models


# 파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
def product_image_path(instance, filename):
    print("gggggggggggggggggg")
    from random import choice
    import string  # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = filename.split('.')[0]+''.join(arr)  # 8자리 임의의 문자를 만들어 파일명으로 지정
    extension = filename.split('.')[-1]  # 파일확장자
    # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    # 예 : wayhome/abcdefgs.png
    return 'product/'+'%s/%s.%s' % (instance.product_category, pid, extension)


class Product(models.Model):
    product_category = models.CharField(max_length=20)  # 제품 카테고리
    product_name = models.CharField(max_length=30)  # 제품 명
    product_quantity = models.IntegerField()  # 제품 수량
    product_price = models.IntegerField()  # 제품 가격
    product_sale = models.IntegerField(default=0)  # 제품 할인율

    product_image = models.ImageField(upload_to=product_image_path)  # 제품 이미지
    product_area = models.TextField(default='Korea')  # 제품 만든 나라
    product_made = models.TextField()  # 제품 만든 장소
    product_created_at = models.DateTimeField(auto_now=True)  # 제품 입고일
    product_updated_at = models.DateTimeField(auto_now=True)  # 제품 변경일
    product_order_number = models.IntegerField(default=0)  # 주문 앱의 외래키
    product_seller = models.CharField(
        max_length=20, default="nsns0101")  # 판매자 앱의 외래키(판매자명)
