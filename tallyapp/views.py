from django.shortcuts import render,redirect
from .models import *
from tallyapp.models import Companies

def index(request):
    return render(request,'index.html')

def company(request):
    com=Companies.objects.all()
    return render(request,'company.html',{'com':com})

def index1(request):
    return render(request,'basepage.html')

def createcompany(request):
    return render(request,'createcompany.html')

def companycreate(request):
    if request.method=='POST':
            name=request.POST['name']
            address1=request.POST['address1']
            
            ctg=Companies(name=name,address1=address1)
            ctg.save()
            return redirect('createcompany')
    return render(request,'createcompany.html')
def group(request):
    return render(request,'group.html')
def ledger(request):
    return render(request,'ledger.html')

def costcentre(request):
    return render(request,'costcentre.html')

def currency(request):
    return render(request,'currency.html')