from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import login as auth_login, authenticate
from django.urls import reverse

from .forms import UserRegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Folder, File


def login_required_decorator(view_func):
    return login_required(view_func, login_url='login')


@login_required
def file_manager(request, guid=None):
    if guid:
        folder = get_object_or_404(Folder, guid=guid)
        folders = folder.get_subfolders()
        user_files = File.objects.filter(folder=folder)
    else:
        user_folders = Folder.objects.filter(owner=request.user, parent_folder=None)
        user_files = File.objects.filter(folder__parent_folder=None)
        print(user_folders)
        return render(request, 'file_manager.html', {
            'user': request.user,
            'user_folders': user_folders,
            'user_files': user_files,
        })

    return render(request, 'file_manager.html', {
        'user': request.user,
        'user_folders': folders,
        'user_files': user_files,
        'folder_item': folder,
        'folder': folders.first(),
    })


def login_view(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect(reverse('index'))
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


def create_folder(request):
    pass


def rename_folder(request):
    pass


def delete_folder(request):
    pass


def upload_file(request):
    pass


def delete_file(request):
    pass


def rename_file(request):
    pass


def share_file(request):
    pass
