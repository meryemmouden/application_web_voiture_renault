from django.db import models
from django.contrib.auth.models import  User

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=200,blank=True)
    position=models.CharField(max_length=250,null=True,blank=True)
    brand = models.CharField(max_length=250, null=True, blank=True)
    image=models.ImageField(null=True)
    small_description=models.CharField(max_length=250,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    selling_price = models.FloatField(null=True, blank=True)

    def ___str__(self):
        return self.name+'--'+self.brand

class accessoir(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    brand=models.CharField(max_length=200,blank=True)
    carburant= models.CharField(max_length=200,blank=True)
    version=models.CharField(max_length=200,blank=True)
    km=models.CharField(max_length=200,blank=True)
    image=models.ImageField(null=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    boitevitesse=models.CharField(max_length=200,blank=True)


    def ___str__(self):
        return self.name+'--'+self.brand

class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

class order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=150,null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    adress = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    pincode= models.CharField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=150, null=False)
    orderstatuses=(
        ('Pending','Pending'),
        ('Out For Shipping','Out For Shipping'),
        ('Completed','Completed'),

    )
    status=models.CharField(max_length=150,choices=orderstatuses,default='Pending')
    message=models.TextField(null=False)
    tracking_no= models.CharField(max_length=150, null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.id,self.tracking_no)

class orderItem(models.Model):
    Order = models.ForeignKey(order, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    price=models.FloatField(null=False)
    quantity=models.IntegerField(null=False)

    def __str__(self):
        return '{}-{}'.format(self.Order.id, self.Order.tracking_no)

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=False)
    adress=models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username