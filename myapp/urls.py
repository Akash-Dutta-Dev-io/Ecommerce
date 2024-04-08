from django.urls import path
from . import views
from .views import buy_post, add_to_cart

urlpatterns = [
    path('seller/register/', views.seller_register, name='seller_register'),
    path('seller/login/', views.seller_login, name='seller_login'),
    path('buyer/register/', views.buyer_register, name='buyer_register'),
    path('buyer/login/', views.buyer_login, name='buyer_login'),
    path('seller/home/', views.seller_home, name='seller_home'),
    path('buyer/home/', views.buyer_home, name='buyer_home'),
    path('seller/upload_product/', views.upload_product, name='upload_product'),
    path('buy/<int:post_id>/', buy_post, name='buy_post'),
    path('add_to_cart/<int:post_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('buy_now/<int:product_id>/', views.buy_now, name='buy_now'),
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('logout/', views.logout_view, name='logout'),

]
