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


def createcompany(request):
    st=States.objects.all()
    country=Countries.objects.all()
    return render(request,'createcompany.html',{'st':st,'country':country})

def company_create(request):
    
    if request.method=='POST':
        name=request.POST['name']
        mailing_name=request.POST['mailing_name']
        address=request.POST['address']
        
        s=request.POST['state']
        
        
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
            ctg=Companies(name=name,mailing_name=mailing_name,address=address,state=s,country=country,
                pincode=pincode,
                telephone=telephone,mobile=mobile,fax=fax,email=email,website=website,fin_begin=fin_begin,
                books_begin=books_begin,currency_symbol=currency_symbol,formal_name=formal_name,fin_end=a)
            ctg.save()
            messages.info(request,'Company created successfully(Enable the features as per your business needs)')
            return render(request,'features.html',{'cmp':ctg})
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
            
    grup=tally_group.objects.filter(company_id=cmp)
    return render(request,'ledger.html',{'cmp':cmp,'grup':grup})

def costcentre(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        cname = request.POST['cname']
        alia = request.POST['alia']
        under = request.POST['under']
        costc=cost_centre.objects.filter(cname=cname)
        if costc:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            
            data = cost_centre(cname=cname,cost_alias=alia,under=under,company=cmp)
            data.save()
            return redirect('index')
    ccentre=cost_centre.objects.filter(company_id=cmp)
    return render(request,'costcentre.html',{'cmp':cmp,'ccentre':ccentre})

def costcentre2(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        cname = request.POST['cname']
        alia = request.POST['alia']
        under = request.POST['under']
        costc=cost_centre.objects.filter(cname=cname)
        if costc:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            
            data = cost_centre(cname=cname,cost_alias=alia,under=under,company=cmp)
            data.save()
            return redirect('index')
    ccentre=cost_centre.objects.filter(company_id=cmp)
    return render(request,'costcentre2.html',{'cmp':cmp,'ccentre':ccentre})


def ratesofexchange(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        
        currencyName = request.POST['cr']
        stdrate = request.POST['stdrate']
        # sell_voucher_rate = request.POST['sell_voucher_rate']
        sell_specified_rate = request.POST['sell_specified_rate']
        # buy_voucher_rate = request.POST['buy_voucher_rate']
        buy_specified_rate = request.POST['buy_specified_rate']
        mdl = rateofexchange(
            currencyName=currencyName,
            stdrate=stdrate,
            # sell_voucher_rate=sell_voucher_rate,
            sell_specified_rate=sell_specified_rate,
            # buy_voucher_rate=buy_voucher_rate,
            buy_specified_rate=buy_specified_rate,
            company = cmp)
        mdl.save()
        return redirect('index')
    cur=currencyAlteration.objects.filter(company_id=cmp)
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
            voucherActivate=activ_vou_typ,
            voucherNumber=meth_vou_num,
            voucherEffective=use_effct_date,
            advance_con = useadv,
            preventDuplicate =prvtdp,
            transaction=allow_zero_trans,
            voucherNarration=allow_naration_in_vou,
            make_optional=optional,
            provideNarration=provide_narr,
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
        data = currencyAlteration(Symbol=symbol,FormalName=formal_name,ISOCurrency=currency_code,
                        DecimalPlace=decimal_places,showAmount=show_in_millions,
                        suffixSymbol=suffix_symbol,AddSpace=symbol_and_amount,
                        DecimalWords=after_decimal,wordRep=amount_in_words,company=cmp)
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
        grp=tally_group.objects.filter(group_name=gname)
        if grp:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            mdl = tally_group(
                group_name=gname,
                group_alias=alia,
                group_under=under,
                sub_ledger=sub_ledger,
                debit_credit=nett,
                calculation=calc,
                invoice=meth,
                nature=nature,
                gross_profit=gross,
                company=cmp
            )
            mdl.save()
            return redirect('index')
    grup=tally_group.objects.filter(company_id=cmp)
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
        grp=tally_group.objects.filter(name=gname)
        if grp:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            mdl = tally_group(
                group_name=gname,
                group_alias=alia,
                group_under=under,
                sub_ledger=sub_ledger,
                debit_credit=nett,
                calculation=calc,
                invoice=meth,
                nature=nature,
                gross_profit=gross,
                company=cmp
            )
            mdl.save()
            return redirect('index')
    grup=tally_group.objects.filter(company_id=cmp)
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
        comp.address=request.POST['address']
        
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

def company_feature(request,pk):
    id=Companies.objects.get(id=pk)
    if request.method=="POST":
        ma=request.POST['maintain_account']
        be=request.POST['billwise_entry']
        cc=request.POST['cost_centre']
        ic=request.POST['interest_calculation']
        mi=request.POST['maintain_inventry']
        ai=request.POST['account_inventry']
        mpl=request.POST['multiple_pricelevel']
        eb=request.POST['enable_batches']
        edt=request.POST['expiry_date']
        jop=request.POST['job_order_procress']
        ct=request.POST['cost_tracking']
        jc=request.POST['job_costing']
        dc=request.POST['discount_column']
        sa=request.POST['seperte_actual']
        gst=request.POST['gst']
        tds=request.POST['tds']
        tcs=request.POST['tcs']
        vat=request.POST['vat']
        excise=request.POST['excise']
        st=request.POST['service_tax']
        prl=request.POST['payroll']
        maddr=request.POST['multiple_address']
        mark_mod=request.POST['mark_modified']
        cmp_fet=Features(maintain_accounts=ma,bill_wise_entry=be,cost_centres=cc,interest_calc=ic,maintain_inventory=mi,
		integrate_accounts=ai,multiple_price_level=mpl,batches=eb,expirydate_batches=edt,joborder_processing=jop,cost_tracking=ct,job_costing=jc,discount_invoices=dc,
		Billed_Quantity=sa,gst=gst,tds=tds,tcs=tcs,vat=vat,excise=excise,servicetax=st,payroll=prl,multiple_addrss=maddr,
		vouchers=mark_mod,company=id)
        cmp_fet.save()
        return redirect('/')
    return render(request,'features.html',{'cmp':id})

def tally_gst(request,pk):
    company=Companies.objects.get(id=pk)
    return render(request, 'gst.html',{'company':company})

def tds(request,pk):
    comp=Companies.objects.get(id=pk)
    return render(request, 'tds.html',{'company':comp})  

def person(request,pk):
    comp=Companies.objects.get(id=pk)
    return render(request, 'tds_person.html',{'company':comp})

def gst_tax(request,pk):
    company=Companies.objects.get(id=pk)
    return render(request, 'gst_tax.html',{'company':company})
def lut_bond(request):
    return render(request, 'lut_bond.html')

def create_tds(request,pk):
    id=Companies.objects.get(id=pk)
    if request.method=='POST':
        t_reg = request.POST['tan_reg_no']
        tax_clct = request.POST['tax_ded_clctn']
        ded_type = request.POST['deductor_type']
        ded_bd = request.POST['ded_brachdevision']
        prsn_res = request.POST['person_res']
        ignr = request.POST['ignore_it']
        st_itm = request.POST['tds_stock_items']
        ctds=Tds_Details(tan_regno=t_reg,
                        tan = tax_clct,
                        deductor_type = ded_type,
                        deductor_branch = ded_bd,
                        person_details = prsn_res,
                        ignore_it = ignr,
                        active_tds = st_itm,
						company = id)
        ctds.save()
        print("added")
        return redirect('/')
    return render(request,'tds.html')

def person_tds(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		name = request.POST['name']
		sd = request.POST['son_daughter']
		des = request.POST['designation']
		pan = request.POST['pan']
		ftno = request.POST['flat_no']
		pnm = request.POST['premise_name']
		str = request.POST['street']
		are = request.POST['area']
		city = request.POST['city']
		st = request.POST['state']
		pcd = request.POST['pincode']
		m_no = request.POST['mobile_no']
		std = request.POST['std_code']
		tph = request.POST['telephone']
		emal = request.POST['email']
	    
		prs=tds_person(name=name,
                        son_daughter = sd,
                        designation = des,
                        pan = pan,
                        flat_no = ftno,
                        building = pnm,
                        street = str,
                        area = are,
                        town = city,
                        state = st,
                        pincode = pcd,
                        mobile = m_no,
                        std = std,
                        telephone = tph,
                        email = emal,
						company = id)          
		prs.save()
		print("added")
		return redirect('/')
	return render(request,'tds_person.html')

def shutcompany(request):
    com=Companies.objects.all()
    return render(request,'shutcompany.html',{'com':com})

def disable(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=False
    c.save()
    return redirect('shutcompany')


def enable(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=True
    c.save()
    return redirect('shutcompany')


def featurepage(request):
    comp=Companies.objects.all()
    return render(request,'featurepage.html',{'comp':comp})

def create_gst(request,pk):
    id=Companies.objects.get(id=pk)
    if request.method=='POST':
        st = request.POST['state']
        rt = request.POST['registration_type']
        at = request.POST['assessee_territory']
        gsta = request.POST['gst_applicable']
        gstuin = request.POST['gstin_uin']
        prd = request.POST['periodicity']

	# .................regular.................
        kfca = request.POST['kerala_fca']
        af = request.POST['applicable_from']
        gstrd = request.POST['gst_rate_details']
        tla = request.POST['tl_advanceR']
        tlr = request.POST['tl_reverseC']
        gstc = request.POST['gst_classification'] 
        lb = request.POST['lut_bond']

    # ................composition................#
        tr = request.POST['tax_rate']
        tc = request.POST['tax_calculation']
        
        tp = request.POST['tax_purchase']

	# ............e-Way bill applicable...........#
        ea = request.POST['e_waybillA']
        aaf = request.POST['applicable_f']
        tli = request.POST['thresholdlimit_include']
        tl = request.POST['threshold_limit']
        intr = request.POST['intrastate']
        itl = request.POST['ithreshold_limit']
        pnw = request.POST['print_eway']

	# .............e-Invoice applicable..............
        einva = request.POST['e_invoiceA']
        appf = request.POST['app_f']
        bfp = request.POST['billfrom_place']
        peir = request.POST['period_einvoiceR']
        sewdei = request.POST['send_eW_details_einvoice']
        gstd=GST(state=st,
						reg_type=rt,
						assessee=at,
						gst_applicable=gsta,
						gstin=gstuin,
						periodicity=prd,
					# ........regular.......
						flood_cess=kfca,
						applicable_from=af,
						gst_rate_details=gstrd,
						advance_receipts=tla,
						reverse_charge=tlr,
						gst_classification=gstc,
						bond_details=lb,	
					# ........composition.......
						tax_rate=tr,		
						tax_calc=tc,		
						tax_purchase=tp,
					# ........e-Way bill applicable.......
						eway_bill=ea,
						applicable_form=aaf,
						threshold_includes=tli,
						threshold_limit=tl,
						intrastate=intr,
						threshold_limit2=itl,
						print_eway=pnw,
					# ........e-Invoice applicable.......
						e_invoice=einva,
						app_from=appf,
						billfrom_place=bfp,
						dperiod=peir,
						send_ewaybill=sewdei,
						company=id)
        gstd.save()
        print("Added")
        return redirect('/')
    return render(request,'gst.html')