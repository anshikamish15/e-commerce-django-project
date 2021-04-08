from django.contrib import admin
from django.urls import path
from . import views

app_name = 'buyer'

urlpatterns = [
    path('home/', views.home),
    path('profile/', views.profile),
    path('filter/<int:id>/', views.filter, name='filter'),
    path('add_cart/<int:id>/', views.add_cart, name='cart'),
    path('cartdetails/', views.cartdetails),
    path('delcart/<int:id>/', views.delcart, name="delcart"),
    path('cartcalculate/', views.cartcalculate),
    path('myorder/', views.myorder)
]
