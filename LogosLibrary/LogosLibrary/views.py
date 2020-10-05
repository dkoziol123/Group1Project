from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Sum

now = timezone.now()
def home(request):
   return render(request, 'crm/home.html',
                 {'crm': home})

@login_required
def customer_l(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/customer_list.html',
                 {'customers': customer})

@login_required
def customer_d(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   

@login_required
def customer_e(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   

@login_required
def customer_service(request):
   services = Service.objects.filter(created_date__lte=timezone.now())
   return render(request, 'crm/service_list.html', {'services': services})

@login_required
def customer_service_new(request):
   

@login_required
def customer_service_edit(request, pk):
   service = get_object_or_404(Service, pk=pk)
   
@login_required
def summary(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    
