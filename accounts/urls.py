from django.urls import path
from .views import *

urlpatterns = [
    path('create/', user_create_view,name = 'signup'),
    path('login/', login_view,name = 'login'),
    path('logout/', logout_view ,name = 'logout'),
    path('change-password/', change_password_view, name='change_password'),

]