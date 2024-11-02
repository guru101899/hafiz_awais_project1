from django.shortcuts import render,redirect
from .models import Company,Expense,Income
from .forms import CompanyForm,IncomeForm,ExpenseForm


def home(request):
    return render (request,'home.html')

def company(request):
    if request.method == "POST":
        fm=CompanyForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm=CompanyForm()
    return render (request,'company.html',{"form":fm})

def income(request):
    if request.method == "POST":
        fm=IncomeForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')

    else: 
        fm=IncomeForm()   

    return render (request,'income.html',{"form":fm})

def expense(request):
    if request.method == "POST":
        fm=ExpenseForm(request.POST)
        if fm.is_valid():
            fm.save()      
            return redirect('/')
    
    else: 
        fm=ExpenseForm()

    return render (request,'expense.html',{"form":fm})
    
def report(request):

    companies=Company.objects.all()
    incomes=Income.objects.all()
    expenses=Expense.objects.all()

    xxx={'companies':companies,'incomes':incomes,'expenses':expenses}

    return render (request,'report.html',xxx)