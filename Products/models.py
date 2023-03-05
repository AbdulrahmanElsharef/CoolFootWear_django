from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# from django.utils.translation import gettext as _
from django.utils.text import slugify
# Create your models here.
PRODUCT_WIDTH = (('wide', 'wide'), ('medium', 'medium'), ('narrow', 'narrow'))
PRODUCT_MATERIAL = (('Leather', 'Leather'), ('Rubber', 'Rubber'), ('Textiles',
                                                                   'Textiles'), ('Synthetics', 'Synthetics'), ('Foam', 'Foam'))
PRODUCT_SIZE = (('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'),
                ('42', '42'), ('43', '43'), ('44', '44'))
PRODUCT_COLOR = (('Black', 'Black'), ('White', 'White'), ('Blue', 'Blue'), ('Red', 'Red'), ('Green', 'Green'),
                 ('Grey', 'Grey'),
                 ('Orange', 'Orange'),
                 ('Cream', 'Cream'),
                 ('Brown', 'Brown'),)

# PRODUCT_Category = (('FORMAL', 'FORMAL'), ('CASUALS',
#                     'CASUALS'), ('SPORTS', 'SPORTS'))


class Brand(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='Brand')
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='Category')
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    subtitle = models.TextField(max_length=300)
    brand = models.ForeignKey(Brand, related_name='Product_Brand',
                              on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='Product_Category',
                                 on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='Product_Images')
    width = models.CharField(max_length=25, choices=PRODUCT_WIDTH)
    martial = models.CharField(max_length=25, choices=PRODUCT_MATERIAL)
    style = models.CharField(max_length=25)
    description = models.TextField(max_length=1000)
    manufacturer = models.TextField(max_length=1000)
    tag = TaggableManager()
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class ProductReview(models.Model):
    user = models.ForeignKey(User, related_name='user_Review',
                             on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,  related_name='Product_Review')
    rate = models.IntegerField()
    review = models.TextField(max_length=500)

    def __str__(self):
        return str(self.product)


class ProductSize(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='Product_Size')
    size = models.CharField(max_length=50, choices=PRODUCT_SIZE)

    def __str__(self):
        return str(self.product)


class ProductColor(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='Product_Color')
    color = models.CharField(max_length=50, choices=PRODUCT_COLOR)

    def __str__(self):
        return str(self.product)


class ProductImages(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='Product_Images')
    image = models.ImageField(upload_to='products_image')

    def __str__(self):
        return str(self.product)


class MenProduct(Product):
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MenProduct, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class WomenProduct(Product):
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(WomenProduct, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class About(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='About')
    description = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.title)
