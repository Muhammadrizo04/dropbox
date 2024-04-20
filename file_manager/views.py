from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login, authenticate
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def index_view(request):
    return render(request, 'index.html', {'user': request.user})

def login_view(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect(request.GET.get('next', 'index'))
                else:
                    error = 'Your account is not active.'
            else:
                error = 'Invalid username or password.'
        else:
            error = "Please correct the errors below."
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'error': error, "form": form})

def user_create_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password2'])
            new_user.save()
            return redirect('login')
        else:
            error = 'Please correct the errors below.'
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')