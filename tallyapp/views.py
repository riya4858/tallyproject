from django.shortcuts import render,redirect
from .models import *
from tallyapp.models import Companies
from django.contrib import messages
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
            address2=request.POST['address2']
            address3=request.POST['address3']
            address4=request.POST['address4']
            # state=request.POST['state']
            # country=request.POST['country']
            pincode=request.POST['pincode']
            telephone=request.POST['telephone']
            mobile=request.POST['mobile']
            fax=request.POST['fax']
            email=request.POST['email']
            website=request.POST['website']
            fin_begin=request.POST['fin_begin']
            books_begin=request.POST['books_begin']
            currency_symbol=request.POST['currency_symbol']
            formal_name=request.POST['formal_name']
            
            ctg=Companies(name=name,address1=address1,address2=address2,address3=address3,address4=address4,pincode=pincode,
                          telephone=telephone,mobile=mobile,fax=fax,email=email,website=website,fin_begin=fin_begin,
                          books_begin=books_begin,currency_symbol=currency_symbol,formal_name=formal_name)
            ctg.save()
            messages.info(request,'Company added')
            # return redirect('companycreated')
            return render(request,'companycreated.html',{'ctg':ctg})
    return render(request,'createcompany.html')
def group(request):
    return render(request,'group.html')
def ledger(request):
    return render(request,'ledger.html')

def costcentre(request):
    return render(request,'costcentre.html')

def currency(request):
    return render(request,'currency.html')

def companycreated(request):
    # com=Companies.objects.get(id=pk)
    return render(request,'companycreated.html')