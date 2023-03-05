import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
################################
import django
django.setup()
###########################

from Products.models import *
import random
from faker import Faker


# def seed_brand(n):
#     fake = Faker()
#     images = ['brand-1.jpg', 'brand-2.jpg',
#               'brand-3.jpg', 'brand-4.jpg', 'brand-5.jpg']
#     for x in range(n):
#         Brand.objects.create(
#             name=fake.name(),
#             image=f"Brand/{images[random.randint(0,4)]}"
#         )
#     print(f'{n} Brand Seeded')


# seed_brand(25)


# def seed_Category(n):
#     fake = Faker()
#     images = ['img_bg_3.jpg', 'item-10.jpg',
#               'item-11.jpg', 'item-12.jpg', 'men.jpg', 'women.jpg']
#     for x in range(n):
#         Category.objects.create(
#             name=fake.name(),
#             image=f"Category/{images[random.randint(0,4)]}"
#         )
#     print(f'{n} Category Seeded')


# seed_Category(25)


# def seedmenProducts(n):
#     fake = Faker()
#     WIDTH = ['wide', 'medium', 'narrow']
#     MATERIAL = ['Leather', 'Rubber', 'Textiles', 'Synthetics', 'Foam']
#     images = ['item-1.jpg', 'item-2.jpg', 'item-3.jpg', 'item-4.jpg', 'item-5.jpg', 'item-6.jpg', 'item-7.jpg', 'item-8.jpg',
#               'item-9.jpg', 'item-10.jpg', 'item-11.jpg', 'item-11.jpg', 'item-12.jpg', 'item-13.jpg', 'item-14.jpg', 'item-15.jpg', 'item-16.jpg']
#     for x in range(n):
#         MenProduct.objects.create(
#             name=fake.name(),
#             price=round(random.uniform(49.99, 499.99), 2),
#             subtitle=fake.text(max_nb_chars=300),
#             image=f"Product_Images/{images[random.randint(0,15)]}",
#             width=WIDTH[random.randint(0, 2)],
#             martial=MATERIAL[random.randint(0, 4)],
#             style=fake.text(max_nb_chars=25),
#             description=fake.text(max_nb_chars=1000),
#             manufacturer=fake.text(max_nb_chars=1000),
#             brand = Brand.objects.get(id=random.randint(1,24)),
#             category = Category.objects.get(id=random.randint(1,24)),
#         )
#     print(f'{n} MenProduct Seeded')


# seedmenProducts(249)


# def seed_ProductSize(n):
#     fake = Faker()
#     SIZE = ['36', '37', '38', '39', '40', '41', '42', '43', '44',]
#     for x in range(n):
#         ProductSize.objects.create(
#             product=Product.objects.get(id=random.randint(753, 1250)),
#             size=SIZE[random.randint(0, 8)]
#         )
#     print(f'{n} ProductSize Seeded')


# seed_ProductSize(1500)


# def seed_ProductColor(n):
#     fake = Faker()
#     COLOR = ['Black', 'White', 'Blue', 'Red',
#              'Green', 'Grey', 'Orange', 'Cream', 'Brown']
#     for x in range(n):
#         ProductColor.objects.create(
#             product=Product.objects.get(id=random.randint(753, 1250)),
#             color=COLOR[random.randint(0, 8)]
#         )
#     print(f'{n} ProductColor Seeded')


# seed_ProductColor(2000)


# def seed_ProductImages(n):
#     fake = Faker()
#     images = ['item-1.jpg', 'item-2.jpg', 'item-3.jpg', 'item-4.jpg', 'item-5.jpg', 'item-6.jpg', 'item-7.jpg', 'item-8.jpg',
#               'item-9.jpg', 'item-10.jpg', 'item-11.jpg', 'item-11.jpg', 'item-12.jpg', 'item-13.jpg', 'item-14.jpg', 'item-15.jpg', 'item-16.jpg']
#     for x in range(n):
#         ProductImages.objects.create(
#             product=Product.objects.get(id=random.randint(753, 1250)),
#             image=f"products_image/{images[random.randint(0,15)]}",
#         )
#     print(f'{n} ProductImages Seeded')


