from django.urls import path
from .views import *


urlpatterns = [
    path('', file_manager, name='index'),
    path('login/', login_view, name='login'),
    path('register/', user_create_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('open_folder/<str:guid>/', file_manager, name='open_folder'),
]
