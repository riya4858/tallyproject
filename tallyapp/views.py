from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.html')

def company(request):
    return render(request,'company.html')

def index1(request):
    return render(request,'basepage.html')

def createcompany(request):
    return render(request,'createcompany.html')