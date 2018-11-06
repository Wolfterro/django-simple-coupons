# Validations

To ensure that the rules from the ruleset are being followed, some validations are required. If you call ```coupon.use_coupon(user)``` without validating first, it'll always assume that the coupon is valid and will be used regardless if it's really valid or not.

There's a couple of functions to check if a coupon is valid before using it.

## Functions

- ##### validate_coupon(coupon_code=\<str\>, user=\<User Object\>) -> Dict

This is the main validation function to call, you don't need to call another function. With it, you can validate the coupon and the user that will be using that coupon.

Returns a dict with one key (if valid), or two keys (if not valid).

##### Example:

```python
from django.contrib.auth.models import User
from django_simple_coupons.validations import validate_coupon

user = User.objects.get(username="john_doe")
coupon_code_valid = "COUPONTEST01"

valid = validate_coupon(coupon_code=coupon_code_valid, user=user)
# {'valid': True}

coupon_code_invalid = "DUMMYCOUPON0"
invalid = validate_coupon(coupon_code=coupon_code_invalid, user=user)
# {'valid': False, 'message': 'Coupon does not exist!'}
```

After validating the coupon and the user, you can call ```coupon.use_coupon(user)``` without any problem.