from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# from django.utils.translation import gettext as _
from django.utils.text import slugify
from Men_Products.models import Brand
# Create your models here.
PRODUCT_WIDTH = (('wide', 'wide'), ('medium', 'medium'), ('narrow', 'narrow'))
PRODUCT_MATERIAL = (('Leather', 'Leather'), ('Rubber', 'Rubber'), ('Textiles',
                                                                   'Textiles'), ('Synthetics', 'Synthetics'), ('Foam', 'Foam'))
PRODUCT_SIZE = (('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'),
                ('40', '40'))
PRODUCT_COLOR = (('Black', 'Black'), ('White', 'White'), ('Blue', 'Blue'), ('Red', 'Red'), ('Green', 'Green'),
                 ('Grey', 'Grey'),
                 ('Orange', 'Orange'),
                 ('Cream', 'Cream'),
                 ('Brown', 'Brown'),)

PRODUCT_KIND = (('MEN', 'MEN'), ('WOMEN', 'WOMEN',), ('KIDS', 'KIDS'))
PRODUCT_Category = (('FORMAL', 'FORMAL'), ('CASUALS',
                    'CASUALS'), ('SPORTS', 'SPORTS'))


# class Brand(models.Model):
#     name = models.CharField(max_length=25)
#     image = models.ImageField(upload_to='brand_images')
#     slug = models.SlugField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         # Call the real save() method
#         super(Brand, self).save(*args, **kwargs)

#     def __str__(self):
#         return str(self.name)


class WomenProduct(models.Model):
    name = models.CharField(max_length=50)
    # kind = models.CharField(max_length=25, choices=PRODUCT_KIND)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    subtitle = models.TextField(max_length=300)
    brand = models.ForeignKey(Brand, related_name='WomenProduct_Brand',
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
        super(WomenProduct, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class WomenSize(models.Model):
    Women_product = models.ForeignKey(
        WomenProduct, on_delete=models.CASCADE, related_name='Product_WomenSize')
    size = models.CharField(max_length=50, choices=PRODUCT_SIZE)

    def __str__(self):
        return str(self.Women_product)


class WomenColor(models.Model):
    Women_product = models.ForeignKey(
        WomenProduct, on_delete=models.CASCADE, related_name='Product_WomenColor')
    color = models.CharField(max_length=50, choices=PRODUCT_COLOR)

    def __str__(self):
        return str(self.Women_product)


class WomenImages(models.Model):
    Women_product = models.ForeignKey(
        WomenProduct, on_delete=models.CASCADE, related_name='Product_WomenImage')
    image = models.ImageField(upload_to='Women_Images')

    def __str__(self):
        return str(self.Women_product)


class Women_Review(models.Model):
    user = models.ForeignKey(User, related_name='user_WomenReview',
                             on_delete=models.SET_NULL, null=True, blank=True)
    Women_product = models.ForeignKey(
        WomenProduct, on_delete=models.CASCADE,  related_name='Product_WomenReview')
    rate = models.IntegerField()
    review = models.TextField(max_length=500)

    def __str__(self):
        return str(self.Women_product)
