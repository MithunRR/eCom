

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='eBhandar'),
    path('about', views.about, name='AboutUs'),
    path('contact', views.contact, name='ContactUs'),
    path('orders', views.orders, name='Orders'),
    path('tracker', views.tracker, name='TrackingStatus'),
    path('search', views.search, name='Search'),
    path('products/<int:myid>/', views.prodView, name='PruductView'),
    path('checkout', views.checkout, name='Checkout'),

    path("signup", views.signup, name='signup'),
    path("login", views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('view_cart', views.view_cart, name='ViewCart'),
    path('inc_cart/<int:product_id>/', views.inc_cart, name='inc_cart'),
    path('dec_cart/<int:product_id>/', views.dec_cart, name='dec_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('prodView_add_to_cart/<int:product_id>/', views.prodView_add_to_cart, name='prodView_add_to_cart'),


    path('thanks', views.thanks, name='thanks'),
    path('account', views.account, name='account'),
    path('profile', views.profile, name='profile'),
    path('address', views.address, name='address'),
    path('career', views.career, name='career'),
    path('shop_index', views.shop_index, name='shop_index'),


    path('vegetable', views.vegetable, name='vegetable'),


]