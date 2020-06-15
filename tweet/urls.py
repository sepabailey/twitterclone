from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('addtweet/<int:user_id>', views.add_tweet.as_view(), name='addtweet'),
    path('addtweet/<int:user_id>', views.add_tweet, name='addtweet'),
    path('tweet/<int:tweet_id>', views.Tweet_view.as_view(), name='tweet_view'),

]
