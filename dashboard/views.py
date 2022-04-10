from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Sale_static,Income,Expenses
from django.contrib.auth.decorators import login_required
from .forms import IncomeForm

# Create your views here.
@login_required()
def index(request):
    return render(request, 'dashboard/index.html',)

@login_required()
def staff(request):
    return render(request,'dashboard/staff.html',)

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
    return render(request,'dashboard/income_delete.html')

@login_required()
def expenses(request):
    return render(request,'dashboard/expenses.html',)

@login_required()
def sale(request):
    return render(request,'dashboard/sale.html',)
