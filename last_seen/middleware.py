from last_seen.models import user_seen

from django.utils.deprecation import MiddlewareMixin


class LastSeenMiddleware(MiddlewareMixin):
    """
        Middleware to set timestampe when a user
        has been last seen
    """
    def process_request(self, request):
        if request.user.is_authenticated():
            user_seen(request.user)

        return None
