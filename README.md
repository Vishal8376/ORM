# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py
from django.contrib import admin
from .models import BankLoan,BankAdmin
admin.site.register(BankLoan,BankAdmin)

models.py
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

```


## OUTPUT

![alt text](<Screenshot 2024-11-14 133822.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
