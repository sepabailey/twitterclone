from django.shortcuts import render, reverse, HttpResponseRedirect
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from tweet.forms import AddTweet
import re
from notification.models import Notification
from django.contrib.auth.decorators import login_required
from django.views.generic import View


@login_required
def add_tweet(request, user_id):
    form = AddTweet()
    if request.method == "POST":
        form = AddTweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            all_user = TwitterUser.objects.all()
            user = TwitterUser.objects.get(id=user_id)
            tweet = Tweet.objects.create(
                tweet=data['tweet'],
                author=user
            )
            # https://stackoverflow.com/questions/7150652/regex-valid-twitter-mention
            # Matt Perry helped with the regex and notifications
            find_users = re.findall(r'@(\w+)', data['tweet'])
            for tagged in find_users:
                Notification.objects.create(
                    notify_user=TwitterUser.objects.get(username=tagged),
                    tweet=tweet,
                )

            return HttpResponseRedirect(reverse('homepage'))
    return render(request, 'addtweet.html', {'form': form})

    def post(self, request):
        if request.method == "POST":
            form = AddTweet(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                all_user = TwitterUser.objects.all()
                user = TwitterUser.objects.get(id=user_id)
                tweet = Tweet.objects.create(
                    tweet=data['tweet'],
                    author=user
                )
            # https://stackoverflow.com/questions/7150652/regex-valid-twitter-mention
            # Matt Perry helped with the regex and notifications
                find_users = re.findall(r'@(\w+)', data['tweet'])
                for tagged in find_users:
                    Notification.objects.create(
                        notify_user=TwitterUser.objects.get(username=tagged),
                        tweet=tweet,
                    )
                return HttpResponseRedirect(reverse('homepage'))


class Tweet_view(View):
    def get(self, request, tweet_id):
        tweet = Tweet.objects.get(id=tweet_id)
        return render(request, 'tweet.html', {'tweet': tweet})
