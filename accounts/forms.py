from dataclasses import field
from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import PasswordChangeForm

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User 
        fields = ['old_password', 'new_password1', 'new_password2']

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name','last_name','username')
        widget = { 'first_name':forms.TextInput(attrs={
                'placeholder':'Name',
                'class':"form-control w-50"
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'LastName',
                'class':"form-control w-50"
            }),
            'username':forms.TextInput(attrs={
                'placeholder':'Username',
                'class':"form-control w-50"
            }),
        }


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            return None
        else:
            return cd['password2']

class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control w-50' }))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control w-50'}))