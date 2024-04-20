from django.urls import path
from .views import *


urlpatterns = [
    path('', login_view, name='login'),
    path('register/', user_create_view, name='register'),
    path('index/', index_view, name='index'), 
    path('logout/', logout_view, name='logout'),
]
