import imp
from re import S
from django.contrib import admin
from .models import (StorCategory,Stors)
# Register your models here.
admin.site.register(StorCategory)
admin.site.register(Stors)