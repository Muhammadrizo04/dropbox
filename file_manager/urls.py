from django.urls import path
from .views import *


urlpatterns = [
    path('', file_manager, name='index'),
    path('login/', login_view, name='login'),
    path('register/', user_create_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('create_folder/', create_folder, name='create_folder'),
    path('open_folder/<str:guid>/', file_manager, name='open_folder'),
    path('rename_folder/<str:guid>/', rename_folder, name='rename_folder'),
    path('remove_folder/<str:guid>/', delete_folder, name='remove_folder'),
]
