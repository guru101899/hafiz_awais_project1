from django.shortcuts import render,redirect
from .models import Company,Expense,Income


def home(request):
    return render (request,'home.html')

def company(request):
    if request.method == "POST":
        xxname=request.POST.get('c_name')
        xxlocation=request.POST.get('c_location')

        new_company=Company(name=xxname,location=xxlocation)
        new_company.save()

        return redirect('/')
    else:
        return render (request,'company.html')

def income(request):
    if request.method == "POST":
        c_income=request.POST.get("company_income")
        t_income=request.POST.get("total_income")

        income_data=Income(company_income=c_income,total_income=t_income)
        income_data.save()
        return redirect('/')

    else:    
        return render (request,'income.html')

def expense(request):
    if request.method == "POST":
        c_expense=request.POST.get("company_expense")
        t_expense=request.POST.get("total_expense")

        expense_data=Expense(company_expense=c_expense,total_expense=t_expense)
        expense_data.save()
        return redirect('/')
    
    else:    
        return render (request,'expense.html')
    
def report(request):

    companies=Company.objects.all()
    incomes=Income.objects.all()
    expenses=Expense.objects.all()

    xxx={'companies':companies,'incomes':incomes,'expenses':expenses}

    return render (request,'report.html',xxx)