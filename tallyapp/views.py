from django.shortcuts import render,redirect
from .models import *
from tallyapp.models import Companies
from django.contrib import messages
from django.http import JsonResponse
def index(request):
    comp=Companies.objects.all()
    return render(request,'index.html',{'comp':comp})

def company(request):
    com=Companies.objects.all()
    return render(request,'company.html',{'com':com})

def index1(request):
    return render(request,'basepage.html')

def getStates(request):
    return States.objects.all()

def createcompany(request):
    com=States.objects.all()
    country=Countries.objects.all()
    return render(request,'createcompany.html',{'com':com,'country':country})

def companycreate(request):
    
    if request.method=='POST':
            name=request.POST['name']
            mailing_name=request.POST['mailing_name']
            address1=request.POST['address1']
            address2=request.POST['address2']
            address3=request.POST['address3']
            address4=request.POST['address4']
            state=request.POST['state']
            country=request.POST['country']
            #stateId= request.POST['statehidden']
            #print('fghj')
            
            state=States.objects.get(name=state) 
            #countryId=request.POST['countryhidden']
            #print(countryId)
            country=Countries.objects.get(name=country) 
            pincode=request.POST['pincode']
            telephone=request.POST['telephone']
            mobile=request.POST['mobile']
            fax=request.POST['fax']
            email=request.POST['email']
            website=request.POST['website']
            fin_begin=request.POST['fin_begin']
            books_begin=request.POST['books_begin']
            # maintain_accounts=request.POST['maintain_accounts']
            # currency_symbol=request.POST['currency_symbol']
            # formal_name=request.POST['formal_name']
            
            ctg=Companies(name=name,mailing_name=mailing_name,address1=address1,address2=address2,address3=address3,
                          address4=address4,
                          state=state,country=country,
                          pincode=pincode,
                          telephone=telephone,mobile=mobile,fax=fax,email=email,website=website,fin_begin=fin_begin,
                          books_begin=books_begin)
            ctg.save()
            
            
             
            messages.info(request,'Company added')
            
            demo1(request, ctg.id)
            
            # return redirect('companycreated')
            return render(request,'companycreated.html',{'ctg':ctg})
    return render(request,'createcompany.html')

def group(request):
    return render(request,'group.html')
def ledger(request):
    return render(request,'ledger.html')

def costcentre(request):
    return render(request,'costcentre.html')

def ratesofexchange(request):
    return render(request,'ratesofexchange.html')
def voucher(request):
    return render(request,'voucher.html')

def currency(request):
    return render(request,'currency.html')

def companycreated(request):
    # com=Companies.objects.get(id=pk)
    return render(request,'companycreated.html')

def create_group(request):
    if request.method == 'POST':
        gname = request.POST['gname']
        alia = request.POST['alia']
        

        under = request.POST['und']
        gp = request.POST['subled']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']

        mdl = Group(
            name=gname,
            alias=alia,
            under=under,
            sub_ledger=gp,
            debit_credit=nett,
            calculation=calc,
            used_purchase=meth,
        )
        mdl.save()
        return redirect('group')
        
    return render(request,'group.html')

def features(request):
    return render(request,'features.html')
def altercompanyview(request):
    com=Companies.objects.all()
    return render(request,'altercompanyview.html',{'com':com})

def altercompany(request,pk):
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        comp.name=request.POST['name']
        comp.mailing_name=request.POST['mailing_name']
        comp.address1=request.POST['address1']
        comp.address2=request.POST['address2']
        comp.address3=request.POST['address3']
        comp.address4=request.POST['address4']
            # state=request.POST['state']
            # country=request.POST['country']
        comp.pincode=request.POST['pincode']
        comp.telephone=request.POST['telephone']
        comp.mobile=request.POST['mobile']
        comp.fax=request.POST['fax']
        comp.email=request.POST['email']
        comp.website=request.POST['website']
        comp.fin_begin=request.POST['fin_begin']
        comp.books_begin=request.POST['books_begin']
            # currency_symbol=request.POST['currency_symbol']
            # formal_name=request.POST['formal_name']
        comp.save()
        return redirect('altercompanyview')
    return render(request,'editcompany.html',{'comp':comp})

def selectcompany(request):
    com=Companies.objects.all()
    return render(request,'selectcompany.html',{'com':com})

def addstate(request):
    if request.method=='POST':
        name=request.POST['name']
        data=States(name=name)
        data.save()
        return redirect('createcompany')
    return render(request,'createcompany.html')
def addcountry(request):
    if request.method=='POST':
        name=request.POST['name']
        data=Countries(name=name)
        data.save()
        return redirect('createcompany')
    return render(request,'createcompany.html')

def featurecompany(request,pk):
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        maintain_accounts=request.POST['maintain_accounts']
        ctg=features(maintain_accounts=maintain_accounts, company= comp)
        ctg.save()
    return render(request,'company.html')
def democreate(request):
    return render(request,'democreate.html')

def demo1(request, pk):
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        #maintain_accounts=request.POST['maintain_accounts']
        ctg=Features(company= comp)
        ctg.save()
    return render(request,'company.html')

def demo2(request, pk):
    feature=Features.objects.get(company_id=pk)
    c=Companies.objects.get(id=pk)
    if request.method == 'POST':
        if request.POST['maintain_accounts'] == 'Yes':
            feature.maintain_accounts= 'True'
        else:
            feature.maintain_accounts= 'False'
        feature.save()
    return render(request,'companycreated.html',{'ctg':c, 'ft':feature})


def shutcompany(request):
    com=Companies.objects.all()
    return render(request,'shutcompany.html',{'com':com})

def disable(request,pk):
    c=Companies.objects.get(id=pk)
    c.disabled=False
    c.save()
    return redirect('shutcompany')


def enable(request,pk):
    c=Companies.objects.get(id=pk)
    c.disabled=True
    c.save()
    return redirect('shutcompany')
