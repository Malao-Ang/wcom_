import re
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Sale_static,Income,Expenses
from django.contrib.auth.decorators import login_required
from .forms import IncomeForm,ExpenseForm,Sale_staticForm
from django.db import connection
import math


# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html',)

@login_required()
def staff(request):
    return render(request,'dashboard/staff.html',)

@login_required()
def sale_static(request):
    items = Sale_static.objects.all() #Use ORM
    # items = Income.objects.raw('SELECT * FROM dashboard_income')
    
    if request.method == 'POST':
        form = Sale_staticForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-sale')
    else:
        form = Sale_staticForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request,'dashboard/sale.html',context)

def sale_static_delete(request,ind):
    item = Sale_static.objects.get(id=ind)
    if request.method == "POST":
        item.delete()
        return redirect('dashboard-sale')
    return render(request,'dashboard/sale_delete.html')


def sale_static_update(request,ind):
    item = Sale_static.objects.get(id=ind)
    if request.method == 'POST':
        form = Sale_staticForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-sale')
    else:
        form = Sale_staticForm(instance=item)
    
    context = {
        'form': form,
    }
    return render(request,'dashboard/sale_update.html',context)

    

@login_required()
def income(request):
    items = Income.objects.all() #Use ORM
    # items = Income.objects.raw('SELECT * FROM dashboard_income')
    
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-income')
    else:
        form = IncomeForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request,'dashboard/income.html',context)


def Income_delete(request,ind):
    item = Income.objects.get(id=ind)
    if request.method == "POST":
        item.delete()
        return redirect('dashboard-income')
    return render(request,'dashboard/income_delete.html')


def Income_update(request,ind):
    item = Income.objects.get(id=ind)
    if request.method == 'POST':
        form = IncomeForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-income')
    else:
        form = IncomeForm(instance=item)
    
    context = {
        'form': form,
    }
    return render(request,'dashboard/income_update.html',context)


@login_required()
def expenses(request):
    items = Expenses.objects.all() #Use ORM
    # items = Income.objects.raw('SELECT * FROM dashboard_income')
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-expenses')
    else:
        form = ExpenseForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request,'dashboard/expenses.html',context)

def expenses_delete(request,ind):
    item = Expenses.objects.get(id=ind)
    if request.method == "POST":
        item.delete()
        return redirect('dashboard-expenses')
    return render(request,'dashboard/expense_delete.html')


def expenses_update(request,ind):
    item = Expenses.objects.get(id=ind)
    if request.method == 'POST':
        form = ExpenseForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-expenses')
    else:
        form = ExpenseForm(instance=item)
    
    context = {
        'form': form,
    }
    return render(request,'dashboard/expense_update.html',context)


@login_required()
def sale(request):
    return render(request,'dashboard/sale.html',)

@login_required()
def staff(request):
    num =  Sale_static.objects.all().count()
    this = Sale_static.objects.all()
    price  = []
    r = 0
    for i in range(num):
        result = str(this[i].price)
        if result not in price:
            price.append(str(result))
    count = [0]*len(price)
    for i in range(num):
        result = str(this[i].price)
        for j in range(len(price)):
            if result == price[j]:
                count[j] += 1
            else:
                continue


    incomes = Income.objects.all()
    totalBat = cal_Price(Income,'Battery')
    totalWin = cal_Price(Income,'Windows')
    totalUp = cal_Price(Income,'Upgrade')
    totalAcc = cal_Price(Income,'Accessories')
    
    expenses = Expenses.objects.all()
    totalRent = cal_Price(Expenses,'shop rent')
    totalAcce = cal_Price(Expenses,'Accessories')
    
    sale_static = Sale_static.objects.all()
    totalAcer = cal_PriceSale(Sale_static,'Acer')
    totalMac = cal_PriceSale(Sale_static,'Macbook')
    totalHp= cal_PriceSale(Sale_static,'HP')
    totalAsus = cal_PriceSale(Sale_static,'ASUS')
    totalDell = cal_PriceSale(Sale_static,'Dell')
    totalLG = cal_PriceSale(Sale_static,'LG')
    totalCompaq = cal_PriceSale(Sale_static,'Compaq')
    totalLe = cal_PriceSale(Sale_static,'Lenovo')
    totalToshi = cal_PriceSale(Sale_static,'Toshiba')
    totalMSI = cal_PriceSale(Sale_static,'MSI')
    
    uniquePriceLaptop = price
    numOfPriceLaptop = count
    
    
    totalOffline = onlineVsoffline(Sale_static,'offline')
    totalOnline = onlineVsoffline(Sale_static,'online')
    
    totalProfit = totalBat+totalWin+totalUp+totalAcc+totalUp+totalAcer+totalMac+totalHp+totalAsus+totalDell+totalLG+totalCompaq+totalLe+totalToshi+totalMSI
    totalExpense = totalRent+totalAcce
    

    
    PercenProfit = round(((totalProfit-totalExpense)/totalProfit)*100,2)

    print(totalOffline,totalOnline) 
    context = {
        'incomes': incomes,
        'expenses': expenses,
        'sale_static': sale_static,
        'totalBat': totalBat,
        'totalWin': totalWin,
        'totalAcc': totalAcc,
        'totalUp': totalUp,
        
        'totalRent': totalRent,
        'totalAcce':totalAcce,
        
        'totalAcer': totalAcer,
        'totalMac': totalMac,
        'totalHp': totalHp,
        'totalAsus': totalAsus,
        'totalDell': totalDell,
        'totalLG': totalLG,
        'totalCompaq':totalCompaq,
        'totalLe':totalLe,
        'totalToshi':totalToshi,
        'totalMSI':totalMSI,
        
        'uniquePriceLaptop': uniquePriceLaptop,
        'numOfPriceLaptop':numOfPriceLaptop,
        
        'totalOffline': totalOffline,
        'totalOnline': totalOnline,
        
        'totalProfit':totalProfit,
        'totalExpense':totalExpense,
        
        'PercenProfit':PercenProfit,
    }
    
    return render(request,'dashboard/staff.html',context)

def cal_Price(model,x):
    total_count = model.objects.filter(list=x).count()
    total_list = model.objects.filter(list=x)
    total = 0
    for i in range(total_count):
        total+= total_list[i].price
    return total

def cal_PriceSale(model,x):
    total_count = model.objects.filter(brand=x).count()
    total_list = model.objects.filter(brand=x)
    total = 0
    for i in range(total_count):
        total+= total_list[i].price
    return total

def onlineVsoffline(model,x):
    total = model.objects.filter(location=x).count()
    return total

