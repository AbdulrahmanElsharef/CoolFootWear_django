from django.contrib import admin
from .models import *


class ProductSizeInline(admin.TabularInline):
    model = MenSize


class ProductColorInline(admin.TabularInline):
    model = MenColor


class ProductImagesInline(admin.TabularInline):
    model = MenImages


class ProductReviewInline(admin.TabularInline):
    model = MenReview


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizeInline, ProductColorInline,
               ProductImagesInline, ProductReviewInline]


admin.site.register(MenProduct, ProductAdmin)
admin.site.register(MenSize)
admin.site.register(MenColor)
admin.site.register(MenImages)
admin.site.register(MenReview)
admin.site.register(Brand)
