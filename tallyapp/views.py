from django.shortcuts import render,redirect
from .models import *
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
            country=Countries.objects.get(name=country) 
            pincode=request.POST['pincode']
            telephone=request.POST['telephone']
            mobile=request.POST['mobile']
            fax=request.POST['fax']
            email=request.POST['email']
            website=request.POST['website']
            fin_begin=request.POST['fin_begin']
            books_begin=request.POST['books_begin']
            # currency_symbol=request.POST['currency_symbol']
            # formal_name=request.POST['formal_name']
            cmp=Companies.objects.filter(name=name)
            if cmp:
                messages.info(request,'Company name already exists!!')
                return redirect('createcompany')
            else:
                ctg=Companies(name=name,mailing_name=mailing_name,address1=address1,address2=address2,address3=address3,
                    address4=address4,
                    state=state,country=country,
                    pincode=pincode,
                    telephone=telephone,mobile=mobile,fax=fax,email=email,website=website,fin_begin=fin_begin,
                    books_begin=books_begin)
                ctg.save()
            
            
             
            
            
            demo1(request, ctg.id)
            
            # return redirect('companycreated')
            return render(request,'features.html',{'ctg':ctg})
    return render(request,'createcompany.html')

def group(request,pk):
    # feature=Features.objects.get(company_id=pk)
    cmp=Companies.objects.get(id=pk)
    return render(request,'group.html',{'cmp':cmp})
def ledger(request,pk):
    cmp=Companies.objects.get(id=pk)
    return render(request,'ledger.html',{'cmp':cmp})

def costcentre(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        cname = request.POST['cname']
        alia = request.POST['alia']
        under = request.POST['under']
        costc=Costcentre.objects.filter(cname=cname)
        if costc:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            
            data = Costcentre(cname=cname,alias=alia,under=under,company=cmp)
            data.save()
        # return redirect('costcentre')
    ccentre=Costcentre.objects.filter(company_id=cmp)
    return render(request,'costcentre.html',{'cmp':cmp,'ccentre':ccentre})


def ratesofexchange(request):
    return render(request,'ratesofexchange.html')
def voucher(request):
    return render(request,'voucher.html')

def currency(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        symbol = request.POST['symbol']
        formal_name = request.POST['formal_name']
        currency_code = request.POST['currency_code']
        decimal_places = request.POST['decimal_places']
        show_in_millions = request.POST['show_in_millions']
        suffix_symbol = request.POST['suffix_symbol']
        symbol_and_amount = request.POST['symbol_and_amount']
        after_decimal = request.POST['after_decimal']
        amount_in_words = request.POST['amount_in_words']
        data = Currency(symbol=symbol,formal_name=formal_name,currency_code=currency_code,
                        decimal_places=decimal_places,show_in_millions=show_in_millions,
                        suffix_symbol=suffix_symbol,symbol_and_amount=symbol_and_amount,
                        after_decimal=after_decimal,amount_in_words=amount_in_words,company=cmp)
        data.save()
        # return redirect('costcentre')
    return render(request,'currency.html',{'cmp':cmp})



def creategroup(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        gname = request.POST['gname']
        alia = request.POST['alia']
        under = request.POST['under']
        sub_ledger = request.POST['sub_ledger']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']
        
        mdl = Group(
            name=gname,
            alias=alia,
            under=under,
            sub_ledger=sub_ledger,
            debit_credit=nett,
            calculation=calc,
            used_purchase=meth,
            company=cmp
        )
        mdl.save()
        # return redirect('index')
    return render(request,'group.html',{'cmp':cmp})
    


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
        st=States.objects.filter(name=name)
        if st:
            # messages.info(request,'Company name already exists!!')
            return redirect('createcompany')
        else:
            data=States(name=name)
            data.save()
            return redirect('createcompany')
    return render(request,'createcompany.html')
def addcountry(request):
    if request.method=='POST':
        name=request.POST['name']
        con=Countries.objects.filter(name=name)
        if con:
            # messages.info(request,'Company name already exists!!')
            return redirect('createcompany')
        else:
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

def features(request, pk):
    feature=Features.objects.get(company_id=pk)
    c=Companies.objects.get(id=pk)
    if request.method == 'POST':
        if request.POST['maintain_accounts'] == 'Yes':
            feature.maintain_accounts= 'True'
        else:
            feature.maintain_accounts= 'False'
        if request.POST['bill_wise_entry'] == 'Yes':
            feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        feature.save()
    return render(request,'features.html',{'ctg':c, 'ft':feature})


def shutcompany(request):
    com=Companies.objects.all()
    return render(request,'shutcompany.html',{'com':com})

def disable(request,pk):
    c=Companies.objects.get(id=pk)
    c.active=False
    c.save()
    return redirect('shutcompany')


def enable(request,pk):
    c=Companies.objects.get(id=pk)
    c.active=True
    c.save()
    return redirect('shutcompany')
