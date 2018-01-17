from django.shortcuts import render
from shnc.forms import user_profile_form,UserForm
# from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,UpdateView, DeleteView, ListView, DetailView, CreateView)
from django.contrib.auth.models import User


###########################################
###########################################

def index(request):
    my_dict = {'insert_me':"hello dsfsfsd views"}
    context_dict = {'text':"hello world", 'number':34}
    return render(request,'shnc/login.html', context=context_dict)

###########################################
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    
###########################################  

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('shnc:welcome'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("not correct login")
            return HttpResponseRedirect(reverse('shnc:user_login'))
    else:
        return render(request,'shnc/login.html')

###########################################    
@login_required    
def welcome(request):
    return render(request,'shnc/welcome.html')
    

###########################################    



class AdminListView(LoginRequiredMixin,ListView):
    login_url = '/shnc/user_login/'
    model = User
    context_object_name = 'users'
    template_name = 'shnc/admin/admin_list.html'
    # def get_queryset(self):
    #     return LpnData.objects.all()
    
class AdminDetailView(LoginRequiredMixin,DetailView):
    login_url = '/shnc/user_login/'
    model = User        
    context_object_name = 'user'
    template_name = 'shnc/admin/admin_details.html'


    
###########################################    

@login_required        
def add_user(request):
    if request.method=='POST':
        profile_form=user_profile_form(request.POST) 
        user_form = UserForm(request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse('shnc:admin'))
        else:
            print("error form invald")
        #save data to db 
    else:
        profile_form=user_profile_form() 
        user_form = UserForm()
        return render(request,'shnc/admin/add_user.html',{'profile_form':profile_form, 'user_form':user_form})

