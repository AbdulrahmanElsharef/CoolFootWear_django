from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'Products'


urlpatterns = [
    path('menProducts', MenProductList.as_view(), name='men_list'),
    path('menProducts/<slug:slug>', MenProductDetail.as_view(), name='men_detail'),
    path('womenProducts', WomenProductList.as_view(), name='women_list'),
    path('womenProducts/<slug:slug>',
         WomenProductDetail.as_view(), name='women_detail'),
    path('about', About_view, name='about')
]
