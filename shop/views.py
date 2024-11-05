from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import Add_CartForm
from .models import Product, Category, slugify, Cart, CartItem


# Create your views here.
def all_products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'shop/index.html', context)


def all_category(request):
    category = Category.objects.all()

    context = {
        'categories': category
    }
    return render(request, 'shop/categories.html', context)




# def product_list(request, category_slug):
#     category = Category.objects.all()
#     products = Product.objects.all()
#
#
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     # p = Product.objects.all()
#     #
#     # context = {
#     #     'products': p
#     # }
#     return render(request, 'shop/d_cate.html', products)


from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request, category_slug):
    # Получаем категорию по slug
    category = get_object_or_404(Category, slug=category_slug)
    # Получаем все продукты, относящиеся к данной категории
    products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'products': products
    }
    return render(request, 'shop/d_cate.html', context)


def my_cart(request):
    cart = Cart.objects.get(user=request.user)
    cartitems = CartItem.objects.filter(cart=cart)
    context = {
        'cart': cart,
        'cartitems': cartitems

    }
    return render(request, 'shop/my_cart.html', context)




def add_to_cart(request, product_id):
    if request.method == 'POST':
        cart, _ = Cart.objects.get_or_create(user=request.user)

        product = Product.objects.get(id=product_id)
        cartitem = CartItem.objects.create(cart=cart, product=product, amount=product.price, quantity = 1)
        print(cart)
    return redirect('my_cart')

























