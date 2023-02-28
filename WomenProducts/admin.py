from django.contrib import admin
from .models import *


class ProductSizeInline(admin.TabularInline):
    model = WomenSize


class ProductColorInline(admin.TabularInline):
    model = WomenColor


class ProductImagesInline(admin.TabularInline):
    model = WomenImages


class ProductReviewInline(admin.TabularInline):
    model = Women_Review


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizeInline, ProductColorInline,
               ProductImagesInline, ProductReviewInline]


admin.site.register(WomenProduct, ProductAdmin)
admin.site.register(WomenSize)
admin.site.register(WomenColor)
admin.site.register(WomenImages)
admin.site.register(Women_Review)
