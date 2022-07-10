from django.db import models
from datetime import datetime
from store.models import Stors
from persons.models import Persons

# Create your models here.




class Transactions(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.ForeignKey(Stors , blank=True, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Persons ,related_name='customer_transaction' , blank=True, null=True, on_delete=models.SET_NULL)
    guarantor = models.ForeignKey(Persons ,related_name='guarantor_transaction', blank=True, null=True, on_delete=models.SET_NULL)
    create_time = models.DateTimeField(default=datetime.now)
    last_edite_time = models.DateTimeField(null=True, blank=True)
    receipt_time = models.DateTimeField(null=True, blank=True)
    goods = models.CharField(max_length=500,blank=True, null=True)
    amount = models.IntegerField()
    profit = models.FloatField()
    term = models.IntegerField()
    description = models.CharField(max_length=1500,blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self) -> str:
        return 'transaction ' + str(self.id)
    


class BankList(models.Model):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to ='uploads/bank_logo/')
    def __str__(self) -> str:
        return self.name


class TransactionDetails(models.Model):
    TYPE_CHOICES = [
        ('1', 'Check'),
        ('2', 'Installment'),   
    ]
    id = models.AutoField(primary_key=True)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)
    type = models.CharField(max_length=1,choices=TYPE_CHOICES, default=1)
    store = models.ForeignKey(Stors, blank=True, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Persons , blank=True, null=True, on_delete=models.SET_NULL)
    bank = models.ForeignKey(BankList,blank=True, null=True, on_delete=models.SET_NULL)
    check_number = models.CharField(max_length=50, blank=True, null=True)
    amount = models.IntegerField()
    create_time = models.DateTimeField(default=datetime.now)
    last_edite_time = models.DateTimeField(null=True, blank=True)
    Passed = models.BooleanField(default=False)
    Passed_time = models.DateTimeField(null=True, blank=True)

