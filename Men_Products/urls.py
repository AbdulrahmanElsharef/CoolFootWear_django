from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'Men_Products'


urlpatterns = [
    path('men_products', MenProductList.as_view(), name='men_product_list'),
]
