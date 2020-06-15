from django.shortcuts import render, reverse, HttpResponseRedirect
from notification.models import Notification
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View


# Joe helped with the notification section and getting it to function
class Notification_view(View):
    @method_decorator(login_required)
    def notification_view(request):
        notified_user = request.user
        notifications = Notification.objects.filter(
            notify_user=notified_user, unread_notifs=False)
        for notification in notifications:
            notification.unread_notifs = True
            notification.save()
        return render(request, 'notifications.html', {'notifications': notifications, 'notified_user': notified_user})
