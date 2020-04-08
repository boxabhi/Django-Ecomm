from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User

# Create your models here.

class Creator(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    price = models.FloatField(default=0)
    image = models.ImageField()
    slug = models.CharField(max_length=1000)
    creator = models.ForeignKey(Creator,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name    
    
class Cart(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

class Ordered(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    
        
       

    
    
    
    