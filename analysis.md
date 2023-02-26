men_product:
        -name
        -price
        -subtitle
        -BRAND
        -cateogry (relations)
                -cateogry
                    -name
                    -image
        -size(relations)
                -size selections
                    -product
                    -size
        -WIDTH(select[m,w])
        -color(relations)
                -product
                -color selections
                    -product
                    -color
        -image(relations)
                -productimages
                    -product
                    -image
        -MATERIAL(select[Leather,coton,Suede])
        -STYLE
        -description
        -MANUFACTURER
        -REVIEW(relations)
                productreview
                        -user
                        -product
                        -rate
                        -review

women_product:
        -name
        -price
        -subtitle
        -BRAND
        -cateogry (relations)
                -cateogry
                    -name
                    -image
        -size(relations)
                -size selections
                    -product
                    -size
        -WIDTH(select[m,w])
        -color(relations)
                -size selections
                    -product
                    -color
        -image(relations)
                -productimages
                    -product
                    -image
        -MATERIAL(select[Leather,coton,Suede])
        -STYLE
        -description
        -MANUFACTURER
        -REVIEW(relations)
                productreview
                        -user
                        -product
                        -rate
                        -review

about:
        -title
        -description
        -image

contact-
        -form.forms
        -First Name
        -last name
        -subject
        -email
        -subject
        -message




        CART_STATUS = (
    ('Inprogress' , 'Inprogress') , 
    ('Completed' , 'Completed'),
)


# calculated fields

class Cart(models.Model):
    user = models.ForeignKey(User,related_name='cart_user',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(max_length=12,choices=CART_STATUS)
    
    def __str__(self):
        return str(self.user)
    
    
class CartDetail(models.Model):
    cart = models.ForeignKey(Cart,related_name='cart_Detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='cart_product',on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()
    
    def __str__(self):
        return str(self.cart)










ORDER_STATUS = (
    ('Recieved' , 'Recieved') , 
    ('Processed' , 'Processed'),
    ('Shipped','Shipped') , 
    ('Delivered','Delivered')
)


# calculated fields

 Order:
    user =
    code = 
    status 
    order_time = 
    delivery_time =

    
    
class OrderDetail(models.Model):
    order = 
    product = 
    quantity = models.IntegerField()
    price = models.FloatField()
    
    def __str__(self):
        return str(self.order)
    
    
class Coupon(models.Model):
    code = models.CharField(max_length=10)
    value = models.FloatField()
    from_date = models.DateField(default=timezone.now)
    to_date = models.DateField(default=timezone.now)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='coupon/')
    
    def __str__(self):
        return self.code

