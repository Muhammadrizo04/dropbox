from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    path('', file_manager, name='index'),
    path('file-manager/', file_manager, name='file_manager'),
    re_path(r'^file-manager/(?P<directory>.*)?/$', file_manager, name='file_manager'),
    path('delete-file/<str:file_path>/', delete_file, name='delete_file'),
    path('delete-folder/<str:folder_path>/', delete_folder, name='delete_folder'),
    path('download-file/<str:file_path>/', download_file, name='download_file'),
    path('upload-file/', upload_file, name='upload_file'),
    path('save-info/<str:file_path>/', save_info, name='save_info'),
    path('create-folder/', create_folder, name='create_folder'),
    path('rename/<str:file_path>/', rename_file, name='rename_file'),
    path('rename_folder/<str:folder_path>/', rename_folder, name='rename_folder'),

]
