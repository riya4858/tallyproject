from datetime import datetime, timedelta
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse
def index(request):
    comp=Companies.objects.all()
    return render(request,'index.html',{'comp':comp})
def basepage(request):
    comp=Companies.objects.all()
    return render(request,'base.html',{'comp':comp})

def company(request):
    com=Companies.objects.all()
    return render(request,'company.html',{'com':com})


# def getStates(request):
#     cmp=States.objects.filter(country_id=pk)
#     return cmp
def getStates(request):
    st=States.objects.all()
    country=Countries.objects.all()
   
    post_id=request.GET.get['post_id']
    
    cmp=States.objects.filter(country_id=post_id)
    # return render(request,'createcompany.html',{'st':st,'country':country,'cmp':cmp})
    return JsonResponse(cmp)

def createcompany(request):
    st=States.objects.all()
    country=Countries.objects.all()
    return render(request,'createcompany.html',{'st':st,'country':country})

def companycreate(request):
    
    if request.method=='POST':
        name=request.POST['name']
        mailing_name=request.POST['mailing_name']
        address1=request.POST['address1']
        address2=request.POST['address2']
        address3=request.POST['address3']
        address4=request.POST['address4']
        s=request.POST['state']
        
        print(s)
        country=request.POST['country']   
        print(country) 
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
        end=datetime.strptime(fin_begin,'%Y-%m-%d')+timedelta(days=364)
        a=end.date()
        cmp=Companies.objects.filter(name=name)
        if cmp:
            
            messages.info(request,'Company name already exists!!')
            return redirect('createcompany')
        else:
            ctg=Companies(name=name,mailing_name=mailing_name,address1=address1,address2=address2,address3=address3,
                address4=address4,states=s,country=country,
                pincode=pincode,
                telephone=telephone,mobile=mobile,fax=fax,email=email,website=website,fin_begin=fin_begin,
                books_begin=books_begin,c_symbol=currency_symbol,f_name=formal_name,end=a)
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
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        #ledger
        name = request.POST['name']
        alias = request.POST['alias']
        under = request.POST['under']
        provide_banking_details = request.POST['provide_banking_details']
        pan_no = request.POST['pan_no']
        
        #mailing_details
        mailingname = request.POST['mailingname']
        address = request.POST['address']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['pincode']
        
        #banking_details
        od_limit= request.POST['od_limit']
        holder_name = request.POST['holder_name']
        acc_no = request.POST['acc_no']
        ifsc = request.POST['ifsc']
        swift_code = request.POST['swift_code']
        bank_name = request.POST['bank_name']
        branch = request.POST['branch']
        set_cheque = request.POST['set_cheque']
        ch_printing = request.POST['ch_printing']
        ch_config = request.POST['ch_config']
        
        
        #Asset_rounding
        rounding_method=request.POST['rounding_method']
        round_limit=request.POST['round_limit']
        
        #Asset_statutory
        assessable_calculation=request.POST['assessable_calculation']
        appropriate_to=request.POST['appropriate_to']
        gst_applicable=request.POST['gst_applicable']
        set_alter_GST=request.POST['set_alter_GST']
        type_of_supply=request.POST['type_of_supply']
        method_of_calc=request.POST['method_of_calc']
        
         #Sundry
        maintain_balance_bill_by_bill=request.POST['maintain_balance_bill_by_bill']
        default_credit_period=request.POST['default_credit_period']
        check_for_credit_days=request.POST['check_for_credit_days']
        
        
        led=Ledger.objects.filter(name=name)
        if led:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            data = Ledger(name=name,alias=alias,under=under,provide_banking_details=provide_banking_details,
                            pan_no=pan_no,company=cmp)
            data.save()
            
            #mailing_details
            data1=Ledger_Mailing_Details(mailingname=mailingname,address=address,state=state,country=country,pincode=pincode,
                                        company=cmp,ledger=data)
            data1.save()
            return redirect('index')
            #banking_details
            data2=Ledger_Banking_Details(od_limit=od_limit,holder_name=holder_name,acc_no=acc_no,ifsc=ifsc,swift_code=swift_code,bank_name=bank_name,
                                        branch=branch,set_cheque=set_cheque,ch_printing=ch_printing,ch_config=ch_config,
                                        company=cmp,ledger=data)
            data2.save()
            return redirect('index')
            #Asset_rounding
            data3=Ledger_Asset_Rounding(rounding_method=rounding_method,round_limit=round_limit,
                                        company=cmp,ledger=data)
            data3.save()
            return redirect('index')
            #Asset_statutory
            data4=Ledger_Asset_Statutory(assessable_calculation=assessable_calculation,appropriate_to=appropriate_to,
                                         gst_applicable=gst_applicable,set_alter_GST=set_alter_GST,type_of_supply=type_of_supply,
                                         method_of_calc=method_of_calc,company=cmp,ledger=data)
            data4.save()
            return redirect('index')
            #Sundry
            data5=Ledger_Sundry(maintain_balance_bill_by_bill=maintain_balance_bill_by_bill,default_credit_period=default_credit_period,
                                        check_for_credit_days=check_for_credit_days,company=cmp,ledger=data)
            data5.save()
            return redirect('index')
            
    grup=Group.objects.filter(company_id=cmp)
    return render(request,'ledger.html',{'cmp':cmp,'grup':grup})

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
            return redirect('index')
    ccentre=Costcentre.objects.filter(company_id=cmp)
    return render(request,'costcentre.html',{'cmp':cmp,'ccentre':ccentre})

