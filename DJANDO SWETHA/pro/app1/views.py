from django.shortcuts import render

from .models import *
from .form import *

# Create your views here.
def home(request):
    return render(request,'base.html')

def add_item(request):
    d=studform()
    if request.method=='POST':
        d=studform(request.POST)
        if d.is_valid():
            d.save()
            return list_items(request)
    return render(request,'add.html',{'form':d})
def list_items(request):
    p=student.objects.all()
    return render(request,'list.html',{'d':p})