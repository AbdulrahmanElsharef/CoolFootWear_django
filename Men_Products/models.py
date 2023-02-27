from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# from django.utils.translation import gettext as _
from django.utils.text import slugify
# Create your models here.
WIDTH = (('wide', 'wide'), ('medium', 'medium'), ('narrow', 'narrow'))
MATERIAL = (('Leather', 'Leather'), ('Rubber', 'Rubber'), ('Textiles',
            'Textiles'), ('Synthetics', 'Synthetics'), ('Foam', 'Foam'))
PRODUCT_SIZE = (('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'),
                ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'))
PRODUCT_COLOR = (('Black', 'Black'), ('White', 'White'), ('Blue', 'Blue'), ('Red', 'Red'), ('Green', 'Green'),
                 ('Grey', 'Grey'),
                 ('Orange', 'Orange'),
                 ('Cream', 'Cream'),
                 ('Brown', 'Brown'),)


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Men_Category')


class MenProduct(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    subtitle = models.TextField(max_length=300)
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='Men_Category')
    width = models.CharField(max_length=50, choices=WIDTH)
    martial = models.CharField(max_length=50, choices=MATERIAL)
    style = models.CharField(max_length=25)
    description = models.TextField(max_length=1000)
    manufacturer = models.TextField(max_length=1000)
    tag = TaggableManager()
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # Call the real save() method
        super(MenProduct, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class ProductSize(models.Model):
    men_product = models.ForeignKey(
        MenProduct, on_delete=models.CASCADE, related_name='Men_Size')
    size = models.CharField(max_length=50, choices=PRODUCT_SIZE)

    def __str__(self):
        return str(self.men_product)


class ProductColor(models.Model):
    men_product = models.ForeignKey(
        MenProduct, on_delete=models.CASCADE, related_name='Men_color')
    color = models.CharField(max_length=50, choices=PRODUCT_COLOR)

    def __str__(self):
        return str(self.men_product)


class ProductImages(models.Model):
    men_product = models.ForeignKey(
        MenProduct, on_delete=models.CASCADE, related_name='Men_image')
    image = models.ImageField(upload_to='men_Images')

    def __str__(self):
        return str(self.men_product)


class ProductReview(models.Model):
    user = models.ForeignKey(User, related_name='Men_user_Review',
                             on_delete=models.SET_NULL, null=True, blank=True)
    men_product = models.ForeignKey(
        MenProduct, on_delete=models.SET_NULL, null=True, blank=True, related_name='Men_Review')
    rate = models.IntegerField()
    review = models.TextField(max_length=500)

    def __str__(self):
        return str(self.men_product)
