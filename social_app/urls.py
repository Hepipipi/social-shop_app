
#
# from django.urls import path, include
# from .views import social_main_page
#
#
# urlpatterns = [
#     path('', social_main_page),
#



from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import social_main_page

urlpatterns = [
    path('', social_main_page),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='sociaty/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='sociaty/logout.html'), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),

    path('post/create', views.create_post, name='create_post'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('add/comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('feed/', views.feed, name='social_feed'),



]





