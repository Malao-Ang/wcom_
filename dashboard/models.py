from email.policy import default
from pyexpat import model
from sre_constants import CATEGORY
from django.db import models
from django import forms
import datetime
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Acer','Acer'),
    ('Macbook','Macbook'),
    ('HP','HP'),
    ('ASUS','ASUS'),
    ('Dell','Dell'),
    ('LG','LG'),
    ('Compaq','Compaq'),
    ('Lenovo','Lenovo'),
    ('Toshiba','Toshiba'),
    ('MSI','MSI')
)

LOCATION = (
    ('online','online'),
    ('offline','offline'),
)
LISTINCOME = (
    ('Windows','Windows'),
    ('Upgrade','Upgrade'),
    ('Accessories','Accessories'),
    ('Battery','Battery'),
    
    
)
LISTEXPENSES = (
    ('shop rent','shop rent'),
    ('Accessories','Accessories')
)

class Sale_static(models.Model):
    date = models.DateTimeField(auto_now_add=True , blank=False)
    brand = models.CharField(max_length=100,choices = CATEGORY,null=False)
    price = models.PositiveIntegerField(null=False)
    location = models.CharField(max_length=20,choices = LOCATION,null=False)
    phone = models.CharField(max_length=10,blank=True)
    note = models.CharField(max_length=1000,blank=True)

    def __str__(self):
        return f'{self.brand}-{self.price} BATH'

class Income(models.Model):
    list = models.CharField(max_length=20,choices=LISTINCOME,null=False)
    price = models.PositiveIntegerField(null=False)
    date = models.DateTimeField(auto_now_add=True , blank=False)
    note = models.CharField(max_length=1000,blank=True)

    
class Expenses(models.Model):
    list = models.CharField(max_length=20,choices=LISTEXPENSES,null=False)
    price = models.PositiveIntegerField(null=False)
    date = models.DateTimeField(auto_now_add=True , blank=False)
    note = models.CharField(max_length=1000,blank=True)

    

