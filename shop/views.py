from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def shop_main_page(request):
    return render(request, 'shop/index.html')

