import string
import random

from django.conf import settings
from django.contrib.auth.models import User


def get_coupon_code_length(length=12):
    return settings.DSC_COUPON_CODE_LENGTH if hasattr(settings, 'DSC_COUPON_CODE_LENGTH') else length


def get_user_model():
    return settings.DSC_USER_MODEL if hasattr(settings, 'DSC_USER_MODEL') else User


def get_random_code(length=12):
    length = get_coupon_code_length(length=length)
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length))
