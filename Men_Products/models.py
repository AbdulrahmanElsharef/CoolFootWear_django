from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# from django.utils.translation import gettext as _
from django.utils.text import slugify
# Create your models here.
PRODUCT_WIDTH = (('wide', 'wide'), ('medium', 'medium'), ('narrow', 'narrow'))
PRODUCT_MATERIAL = (('Leather', 'Leather'), ('Rubber', 'Rubber'), ('Textiles',
                                                                   'Textiles'), ('Synthetics', 'Synthetics'), ('Foam', 'Foam'))
PRODUCT_SIZE = (('39','39'),('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'))
PRODUCT_COLOR = (('Black', 'Black'), ('White', 'White'), ('Blue', 'Blue'), ('Red', 'Red'), ('Green', 'Green'),
                 ('Grey', 'Grey'),
                 ('Orange', 'Orange'),
                 ('Cream', 'Cream'),
                 ('Brown', 'Brown'),)

# PRODUCT_KIND = (('MEN', 'MEN'), ('WOMEN', 'WOMEN',), ('KIDS', 'KIDS'))
PRODUCT_Category = (('FORMAL', 'FORMAL'), ('CASUALS',
                    'CASUALS'), ('SPORTS', 'SPORTS'))


class Brand(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='Brand')
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # Call the real save() method
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class MenProduct(models.Model):
    name = models.CharField(max_length=50)
    # kind = models.CharField(max_length=25, choices=PRODUCT_KIND)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    subtitle = models.TextField(max_length=300)
    brand = models.ForeignKey(Brand, related_name='MenProduct_Brand',
                              on_delete=models.SET_NULL, blank=True, null=True)
    category = models.CharField(max_length=25, choices=PRODUCT_Category)
    width = models.CharField(max_length=25, choices=PRODUCT_WIDTH)
    martial = models.CharField(max_length=25, choices=PRODUCT_MATERIAL)
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


class MenSize(models.Model):
    men_product = models.ForeignKey(
        MenProduct, on_delete=models.CASCADE, related_name='Product_MenSize')
    size = models.CharField(max_length=50, choices=PRODUCT_SIZE)

    def __str__(self):
        return str(self.men_product)


class MenColor(models.Model):
    men_product = models.ForeignKey(
        MenProduct, on_delete=models.CASCADE, related_name='Product_MenColor')
    color = models.CharField(max_length=50, choices=PRODUCT_COLOR)

    def __str__(self):
        return str(self.men_product)


class MenImages(models.Model):
    men_product = models.ForeignKey(
        MenProduct, on_delete=models.CASCADE, related_name='Product_MenImage')
    image = models.ImageField(upload_to='Men_Images')

    def __str__(self):
        return str(self.men_product)


class MenReview(models.Model):
    user = models.ForeignKey(User, related_name='user_MenReview',
                             on_delete=models.SET_NULL, null=True, blank=True)
    men_product = models.ForeignKey(
        MenProduct, on_delete=models.CASCADE,  related_name='Product_MenReview')
    rate = models.IntegerField()
    review = models.TextField(max_length=500)

    def __str__(self):
        return str(self.men_product)
