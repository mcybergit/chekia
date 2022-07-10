
from django.db import models
from datetime import datetime
from store.models import Stors
# Create your models here.

class Persons(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.ForeignKey(Stors , blank=True, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=11)
    national_number = models.CharField(max_length=10)
    addres = models.CharField(max_length=1000, null=True, blank=True)
    customer = models.BooleanField(default=False)
    guarantor = models.BooleanField(default=False)
    create_time = models.DateTimeField(default=datetime.now)
    last_edite_time = models.DateTimeField(null=True, blank=True)
    delete_time = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name