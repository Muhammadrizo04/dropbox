from django.urls import path
from .views import *


urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('register/', user_create_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
