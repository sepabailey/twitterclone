from django.shortcuts import render, reverse, HttpResponseRedirect
from twitteruser.models import TwitterUser
from django.contrib.auth import login, logout, authenticate
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    tweet_data = Tweet.objects.all()
    user_data = TwitterUser.objects.all()
    return render(request, 'index.html', {
        "tweet_data": tweet_data, "user_data": user_data
    })


# Peter helped to add a twitteruser helping with follow and unfollow
def profile_view(request, user_id):
    # count of users they follow
    # count of tweets user wrote
    user_tweets = Tweet.objects.filter(author=user_id)
    twitteruser = TwitterUser.objects.get(id=user_id)
    following_list = twitteruser.following.all()
    followers_count = following_list.count()
    if request.user.is_authenticated:
        current_following_list = request.user.following.all()
        tweet_count = user_tweets.count()
        if twitteruser in current_following_list:
            is_following = True
        else:
            is_following = False

        return render(request, 'profile.html', {'user_tweets': user_tweets, 'is_following': is_following, 'twitteruser': twitteruser, 'followers_count': followers_count, 'tweet_count': tweet_count})

    return render(request,
                  'profile.html', {
                      'user_tweets': user_tweets,
                      'twitteruser': twitteruser,
                      'followers_count': followers_count,
                  })


# https://stackoverflow.com/questions/6218175/how-to-implement-followers-following-in-django
def follow_user(request, id):
    current_user = request.user
    follow_user = TwitterUser.objects.get(id=id)
    current_user.following.add(follow_user)
    current_user.save()
    return HttpResponseRedirect(reverse('profile', kwargs={'user_id': id}))


def unfollow_user(request, id):
    current_user = request.user
    follow_user = TwitterUser.objects.get(id=id)
    current_user.following.remove(follow_user)
    current_user.save()
    return HttpResponseRedirect(reverse('profile', kwargs={'user_id': id}))
