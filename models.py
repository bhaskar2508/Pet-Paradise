from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.conf import settings



class LoginForm(forms.Form):
    username=forms.CharField(max_length=60)
    password=forms.CharField(max_length=60,widget=forms.PasswordInput())


class Catgory(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=600)

    class Meta:
        db_table="Category"

    def __str__(self):
        return self.name

class CatFood(models.Model):
    product_name=models.CharField(max_length=60)
    product_price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(max_length=600)
    image=models.ImageField(upload_to='image',default='')
    category=models.ForeignKey(Catgory,on_delete=models.CASCADE)

    class Meta:
        db_table='CatFood'

class CatFoodCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    catfood=models.ForeignKey(CatFood,on_delete=models.CASCADE)

class CatHealth(models.Model):
    product_name=models.CharField(max_length=60)
    product_price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(max_length=600)
    image=models.ImageField(upload_to='image',default='')
    category=models.ForeignKey(Catgory,on_delete=models.CASCADE)

    class Meta:
        db_table='CatHealth'

class CatHealthCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cathealth=models.ForeignKey(CatHealth,on_delete=models.CASCADE)

class CatToys(models.Model):
    product_name=models.CharField(max_length=60)
    product_price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(max_length=600)
    image=models.ImageField(upload_to='image',default='')
    category=models.ForeignKey(Catgory,on_delete=models.CASCADE)

    class Meta:
        db_table='CatToys'

class CatToysCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cattoys=models.ForeignKey(CatToys,on_delete=models.CASCADE)

class DogFood(models.Model):
    product_name=models.CharField(max_length=60)
    product_price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(max_length=600)
    image=models.ImageField(upload_to='image',default='')
    category=models.ForeignKey(Catgory,on_delete=models.CASCADE)

    class Meta:
        db_table='DogFood'

class DogFoodCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    dogfood=models.ForeignKey(DogFood,on_delete=models.CASCADE)

class DogToys(models.Model):
    product_name=models.CharField(max_length=60)
    product_price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(max_length=600)
    image=models.ImageField(upload_to='image',default='')
    category=models.ForeignKey(Catgory,on_delete=models.CASCADE)

    class Meta:
        db_table='DogToys'

class DogToysCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    dogtoys=models.ForeignKey(DogToys,on_delete=models.CASCADE)

class DogHealth(models.Model):
    product_name=models.CharField(max_length=60)
    product_price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(max_length=600)
    image=models.ImageField(upload_to='image',default='')
    category=models.ForeignKey(Catgory,on_delete=models.CASCADE)

    class Meta:
        db_table='DogHealth'

class DogHealthCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    doghealth=models.ForeignKey(DogHealth,on_delete=models.CASCADE)

# models.py

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    razorpay_payment_id = models.CharField(max_length=100)
    razorpay_order_id = models.CharField(max_length=100)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending')

    class Meta:
        db_table = 'Payment'

    def __str__(self):
        return f"Payment for Order {self.order.id} - Status: {self.status}"