# seed_ProductImages(2000)


# def seed_ProductReview(n):
#     fake = Faker()
#     for x in range(n):
#         ProductReview.objects.create(
#             product=Product.objects.get(id=random.randint(753, 1250)),
#             rate=random.randint(0, 4),
#             review=fake.text(max_nb_chars=500),
#         )
#     print(f'{n} ProductReview Seeded')


# seed_ProductReview(1500)


# def seed_womenProducts(n):
#     fake = Faker()
#     # images = ['item-1.jpg','item-2.jpg','item-3.jpg','item-4.jpg','item-5.jpg','item-6.jpg','item-7.jpg','item-8.jpg','item-9.jpg','item-10.jpg','item-11.jpg','item-11.jpg','item-12.jpg','item-13.jpg','item-14.jpg','item-15.jpg','item-16.jpg']
#     WIDTH = (('wide', 'wide'), ('medium', 'medium'), ('narrow', 'narrow'))
#     MATERIAL = (('Leather', 'Leather'), ('Rubber', 'Rubber'), ('Textiles',
#                 'Textiles'), ('Synthetics', 'Synthetics'), ('Foam', 'Foam'))
#     for x in range(n):
#         WomenProduct.objects.create(
#             name=fake.name(),
#             price=round(random.uniform(49.99, 499.99), 2),
#             subtitle=fake.text(max_nb_chars=300),
#             brand=fake.text(max_nb_chars=25),
#             width=WIDTH[random.randint(0, 2)],
#             martial=MATERIAL[random.randint(0, 4)],
#             style=fake.text(max_nb_chars=25),
#             description=fake.text(max_nb_chars=1000),
#             manufacturer=fake.text(max_nb_chars=1000),
#             # category=Category.objects.get(id=random.randint(1, 100)),
#         )
#     print(f'{n} WomenProduct Seeded')


# # seed_womenProducts(100)


# def seed_women_Size(n):
#     fake = Faker()
#     SIZE = (('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'),
#                     ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'))
#     for x in range(n):
#         WomenSize.objects.create(
#             women_product=WomenProduct.objects.get(id=random.randint(1, 100)),
#             size=SIZE[random.randint(0, 8)]
#         )
#     print(f'{n} women_Size Seeded')


# seed_women_Size(800)


# def seed_women_Color(n):
#     fake = Faker()
#     COLOR = (('Black', 'Black'), ('White', 'White'), ('Blue', 'Blue'), ('Red', 'Red'), ('Green', 'Green'),
#                      ('Grey', 'Grey'), ('Orange', 'Orange'), ('Cream', 'Cream'), ('Brown', 'Brown'),)
#     for x in range(n):
#         WomenColor.objects.create(
#             women_product=WomenProduct.objects.get(id=random.randint(1, 100)),
#             color=COLOR[random.randint(0, 8)]
#         )
#     print(f'{n} women_Color Seeded')


# seed_women_Color(800)


# def seed_women_Images(n):
#     fake = Faker()
#     images = ['item-1.jpg', 'item-2.jpg', 'item-3.jpg', 'item-4.jpg', 'item-5.jpg', 'item-6.jpg', 'item-7.jpg', 'item-8.jpg',
#               'item-9.jpg', 'item-10.jpg', 'item-11.jpg', 'item-11.jpg', 'item-12.jpg', 'item-13.jpg', 'item-14.jpg', 'item-15.jpg', 'item-16.jpg']
#     for x in range(n):
#         WomenImages.objects.create(
#             women_product=WomenProduct.objects.get(id=random.randint(1, 100)),
#             image=f"women_Images/{images[random.randint(0,15)]}",
#         )
#     print(f'{n} women_Images Seeded')


# # seed_women_Images(1000)


# def seed_women_Review(n):
#     fake = Faker()
#     for x in range(n):
#         WomenReview.objects.create(
#             women_product=WomenProduct.objects.get(id=random.randint(1, 100)),
#             rate=random.randint(0, 4),
#             review=fake.text(max_nb_chars=500)
#         )
#     print(f'{n} women_Review Seeded')


# # seed_women_Review(300)
