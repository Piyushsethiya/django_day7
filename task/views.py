from django.shortcuts import render


def index(request):
    return render (request,'index.html')

# Create your views here.

def viewcategory(request):
    return render (request,'viewcategory.html')