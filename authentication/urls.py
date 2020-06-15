from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginview, name='login_url'),
    path('logout/', views.logoutview, name='logout_url'),
    path('signup/', views.Adduser.as_view(), name='signup'),
]
