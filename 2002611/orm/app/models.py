from django.db import models

class Category(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)

class Product(models.Model):
    category = models.ForeignKey(Category , on_delete= models.PROTECT,null=True)
    code = models.CharField(max_length=30, unique=True) 
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True,null=True)
    price= models.IntegerField()