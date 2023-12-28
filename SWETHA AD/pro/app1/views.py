from django.shortcuts import render
from .models import Product
from .models import *

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request,'list.html', {'p': products})