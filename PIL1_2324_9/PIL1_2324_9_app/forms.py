from django import forms
from .models import *


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("name","surname","email","password")
        
class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField( max_length=64, required=True)
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio","interests","preferred_age_range","date_of_birth","gender","location","preferred_location","preferred_gender")

