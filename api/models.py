import re

from django.core.exceptions import ValidationError
from django.db import models

def validateIfsc(value):
    res = re.search('[A-Z]{4}[0-9]{7}')
    if res==None:
        raise ValidationError('{} is not a valid ifsc code'.format(value))



class BankDetail(models.Model):
    ifsc_code = models.CharField(primary_key=True,max_length=11,validators=[validateIfsc])
    bank_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    address = models.CharField(max_length=180)

# Create your models here.
