from django.urls import path,include
from . import  views

urlpatterns = [
    path('upload_product', views.upload_product, name = 'upload_product')
]