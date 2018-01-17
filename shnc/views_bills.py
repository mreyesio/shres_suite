from django.shortcuts import render
from shnc.forms import BillForm
from shnc.models import Bills

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,UpdateView, DeleteView, ListView, DetailView, CreateView)

###########################################
###########################################

###########################################
###########################################
class BillListView(LoginRequiredMixin,ListView):
    login_url = '/shnc/user_login/'
    context_object_name = 'bills'
    template_name = 'shnc/bills/bill_list.html'   
    model = Bills
    
        
class BillDetailView(DetailView):
    login_url = '/shnc/user_login/'
    context_object_name = 'bill'
    template_name = 'shnc/bills/bill_details.html'

    model = Bills
    
class CreateBillView(LoginRequiredMixin,CreateView):
    login_url = '/shnc/user_login/'
    redirect_field_name = '/shnc/bills/'
    template_name = 'shnc/bills/bill_new.html'
    
    form_class = BillForm
    model = Bills  

###########################################
###########################################
