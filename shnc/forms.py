from django import forms
from django.core import validators
from shnc.models import LpnData, UserProfileInfo,Bills
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# create custom validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Does not start with z")
###########################################

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'New Username','autocomplete':'off'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New Password', 'autocomplete': 'new-password'}) )
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'example: abc@gmail.com','autocomplete':'off'}))
    class Meta:
        model = User
        fields = ('username','email','password')
        
class user_profile_form(forms.ModelForm):
    phone_number = forms.CharField(label='Phone Number',required=False)
    
    class Meta:
        model = UserProfileInfo
        fields = ('privileges','phone_number')

###########################################
#forms
class add_nurse_form(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    middle_name = forms.CharField(label='Middle Name' ,required=False)
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(label='Phone Number',required=False)
    # text = forms.CharField(widget=forms.Textarea)
    license_id = forms.CharField(label='License ID') 
    license_exp = forms.DateField(label='License Expiration',widget=forms.TextInput(attrs={'placeholder': 'Format:   01/01/2018'}))
    cpr_exp = forms.DateField(label='CPR Expiration' )
    cpr_provider = forms.CharField(label='CPR Provider' )
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    
    class Meta:
        model = LpnData
        fields = '__all__'
        
###########################################

class BillForm(forms.ModelForm):
    
    class Meta:
        model = Bills
        fields = '__all__'
 