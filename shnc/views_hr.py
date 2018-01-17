from django.shortcuts import render
from shnc.forms import add_nurse_form
from shnc.models import LpnData

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,UpdateView, DeleteView, ListView, DetailView, CreateView)

###########################################
###########################################

class LpnListView(LoginRequiredMixin,ListView):
    login_url = '/shnc/user_login/'
    model = LpnData
    context_object_name = 'lpns'
    template_name = 'shnc/hr/lpn_list.html'
    # def get_queryset(self):
    #     return LpnData.objects.all()
        
class LpnDetailView(LoginRequiredMixin,DetailView):
    login_url = '/shnc/user_login/'
    context_object_name = 'lpn'
    template_name = 'shnc/hr/lpn_details.html'

    model = LpnData
    
class CreateLpnView(LoginRequiredMixin,CreateView):
    login_url = '/shnc/user_login/'
    redirect_field_name = '/shnc/hr/'
    
    template_name = 'shnc/hr/lpn_new.html'
    form_class = add_nurse_form
    model = LpnData        

class LpnUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/shnc/user_login/'
    template_name = 'shnc/hr/lpn_update.html'

    redirect_field_name = '/shnc/hr/'
    
    form_class = add_nurse_form
    
    model = LpnData 
    
class LpnDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/shnc/user_login/'
    model = LpnData   
    success_url = '/shnc/hr/'

