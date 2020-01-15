from django.shortcuts import render
from .forms import ProductForm
from .models import Product


def product_all(request):
    # print(request.POST.get('product_name'))
    product_form = ProductForm(request.POST, request.FILES)
    print(product_form)

    if product_form.is_valid():
        print("굿")
        product_form.save(commit=False)
        print(product_form.cleaned_data['product_image'])
        product_form.cleaned_data['product_image'] = request.FILES['product_image']
        product_form.save()
    return render(request, 'home/index.html')


def man_fashion(request):
    # 로그인 유저가 있는 경우
    try:
        man_fashions = Product.objects.filter(product_category="man_fashion")
        print(man_fashions)
    except:
        man_fashions = None

    return render(request, 'product/man_fashion.html', {'man_fashions': man_fashions})
