from django.db import models

# Create your models here.


class Creator(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Product(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    price = models.FloatField(default=0)
    image = models.ImageField()
    creator = models.ForeignKey(Creator,on_delete=models.CASCADE)
    
    
    
    
    
    
    