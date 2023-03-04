from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'Products'


urlpatterns = [
    path('menProducts', MenProductList.as_view(), name='men_list'),
    path('womenProducts', WomenProductList.as_view(), name='women_list'),
]
