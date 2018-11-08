import sys
import string
import random

from django.conf import settings
from django.contrib.auth import get_user_model as django_get_user_model


def get_coupon_code_length(length=12):
    return settings.DSC_COUPON_CODE_LENGTH if hasattr(settings, 'DSC_COUPON_CODE_LENGTH') else length


def get_user_model():
    return django_get_user_model()


def get_random_code(length=12):
    length = get_coupon_code_length(length=length)
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length))
