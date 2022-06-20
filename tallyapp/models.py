from django.db import models

class Countries(models.Model):
    name=models.CharField(max_length=225)
    
class States(models.Model):
    name=models.CharField(max_length=225)
    country=models.ForeignKey(Countries,on_delete=models.CASCADE,blank=True,null=True)
class Companies(models.Model):
    name=models.CharField(max_length=225)
    mailing_name=models.CharField(max_length=225,default='SOME STRING')
    address1=models.CharField(max_length=225)
    address2=models.CharField(max_length=225)
    address3=models.CharField(max_length=225)
    address4=models.CharField(max_length=225)
    pincode=models.CharField(max_length=225)
    telephone=models.CharField(max_length=225)
    mobile=models.CharField(max_length=225)
    fax=models.CharField(max_length=225)
    email=models.EmailField()
    website=models.CharField(max_length=225)
    fin_begin=models.DateField(null=True)
    books_begin=models.DateField(null=True)
    country=models.ForeignKey(Countries,on_delete=models.CASCADE,blank=True,null=True)
    state=models.ForeignKey(States,on_delete=models.CASCADE,blank=True,null=True)
    currency_symbol=models.CharField(max_length=225,default='SOME STRING')
    formal_name=models.CharField(max_length=225,default='SOME STRING')
