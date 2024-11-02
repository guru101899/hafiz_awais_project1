from django.contrib import admin
from .models import Company, Income, Expense

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','location')

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('company_income','total_income')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('company_expense','total_expense')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
