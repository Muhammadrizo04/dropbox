from contextlib import redirect_stderr
from distutils.log import error
from .forms import UserRegisterForm,LoginForm, ChangePasswordForm
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages

def login_view(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,username = form.cleaned_data['username'],password = form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    if 'next' in request.GET:
                        return HttpResponseRedirect(request.GET.get('next'))
                    else:
                        return redirect('/')
                else:
                    error = 'User is not active'
                    return render(request,'registration/login.html',{'error':error,"form": LoginForm()})

            else:
                error = 'Username or password was entered incorrectly!!!'
                return render(request,'registration/login.html',{'error':error,"form": LoginForm()})

        else:
            error = "The form was filled out incorrectly!!!"
            return render(request,'registration/login.html',{'error':error,"form": LoginForm()})
    else:
        return render(request,'registration/login.html',{'error':error,"form": LoginForm()})
        

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return render(request, "registration/logout.html", {})


def user_create_view(request):
    error = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = form.save(commit = False)
            if cd['password2']:
                new_user.set_password( cd['password2'])
                new_user.save()
                return redirect('login')
            else:
                error = 'The passwords are not the same!!!'
                return render(request,'registration/create.html',{'form':UserRegisterForm(instance=new_user),'error':error})

        else:
            error = 'Error'
            return render(request,'registration/create.html',{'form':UserRegisterForm(),'error':error})    
    else:
        return render(request,'registration/create.html',{'form':UserRegisterForm(),'error':error})
    
def change_password_view(request):
    error = ''
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')  
        else:
            error = 'Error changing password. Please correct the errors below.'
    else:
        form = ChangePasswordForm(user=request.user)

    return render(request, 'registration/change_password.html', {'form': form, 'error': error})