from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {  # 필수항목 지정
            "product_category",
            "product_name",
            "product_quantity",
            "product_price",
            "product_sale",
            "product_image",
            "product_area",
            "product_made",
            "product_order_number",
            "product_seller",
        }
    product_sale = forms.CharField(required=False)
    product_area = forms.CharField(required=False)
    product_made = forms.CharField(required=False)
    product_order_number = forms.IntegerField(required=False)
    product_seller = forms.CharField(required=False)
    product_image = forms.ImageField(required=True)
