from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import *


class MenProductList(ListView):
    model = MenProduct
    extra_context = {'brands': Brand.objects.all(
    ), 'categories': Category.objects.all()}


class WomenProductList(ListView):
    model = WomenProduct
    extra_context = {'brands': Brand.objects.all(
    ), 'categories': Category.objects.all()}
