from django.shortcuts import render
from .models import *
from .forms import studform

# Create your views here.
def home(request):
    return render(request,'base.html')

def add(request):
    d=studform()
    if request.method=="POST":
        d=studform(request.POST)
        if d.is_valid():
            d.save()
            return list(request)
    return render(request,'add.html',{'q':d})




def user_form2(request):
    if request.method=='POST':
        d=studform(request.POST)
        if d.is_valid():
            d.save()
            return list(request)
    return render(request,'form2.html')
    

def list(request):
    p=student.objects.all()
    return render(request,'list.html',{'d':p})


def edit_item(request,p):
    b=student.objects.get(pk=p)
    d=studform(instance=b)
    if request.method=='POST':
        d=studform(request.POST,instance=b)
        if d.is_valid():
            d.save()
            return list(request)
    return render(request,'edit.html',{'q':d})


def delete_item(request,p):
    b=student.objects.get(pk=p)
    b.delete()
    return list(request)

def form3(request):
    if request.method=='POST':
        username=request.POST.get('n')
        email=request.POST.get('r')
        password=request.POST.get('p')
        confirm=request.POST.get('s')
        data=student.objects.create(username=username,email=email,password=password,confirm=confirm)
        data.save()
        return list(request)
    return render(request,'form3.html')

