from email.headerregistry import Group
from django.contrib import admin
from .models import Expenses, Income, Sale_static
from django.contrib.auth.models import Group

admin.site.site_header = 'W.computer'

class Sale_staticAdmin(admin.ModelAdmin):
    list_display = ('brand','price','location','date','day','month','year')
    list_filter = ['location','brand','price','date','day','month','year']

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('list','price','note','date','day','month','year')
    list_filter = ['list','date','day','month','year']
    
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('list','price','note','date','day','month','year')
    list_filter = ['list','date','day','month','year']

# Register your models here.
admin.site.register(Sale_static,Sale_staticAdmin)
admin.site.register(Income,IncomeAdmin)
admin.site.register(Expenses,ExpenseAdmin)
# admin.site.unregister(Group)
