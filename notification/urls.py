from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.Notification_view.as_view(), name='notif'),
]
