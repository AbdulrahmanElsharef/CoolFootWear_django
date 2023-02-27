from django.contrib import admin
from .models import *


class ProductSizeInline(admin.TabularInline):
    model = ProductSize


class ProductColorInline(admin.TabularInline):
    model = ProductColor


class ProductImagesInline(admin.TabularInline):
    model = ProductImages


class WomenProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizeInline, ProductColorInline, ProductImagesInline]


admin.site.register(WomenProduct, WomenProductAdmin)
admin.site.register(ProductSize)
admin.site.register(ProductColor)
admin.site.register(ProductImages)
admin.site.register(ProductReview)
admin.site.register(Category)
