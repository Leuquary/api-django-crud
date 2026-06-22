from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_users, name='get_all_users'),
    path('get', views.get_user, name='get_user'),
    path('user/<str:nick>', views.get_by_nick, name='get_user_by_nick'),
    path('register', views.register_user, name='register_user'),
    path('update', views.update_user, name='update_user'),
    path('delete', views.delete_user, name='delete_user'),
    path('manager', views.manage_user, name='manager_user'),

    path('healthz', views.healthz),
    path('livez', views.livez),
    path('readyz', views.readyz),
    path('startupz', views.startupz)
]