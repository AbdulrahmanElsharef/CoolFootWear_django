from django.contrib import admin
from .models import *


class ProductSizeInline(admin.TabularInline):
    model = ProductSize


class ProductColorInline(admin.TabularInline):
    model = ProductColor


class ProductImagesInline(admin.TabularInline):
    model = ProductImages


class ProductReviewInline(admin.TabularInline):
    model = ProductReview


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizeInline, ProductColorInline,
               ProductImagesInline, ProductReviewInline]

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author']
#     list_filter = ['tags', 'slug']
#     search_fields = ['title', 'contents']

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(About)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSize)
admin.site.register(ProductColor)
admin.site.register(ProductImages)
admin.site.register(ProductReview)
