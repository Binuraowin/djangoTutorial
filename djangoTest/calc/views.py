from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html",{"name":"Owin"})

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 + val2
    return render(request,"header.html",{"result":res})