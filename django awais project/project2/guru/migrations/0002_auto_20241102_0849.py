# Generated by Django 3.2.19 on 2024-11-02 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guru', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='expense',
            new_name='company_expense',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='income',
            new_name='company_income',
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='expense',
            name='total_expense',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='income',
            name='total_income',
            field=models.IntegerField(default=0),
        ),
    ]
