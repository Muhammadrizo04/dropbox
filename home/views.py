import os, shutil
import uuid
import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, Http404
from django.conf import settings
from home.models import FileInfo, UserFolder
from django.contrib.auth.decorators import login_required

def rename_folder(request, folder_path):
    try:
        folder_path = folder_path.replace('%slash%', '/')

        new_folder_name = request.POST.get('new_folder_name')

        if new_folder_name:
            original_folder_path = os.path.join(settings.MEDIA_ROOT, str(request.user.username), folder_path)
            new_folder_path = os.path.join(os.path.dirname(original_folder_path), new_folder_name)
            shutil.move(original_folder_path, new_folder_path)

        return redirect(request.META.get('HTTP_REFERER'))

    except Exception as e:
        raise Http404
    
def rename_file(request, file_path):
    try:
        file_path = file_path.replace('%slash%', '/')

        new_filename = request.POST.get('new_filename')

        if new_filename:
            original_file_path = os.path.join(settings.MEDIA_ROOT, file_path)
            new_file_path = os.path.join(os.path.dirname(original_file_path), new_filename)
            os.rename(original_file_path, new_file_path)

        return redirect(request.META.get('HTTP_REFERER'))

    except Exception as e:
        raise Http404   

def delete_folder(request, folder_path):
    folder_path = os.path.join(settings.MEDIA_ROOT, str(request.user.username), folder_path)
    print(folder_path)

    try:
        shutil.rmtree(folder_path)
    except OSError as e:
        pass
    return redirect('file_manager', directory=os.path.dirname(folder_path))

def create_folder(request):
    if request.method == 'POST':
        new_folder_name = request.POST.get('new_folder_name')
        selected_directory = request.POST.get('selected_directory') 
        selected_directory_path = os.path.join(settings.MEDIA_ROOT, selected_directory)
        new_folder_path = os.path.join(selected_directory_path, new_folder_name)

        try:
            os.mkdir(new_folder_path)
        except FileExistsError:
            pass

    return redirect('file_manager', directory=selected_directory)

def convert_csv_to_text(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    text = ''
    for row in rows:
        text += ','.join(row) + '\n'

    return text


def get_files_from_directory(directory_path):

    files = []
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            try:
                print( ' > file_path ' + file_path)
                _, extension = os.path.splitext(filename)
                if extension.lower() == '.csv':
                    csv_text = convert_csv_to_text(file_path)
                else:
                    csv_text = str

                files.append({
                    'file': file_path.split(os.sep + 'media' + os.sep)[1],
                    'filename': filename,
                    'file_path': file_path,
                    'csv_text': csv_text
                })
            except Exception as e:
                print( ' > ' +  str( e ) )    
    return files


def save_info(request, file_path):
    path = file_path.replace('%slash%', '/')
    if request.method == 'POST':
        FileInfo.objects.update_or_create(
            path=path,
            defaults={
                'info': request.POST.get('info')
            }
        )
    
    return redirect(request.META.get('HTTP_REFERER'))


def get_breadcrumbs(request):
    path_components = [component for component in request.path.split("/") if component]
    breadcrumbs = []
    url = ''

    for component in path_components:
        url += f'/{component}'
        if component == "file-manager":
            component = "media"
        breadcrumbs.append({'name': component, 'url': url})

    return breadcrumbs

@login_required
def file_manager(request, directory=''):
    user = request.user
    media_path = os.path.join(settings.MEDIA_ROOT)
    user_folder = os.path.join(media_path, str(user.username))

    selected_directory = os.path.join(user_folder, directory)
    if not selected_directory.startswith(user_folder):
        selected_directory = user_folder

    directories = generate_nested_directory(user_folder, user_folder)
    
    files = []
    selected_directory_path = os.path.join(user_folder, directory)
    if os.path.isdir(selected_directory_path):
        files = get_files_from_directory(selected_directory_path)

    breadcrumbs = get_breadcrumbs(request)

    context = {
        'directories': directories, 
        'files': files,
        "user": user,
        'selected_directory': os.path.relpath(selected_directory, media_path),
        'segment': 'file_manager',
        'breadcrumbs': breadcrumbs
    }
    return render(request, 'pages/file-manager.html', context)



def generate_nested_directory(root_path, current_path):
    directories = []
    for name in os.listdir(current_path):
        if os.path.isdir(os.path.join(current_path, name)):
            unique_id = str(uuid.uuid4())
            nested_path = os.path.join(current_path, name)
            nested_directories = generate_nested_directory(root_path, nested_path)
            directories.append({'id': unique_id, 'name': name, 'path': os.path.relpath(nested_path, root_path), 'directories': nested_directories})
    return directories


# def delete_file(request, file_path):
#     path = file_path.replace('%slash%', '/')
#     absolute_file_path = os.path.join(settings.MEDIA_ROOT, path)
#     os.remove(absolute_file_path)
#     print("File deleted", absolute_file_path)
#     return redirect(request.META.get('HTTP_REFERER'))

def delete_file(request, file_path):
    path = file_path.replace('%slash%', '/')
    absolute_file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(absolute_file_path):
        os.remove(absolute_file_path)
        return redirect(request.META.get('HTTP_REFERER'))
    raise Http404

   
def download_file(request, file_path):
    path = file_path.replace('%slash%', '/')
    absolute_file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(absolute_file_path):
        with open(absolute_file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(absolute_file_path)
            return response
    raise Http404


def upload_file(request):
    media_path = os.path.join(settings.MEDIA_ROOT)
    selected_directory = request.POST.get('directory', '') 
    selected_directory_path = os.path.join(media_path, selected_directory)
    if request.method == 'POST':
        file = request.FILES.get('file')
        file_path = os.path.join(selected_directory_path, file.name)
        with open(file_path, 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

    return redirect(request.META.get('HTTP_REFERER'))