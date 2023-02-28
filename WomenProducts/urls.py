from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'WomenProducts'


urlpatterns = [
    path('WomenProducts', WomenProductList.as_view(), name='Women_product_list'),
]
