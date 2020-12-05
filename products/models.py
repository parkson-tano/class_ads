from django.db import models

# Create your models here.

class Product_upload(models.Model):
    productname = models.CharField(max_length=200)
    category = models.CharField(max_length=20 )
    subcategory = models.CharField(max_length=20)
    price = models.IntegerField()
    location = models.CharField(max_length=20)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    contact = models.IntegerField()
    images = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.productname