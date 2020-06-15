from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='homepage'),
    path('profile/<int:user_id>', views.profile_view, name='profile'),
    path('follow/<int:id>', views.follow_user, name='follow'),
    path('unfollow/<int:id>', views.unfollow_user, name='unfollow'),
]
