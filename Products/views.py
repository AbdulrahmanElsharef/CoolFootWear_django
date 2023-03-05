from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import *


class MenProductList(ListView):
    model = MenProduct
    paginate_by = 30
    extra_context = {'brands': Brand.objects.all(
    ), 'categories': Category.objects.all()}


class MenProductDetail(DetailView):
    model = MenProduct
    template_name = 'Products/product_detail.html'



class WomenProductList(ListView):
    model = WomenProduct
    paginate_by = 30
    extra_context = {'brands': Brand.objects.all(
    ), 'categories': Category.objects.all()}


class WomenProductDetail(DetailView):
    model = WomenProduct
    template_name = 'Products/product_detail.html'



class BrandList(ListView):
    model = Brand
    paginate_by = 30


class BrandDetail(ListView):
    model = Product
    template_name = 'Products/brand_detail.html'
    paginate_by = 30

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset


class CategoryList(ListView):
    model =  Category
    paginate_by = 30


class  CategoryDetail(ListView):
    model = Product
    template_name = 'Products/category_detail.html'
    paginate_by = 30

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(category=category)
        return queryset
    
class  Home(ListView):
    model = Product
    template_name = 'Products/home.html'
    paginate_by = 16
    
    
def About_view(request):
    data = About.objects.all()
    context = {'about': data}
    return render(request, 'Products/about.html', context)
