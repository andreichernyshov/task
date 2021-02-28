from django.urls import path
from .views import (
    login_view, logout_view, register_view, update_view, delete_view)

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('register_done/', login_view, name='register_done'),
    path('update/', update_view, name='update'),
    path('delete/', delete_view, name='delete'),
]