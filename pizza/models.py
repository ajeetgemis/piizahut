from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import uuid

choice2=('Veg','Veg'),('Non-Veg','Non-Veg')
choices=(('S','small'),('M','medium'),('L','large'),('XL','Xtra large'),('XXL','Double X large'))
class Baseclass(models.Model):
    uid=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract=True

class Pizzacategory(Baseclass):
    cat=models.CharField(choices=choice2,default=True,max_length=20)

class Pizza(Baseclass):
    category=models.ForeignKey(Pizzacategory,on_delete=models.CASCADE,related_name='pizzas')
    pizza_name=models.CharField(max_length=100)
    pizza_price=models.IntegerField()
    pizza_image=models.ImageField(upload_to='uploads\products')

class Cart(Baseclass):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='carts')
    is_paid=models.BooleanField(default=False)
    payment_id=models.CharField(max_length=100,default=True)
    payment_request_id=models.CharField(max_length=100,default=True)
    

    def g_total(self):
        return Cart_items.objects.filter(cart=self).aggregate(sum('pizza__pizza_price'))['pizza_pizza_price__sum']
class Cart_items(Baseclass):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cart_item")
    pizza=models.ForeignKey(Pizza,on_delete=models.CASCADE) 

class faker_test(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name       

class enqury(models.Model):
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50)
    message=models.TextField(max_length=300)

    def __str__(self):
        return self.email        