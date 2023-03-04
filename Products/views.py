from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import *


class MenProductList(ListView):
    model = MenProduct
    extra_context = {'brands': Brand.objects.all(
    ), 'categories': Category.objects.all()}

class MenProductDetail(DetailView):
    model = MenProduct
    template_name='Products/product_detail.html'
    # extra_context = {'brands': Brand.objects.all(
    # ), 'categories': Category.objects.all()}



class WomenProductList(ListView):
    model = WomenProduct
    extra_context = {'brands': Brand.objects.all(
    ), 'categories': Category.objects.all()}
    
    
class WomenProductDetail(DetailView):
    model = WomenProduct
    template_name='Products/product_detail.html'

    # extra_context = {'brands': Brand.objects.all(
    # ), 'categories': Category.objects.all()}

def About_view(request):
    data=About.objects.all()
    context={'about':data}
    return render(request ,'Products/about.html',context)