from django.contrib import admin
from .models import *
# Register your models here.

# class ProductAdmin(admin.ModelAdmin):
#     list_filter = ('productname', 'category')
#     list_per_page = 100
#     list_display = ('productname', 'category', 'date_uploaded')

admin.site.register([Product_upload, ProductImage ])