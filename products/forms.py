from .models import Product_upload
from django.forms import ModelForm

class Product_uploadForm(ModelForm):
    class Meta:
        model = Product_upload
        fields = '__all__'
    