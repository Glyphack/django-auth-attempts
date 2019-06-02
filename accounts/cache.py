import logging
from django.core.cache import cache
logger = logging.getLogger(__name__)


class InvalidLoginAttemptsCache:
    @staticmethod
    def _key(username):
        return 'invalid_login_attempt_{}'.format(username)

    @staticmethod
    def _value(lockout_timestamp, timebucket):
        return {
            'lockout_start': lockout_timestamp,
            'invalid_attempt_timestamps': timebucket
        }

    @staticmethod
    def delete(username):
        try:
            cache.delete(InvalidLoginAttemptsCache._key(username))
        except Exception as e:
            logger.exception(e)

    @staticmethod
    def set(username, timebucket, lockout_timestamp=None):
        try:
            key = InvalidLoginAttemptsCache._key(username)
            value = InvalidLoginAttemptsCache._value(lockout_timestamp, timebucket)
            cache.set(key, value)
        except Exception as e:
            logger.exception(e.message)

    @staticmethod
    def get(username):
        try:
            key = InvalidLoginAttemptsCache._key(username)
            return cache.get(key)
        except Exception as e:
            logger.exception(e.message)
