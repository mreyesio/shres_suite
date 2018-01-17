from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

###########################################
        
class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User)
    privileges = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=80)
    
    def __str__(self):
        return self.user.username
        
###########################################       
class AccessRecord(models.Model):
    # name = models.ForeignKey(Webpage)
    date = models.DateField()
    # time = models.TimeField()
    user = models.CharField(max_length=80)
    form = models.CharField(max_length=80)
    action = models.CharField(max_length=80)
    
    def __str__(self):
        return self.date
        
###########################################        
class LpnData(models.Model):
    
    first_name = models.CharField(max_length=80)
    middle_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=80,unique=True)
    # text = forms.CharField(widget=forms.Textarea)
    license_id = models.CharField(max_length=80,unique=True)
    license_exp = models.DateField()
    cpr_exp = models.DateField()
    cpr_provider = models.CharField(max_length=80)
    
    def publish(self):
        self.save()
        
    def get_absolute_url(self):
        return reverse('shnc:hr') 
        
class Bills(models.Model):
    agency = models.CharField(max_length=80)
    provider = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    date_due = models.DateField()
    amount = models.CharField(max_length=80)
    overdue = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    
    def paid_publish(self):
        self.paid = True
        self.save()
        
    def get_absolute_url(self):
        return reverse("shnc:bills_list") 
        
    def __str__(self):
        return self.provider
# Create your models here.
