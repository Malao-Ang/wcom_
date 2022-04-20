from django import forms
from .models import Income,Expenses,Sale_static


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['list','price','note','day','month','year']
        
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['list','price','note','day','month','year']

class Sale_staticForm(forms.ModelForm):
    class Meta:
        model = Sale_static
        fields = ['brand','price','location','phone','note','day','month','year']