def costcentre2(request,pk):
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
            return redirect('index')
    ccentre=Costcentre.objects.filter(company_id=cmp)
    return render(request,'costcentre2.html',{'cmp':cmp,'ccentre':ccentre})


def ratesofexchange(request,pk):
    cmp=Companies.objects.get(id=pk)
    cur=Currency.objects.filter(company_id=cmp)
    return render(request,'ratesofexchange.html',{'cmp':cmp,'curr':cur})

def voucher(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        Vname = request.POST['nam']
        alias = request.POST['alias']
        vtype = request.POST['vtype']
        abbre = request.POST['abbre']
        activ_vou_typ = request.POST['avtyp']  # bool
        meth_vou_num = request.POST['meth_vou_num']
        useadv = request.POST.get('useadvc', False)
        prvtdp = request.POST.get('prvtdp', False)
        use_effct_date = request.POST['uefftdate']  # bool
        allow_zero_trans = request.POST['allow_zero_trans']  # bool
        allow_naration_in_vou = request.POST['allow_naration_in_vou']  # bool
        optional = request.POST['optional'] 
        provide_narr = request.POST['providenr']  # bool
        print = request.POST['print']  # bool

        if Voucher.objects.filter(voucher_name=Vname).exists():
               pass
        
        mdl = Voucher(

            voucher_name=Vname,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            use_effective_date=use_effct_date,
            use_adv_conf = useadv,
            prvnt_duplictes =prvtdp,
            allow_zero_value_trns=allow_zero_trans,
            allow_naration_in_voucher=allow_naration_in_vou,
            make_optional=optional,
            provide_naration=provide_narr,
            print_voucher=print,
            company=cmp

        )
        mdl.save()
        return redirect('index')
    vv=Voucher.objects.filter(company_id=cmp)
    return render(request,'voucher.html',{'cmp':cmp,'vv':vv})

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
        return redirect('index')
    return render(request,'currency.html',{'cmp':cmp})



def creategroup(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        gname = request.POST['gname']
        alia = request.POST['alia']
        under = request.POST['under']
        sub_ledger = request.POST['sub_ledger']
        gross = request.POST['gross']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']
        nature = request.POST['nature']
        grp=Group.objects.filter(name=gname)
        if grp:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            mdl = Group(
                name=gname,
                alias=alia,
                under=under,
                sub_ledger=sub_ledger,
                debit_credit=nett,
                calculation=calc,
                used_purchase=meth,
                nature_of_group=nature,
                gross_profit=gross,
                company=cmp
            )
            mdl.save()
            return redirect('index')
    grup=Group.objects.filter(company_id=cmp)
    return render(request,'group.html',{'cmp':cmp,'grup':grup})
    
def group2(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        gname = request.POST['gname']
        alia = request.POST['alia']
        under = request.POST['under']
        sub_ledger = request.POST['sub_ledger']
        gross = request.POST['gross']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']
        nature = request.POST['nature']
        grp=Group.objects.filter(name=gname)
        if grp:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            mdl = Group(
                name=gname,
                alias=alia,
                under=under,
                sub_ledger=sub_ledger,
                debit_credit=nett,
                calculation=calc,
                used_purchase=meth,
                nature_of_group=nature,
                gross_profit=gross,
                company=cmp
            )
            mdl.save()
            return redirect('index')
    grup=Group.objects.filter(company_id=cmp)
    return render(request,'group2.html',{'cmp':cmp,'grup':grup})

def altercompanyview(request):
    com=Companies.objects.all()
    return render(request,'altercompanyview.html',{'com':com})

def altercompany(request,pk):
    com=States.objects.all()
    cntry=Countries.objects.all()
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        comp.name=request.POST['name']
        comp.mailing_name=request.POST['mailing_name']
        comp.address1=request.POST['address1']
        comp.address2=request.POST['address2']
        comp.address3=request.POST['address3']
        comp.address4=request.POST['address4']
        comp.states=request.POST['state']
        comp.country=request.POST['country']
        
        comp.pincode=request.POST['pincode']
        comp.telephone=request.POST['telephone']
        comp.mobile=request.POST['mobile']
        comp.fax=request.POST['fax']
        comp.email=request.POST['email']
        comp.website=request.POST['website']
        comp.fin_begin=request.POST['fin_begin']
        comp.books_begin=request.POST['books_begin']
        comp.currency_symbol=request.POST['currency_symbol']
        comp.formal_name=request.POST['formal_name']
        comp.save()
        return redirect('altercompanyview')
    return render(request,'editcompany.html',{'comp':comp,'com':com,'country':cntry})

def selectcompany(request):
    com=Companies.objects.all()
    return render(request,'selectcompany.html',{'com':com})

def addstate(request):
    if request.method=='POST':
        name=request.POST['name']
        cntryid=request.POST['cname']
        st=States.objects.filter(name=name)
        countr=Countries.objects.filter(name=cntryid)
        if st:
            # messages.info(request,'Company name already exists!!')
            return redirect('createcompany')
        else:
            data=States(name=name, country=countr)
            data.save()
            return redirect('createcompany')
    return render(request,'createcompany.html')

def addstatenew(name):
    return "";

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
        if request.POST['cost_centres'] == 'Yes':
            feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['interest_calc'] == 'Yes':
            feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['maintain_inventory'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['integrate_accounts'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['multiple_price_level'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['batches'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['expirydate_batches'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['joborder_processing'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        
        if request.POST['cost_tracking'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['job_costing'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['discount_invoices'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['Billed_Quantity'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['gst'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['tds'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['tcs'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['vat'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['excise'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['servicetax'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['payroll'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['multiple_addrss'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['vouchers'] == 'Yes':
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
def gst(request,pk):
    cm=Companies.objects.get(id=pk)
    return render(request,'gstpage.html',{'cm':cm})

def gstcreate(request,pk):
    cm=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cm=Companies.objects.get(id=pk)
        state = request.POST['state']
        reg_type = request.POST['reg_type']
        assessee = request.POST['assessee']
        app_form = request.POST['app_form']
        gstin = request.POST['gstin']
        gstr1 = request.POST['gstr1']
        flood = request.POST['flood']
        rate_details = request.POST['rate_details']
        advance_receipts = request.POST['advance_receipts']
        reverse_charge = request.POST['reverse_charge']
        classifications = request.POST['classifications']
        bend_details = request.POST['bend_details']
        eway_bill = request.POST['eway_bill']
        applicable_form = request.POST['applicable_form']
        threshold_includes = request.POST['threshold_includes']
        threshold_limit = request.POST['threshold_limit']
        intrastate = request.POST['intrastate']
        threshold_limit1 = request.POST['threshold_limit1']
        print_eway = request.POST['print_eway']
        e_invoice = request.POST['e_invoice']
        
       
        mdl = Gst_Details(
            state=state,
            reg_type=reg_type,
            assessee=assessee,
            app_form=app_form,
            gstin=gstin,
            gstr1=gstr1,
            flood=flood,rate_details=rate_details,advance_receipts=advance_receipts,
            reverse_charge=reverse_charge,classifications=classifications,bend_details=bend_details,
            eway_bill=eway_bill,applicable_form=applicable_form,threshold_includes=threshold_includes,
            threshold_limit=threshold_limit,intrastate=intrastate,threshold_limit1=threshold_limit1,
            print_eway=print_eway,e_invoice=e_invoice,
            company=cm
        )
        mdl.save()
        return redirect('index')
    return render(request,'features.html',{'ctg':cm})

def featurepage(request):
    comp=Companies.objects.all()
    return render(request,'featurepage.html',{'comp':comp})