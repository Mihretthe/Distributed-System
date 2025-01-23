from django.urls import path

from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('user/<int:user_id>/', get_user, name='get_user'),
]
