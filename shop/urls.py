from django.urls import path, include

from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('all_category/', views.all_category, name='all_category'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('my_cart/', views.my_cart, name='my_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),


    ]



