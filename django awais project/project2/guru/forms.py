from django import forms
from .models import Company, Income, Expense

class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields='__all__'
        labels={'name':'Enter Company Name','location':"enter location"}


class IncomeForm(forms.ModelForm):
    class Meta:
        model=Income
        fields='__all__'


class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields='__all__'
