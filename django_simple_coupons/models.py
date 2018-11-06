from django.db import models
from django.utils import timezone

from django_simple_coupons.helpers import (get_random_code,
                                           get_coupon_code_length,
                                           get_user_model)


# Create your models here.
# ========================
class Ruleset(models.Model):
    allowed_users = models.ForeignKey('AllowedUsersRule', on_delete=models.CASCADE, verbose_name="Allowed users rule")
    max_uses = models.ForeignKey('MaxUsesRule', on_delete=models.CASCADE, verbose_name="Max uses rule")
    validity = models.ForeignKey('ValidityRule', on_delete=models.CASCADE, verbose_name="Validity rule")

    def __str__(self):
        return "Ruleset Nº{0}".format(self.id)

    class Meta:
        verbose_name = "Ruleset"
        verbose_name_plural = "Rulesets"


class AllowedUsersRule(models.Model):
    user_model = get_user_model()

    users = models.ManyToManyField(user_model, verbose_name="Users", blank=True)
    all_users = models.BooleanField(default=False, verbose_name="All users?")

    def __str__(self):
        return "AllowedUsersRule Nº{0}".format(self.id)

    class Meta:
        verbose_name = "Allowed User Rule"
        verbose_name_plural = "Allowed User Rules"


class MaxUsesRule(models.Model):
    max_uses = models.BigIntegerField(default=0, verbose_name="Maximum uses")
    is_infinite = models.BooleanField(default=False, verbose_name="Infinite uses?")
    uses_per_user = models.IntegerField(default=1, verbose_name="Uses per user")

    def __str__(self):
        return "MaxUsesRule Nº{0}".   format(self.id)

    class Meta:
        verbose_name = "Max Uses Rule"
        verbose_name_plural = "Max Uses Rules"


class ValidityRule(models.Model):
    expiration_date = models.DateTimeField(verbose_name="Expiration date")
    is_active = models.BooleanField(default=False, verbose_name="Is active?")

    def __str__(self):
        return "ValidityRule Nº{0}".   format(self.id)

    class Meta:
        verbose_name = "Validity Rule"
        verbose_name_plural = "Validity Rules"


class CouponUser(models.Model):
    user_model = get_user_model()

    user = models.ForeignKey(user_model, on_delete=models.CASCADE, verbose_name="User")
    coupon = models.ForeignKey('Coupon', on_delete=models.CASCADE, verbose_name="Coupon")
    times_used = models.IntegerField(default=0, editable=False, verbose_name="Times used")

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Coupon User"
        verbose_name_plural = "Coupon Users"


class Discount(models.Model):
    value = models.IntegerField(default=0, verbose_name="Value")
    is_percentage = models.BooleanField(default=False, verbose_name="Is percentage?")

    def __str__(self):
        if self.is_percentage:
            return "{0}% - Discount".format(self.value)

        return "${0} - Discount".format(self.value)

    class Meta:
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"


class Coupon(models.Model):
    code_length = get_coupon_code_length()

    code = models.CharField(max_length=code_length, default=get_random_code, verbose_name="Coupon Code", unique=True)
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE)
    times_used = models.IntegerField(default=0, editable=False, verbose_name="Times used")
    created = models.DateTimeField(editable=False, verbose_name="Created")

    ruleset = models.ForeignKey('Ruleset', on_delete=models.CASCADE, verbose_name="Ruleset")

    def __str__(self):
        return self.code

    def use_coupon(self, user):
        coupon_user, created = CouponUser.objects.get_or_create(user=user, coupon=self)
        coupon_user.times_used += 1
        coupon_user.save()

        self.times_used += 1
        self.save()

    def get_discount(self):
        return {
            "value": self.discount.value,
            "is_percentage": self.discount.is_percentage
        }

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(Coupon, self).save(*args, **kwargs)
