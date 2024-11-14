from django.db import models
from django.contrib import admin
class BankLoan (models.Model):
    loanid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    loantype=models.CharField(max_length=30)
    amount=models.IntegerField()
    c_acnt_num=models.IntegerField()
 
class BankAdmin(admin.ModelAdmin):
    list_display=('loanid','name','loantype','amount','c_acnt_num')