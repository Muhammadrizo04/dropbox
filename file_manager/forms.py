from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': "form-control w-50"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': "form-control w-50"}))
    
    class Meta:
        model = User
        fields = ('email', 'username')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': "form-control w-50"}),
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': "form-control w-50"}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password1') != cd.get('password2'):
            raise ValidationError("Passwords don't match.")
        return cd['password2']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-50'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control w-50'}))
