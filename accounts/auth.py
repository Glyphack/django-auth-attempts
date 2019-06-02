import arrow as arrow
from django.contrib.auth import get_user_model, authenticate
from rest_framework import exceptions, authentication

from accounts.cache import InvalidLoginAttemptsCache


class ExampleAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):

        print(request.data)
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if not username or not password:
            raise exceptions.AuthenticationFailed('No credentials provided.')

        is_locked_out(username)
        is_ip_blocked(request.META.get('REMOTE_ADDR'))
        credentials = {
            get_user_model().USERNAME_FIELD: username,
            'password': password
        }

        user = authenticate(**credentials)

        if user is None:
            cache_login_attempt(username, request)
            raise exceptions.AuthenticationFailed('Invalid username/password.')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return user, None


def is_ip_blocked(ip):
    print(f"checking ip{ip}")
    cache_results = InvalidLoginAttemptsCache.get(ip)
    if cache_results and cache_results.get('lockout_start'):
        lockout_start = arrow.get(cache_results.get('lockout_start'))
        locked_out = lockout_start >= arrow.utcnow().shift(minutes=-15)
        if not locked_out:
            InvalidLoginAttemptsCache.delete(ip)
        else:
            raise exceptions.AuthenticationFailed("you're ip is blocked")
    else:
        pass


def is_locked_out(username):
    cache_results = InvalidLoginAttemptsCache.get(username)
    if cache_results and cache_results.get('lockout_start'):
        lockout_start = arrow.get(cache_results.get('lockout_start'))
        locked_out = lockout_start >= arrow.utcnow().shift(minutes=-60)
        if not locked_out:
            InvalidLoginAttemptsCache.delete(username)
        else:
            raise exceptions.AuthenticationFailed("you are locked out")
    else:
        pass


def cache_login_attempt(username, request):
    cache_results = InvalidLoginAttemptsCache.get(username)
    lockout_timestamp = None
    now = arrow.utcnow()
    invalid_attempt_timestamps = cache_results['invalid_attempt_timestamps'] if cache_results else []
    invalid_attempt_timestamps = [timestamp for timestamp in invalid_attempt_timestamps if
                                  timestamp > now.shift(minutes=-60).timestamp]

    invalid_attempt_timestamps.append(now.timestamp)
    if len(invalid_attempt_timestamps) >= 3:
        lockout_timestamp = now.timestamp

    InvalidLoginAttemptsCache.set(username, invalid_attempt_timestamps, lockout_timestamp)
    InvalidLoginAttemptsCache.set(
        request.META['REMOTE_ADDR'],
        invalid_attempt_timestamps,
        lockout_timestamp
    )
