from django.urls import path, include
from .views import shop_main_page

urlpatterns = [
    path('', shop_main_page),

]


