import string
import random

from django.conf import settings


def get_coupon_code_length(length=12):
    return settings.DSC_COUPON_CODE_LENGTH if hasattr(settings, 'DSC_COUPON_CODE_LENGTH') else length


def get_user_model():
    return settings.AUTH_USER_MODEL


def get_random_code(length=12):
    length = get_coupon_code_length(length=length)
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length))
