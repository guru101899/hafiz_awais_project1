from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100, default='Unknown')

class Income(models.Model):
    company_income = models.IntegerField()
    total_income = models.IntegerField(default=0)

class Expense(models.Model):
    company_expense = models.IntegerField()
    total_expense = models.IntegerField(default=0)  
