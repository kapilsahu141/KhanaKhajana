from django.db import models

# Create your models here.
class TestTable(models.Model):
    name2=models.CharField(max_length=122)
    email2=models.CharField(max_length=122)
    phone2=models.CharField(max_length=122)
class TestTable1(models.Model):
    uname=models.CharField(max_length=122)
    date=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    number=models.CharField(max_length=122)
    food1=models.CharField(max_length=122)
    restaurant=models.CharField(max_length=122)
    drinks=models.CharField(max_length=122)
    soups=models.CharField(max_length=122)
    dishes=models.CharField(max_length=122)
    order=models.CharField(max_length=122)
   



