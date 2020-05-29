from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweet


class Notification(models.Model):
    notify_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    unread_notifs = models.BooleanField(default=False)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return self.tweet.tweet
