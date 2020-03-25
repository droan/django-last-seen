from last_seen.models import clear_interval

from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect


def clear(request):
    """ Testing view to force clear interval of user"""
    clear_interval(request.user)
    return redirect("/admin")


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^clear/', clear),
]
