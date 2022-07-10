from django.urls import path
from . import views

urlpatterns = [
    path('<id>/', views.Dashboard.as_view(), name='dashboard'),

]