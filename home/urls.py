from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    path('', login_required(file_manager), name='index'),
    path('file-manager/', login_required(file_manager), name='file_manager'),
    re_path(r'^file-manager/(?P<directory>.*)?/$', file_manager, name='file_manager'),
    path('delete-file/<str:file_path>/', delete_file, name='delete_file'),
    path('download-file/<str:file_path>/', download_file, name='download_file'),
    path('upload-file/', upload_file, name='upload_file'),
    path('save-info/<str:file_path>/', save_info, name='save_info'),
    path('create-folder/', create_folder, name='create_folder'),

]
