from django.db import models

class Countries(models.Model):
    name=models.CharField(max_length=225)
    currency_symbol=models.CharField(max_length=225,default='र')
    formal_name=models.CharField(max_length=225,default='INR')

    
class States(models.Model):
    name=models.CharField(max_length=225)
    country=models.ForeignKey(Countries,on_delete=models.CASCADE,blank=True,null=True)
    
class Companies(models.Model):
    name=models.CharField(max_length=225)
    mailing_name=models.CharField(max_length=225)
    address1=models.CharField(max_length=225)
    address2=models.CharField(max_length=225)
    address3=models.CharField(max_length=225)
    address4=models.CharField(max_length=225)
    pincode=models.CharField(max_length=6)
    telephone=models.CharField(max_length=225)
    mobile=models.CharField(max_length=225)
    fax=models.CharField(max_length=225)
    email=models.EmailField()
    website=models.CharField(max_length=225)
    fin_begin=models.DateField(null=True)
    books_begin=models.DateField(null=True)
    country=models.ForeignKey(Countries,on_delete=models.CASCADE,blank=True,null=True)
    state=models.ForeignKey(States,on_delete=models.CASCADE,blank=True,null=True)
    active=models.BooleanField(default=True)
    
    
class Group(models.Model):
    name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225,null=True)
    under = models.CharField(max_length=225)
    sub_ledger = models.BooleanField(default=False)
    debit_credit = models.BooleanField(default=False)
    calculation = models.BooleanField(default=False)
    used_purchase = models.CharField(max_length=225,null=True,blank=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    nature_of_group=models.CharField(max_length=225)

class Features(models.Model):
    maintain_accounts = models.BooleanField(default=True)
    bill_wise_entry = models.BooleanField(default=True)
    cost_centres = models.BooleanField(default=False)
    interest_calc = models.BooleanField(default=True)
    maintain_inventory = models.BooleanField(default=True)
    integrate_accounts = models.BooleanField(default=True)
    multiple_price_level = models.BooleanField(default=True)
    batches = models.BooleanField(default=True)
    expirydate_batches = models.BooleanField(default=True)
    joborder_processing = models.BooleanField(default=True)
    sub_ledger = models.BooleanField(default=True)
    cost_tracking= models.BooleanField(default=True)
    job_costing = models.BooleanField(default=True)
    discount_invoices = models.BooleanField(default=True)
    Billed_Quantity = models.BooleanField(default=True)
    gst = models.BooleanField(default=False)
    tds = models.BooleanField(default=False)
    tcs = models.BooleanField(default=False)
    vat = models.BooleanField(default=False)
    excise = models.BooleanField(default=True)
    servicetax = models.BooleanField(default=True)
    payroll = models.BooleanField(default=False)
    multiple_addrss = models.BooleanField(default=True)
    vouchers = models.BooleanField(default=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

    


