from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

from mptt.models import MPTTModel, TreeForeignKey


class StorCategory(MPTTModel):
    category = models.CharField(max_length=20)
    parent = TreeForeignKey('self', blank=True, null=True,on_delete=models.CASCADE,related_name="child")
    def __str__(self) -> str:
        return self.category
    class MPTTMeta:
        order_insertion_by = ['category']
   

class Stors(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(StorCategory, related_name="category_stor",blank=True, null=True, on_delete=models.SET_NULL)
    stor_name = models.CharField(max_length=255)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=datetime.now)
    number_staff = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.stor_name
