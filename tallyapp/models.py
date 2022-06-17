from django.db import models

class company(models.Model):
    companyname=models.CharField(max_length=225)
    