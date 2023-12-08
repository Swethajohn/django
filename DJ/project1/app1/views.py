from django.shortcuts import render

# Create your views here.
def home(request):
    d={'name':'swetha','age':22}
    l=[1,2,3,4,5,6]
    return render(request,'base.html',{'data':d,'lk':l})
def index(request):
    return render(request,'index.html')