from django.shortcuts import render, redirect
from .forms import Product_uploadForm
# Create your views here.

def upload_product(request):
    if request.method == 'POST':
        upload = Product_uploadForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('/')
    else:
        upload = Product_uploadForm()
    return render(request, 'products/upload_product.html', {'upload':upload})