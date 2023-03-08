from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'Products'


urlpatterns = [
    path('home', Home.as_view(), name='home'),
    path('products/', ProductList.as_view(), name='Product_list'),
    path('products/<slug:slug>', ProductDetail.as_view(), name='Product_detail'),
    path('brands', BrandList.as_view(), name='brands'),
    path('brands/<slug:slug>', BrandDetail.as_view(), name='brand_detail'),
    path('catagories', CategoryList.as_view(), name='catagories'),
    path('catagories/<slug:slug>', CategoryDetail.as_view(),
         name='catagories_detail'),
    path('about', About_view, name='about')
]
