from django.contrib import admin
from .models import(Transactions, BankList, TransactionDetails)
# Register your models here.

admin.site.register(BankList)
admin.site.register(Transactions)
admin.site.register(TransactionDetails)
