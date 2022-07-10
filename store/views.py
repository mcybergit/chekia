from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
)
from .models import Stors
# Create your views here.

class Dashboard(View):
    def get(self, request, id):

        store = get_object_or_404(Stors, id=id)
        

        context={
            'store' : store,

        }


        return render(request,'dashboard/dashboard.html', context)