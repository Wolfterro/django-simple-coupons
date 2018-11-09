from django.contrib.admin import ModelAdmin
from django.utils import timezone


# Create your actions here
# ========================
def reset_coupon_usage(modeladmin, request, queryset):
    for coupon_user in queryset:
        coupon_user.times_used = 0
        coupon_user.save()

    ModelAdmin.message_user(modeladmin, request, "Coupons reseted!")


def delete_expired_coupons(modeladmin, request, queryset):
    count = 0
    for coupon in queryset:
        expiration_date = coupon.ruleset.validity.expiration_date
        if timezone.now() >= expiration_date:
            coupon.delete()
            count += 1

    ModelAdmin.message_user(modeladmin, request, "{0} Expired coupons deleted!".format(count))


# Actions short descriptions
# ==========================
reset_coupon_usage.short_description = "Reset coupon usage"
delete_expired_coupons.short_description = "Delete expired coupons"
