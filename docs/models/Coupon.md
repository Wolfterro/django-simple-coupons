# Coupon

Each coupon has a ***code***, ***discount*** and set of rules (known as ***ruleset*** in the admin).

Every time you click ```Add Coupon```, a new coupon code will be generated randomly for you. Don't worry, you can set your own personal code if you wish.

![create-coupon](https://github.com/Wolfterro/django-simple-coupons/raw/master/docs/images/coupon-create.png)

Each ruleset has three basic rules that you need to supply: ***Allowed user rule***, ***Max uses rule*** and ***Validity rule***.

For the ***Ruleset*** documentation, see:

##### [https://github.com/Wolfterro/django-simple-coupons/blob/develop/docs/models/Ruleset.md](https://github.com/Wolfterro/django-simple-coupons/blob/develop/docs/models/Ruleset.md)

## Methods (Instance)

- ##### coupon.use_coupon(user=\<User Object\>) -> None

Uses the coupon ***WITHOUT ANY VALIDATION!*** To validate first, check the ***Validations*** doc:

##### [https://github.com/Wolfterro/django-simple-coupons/blob/develop/docs/validation/Validations.md](https://github.com/Wolfterro/django-simple-coupons/blob/develop/docs/validation/Validations.md)

##### Example:

```python
from django.contrib.auth.models import User

from django_simple_coupons.validations import validate_coupon
from django_simple_coupons.models import Coupon

coupon_code = "COUPONTEST01"
user = User.objects.get(username="john_doe")

status = validate_coupon(coupon_code=coupon_code, user=user)
if status['valid']:
    coupon = Coupon.objects.get(code=coupon_code)
    coupon.use_coupon(user=user)
```

<hr>

- ##### coupon.get_discount() -> Dict

Returns a dict with two keys, with the discount ***value*** and if it's ***percentage*** or not.

For the ***Discount*** documentation, see:

##### [https://github.com/Wolfterro/django-simple-coupons/blob/develop/docs/models/Discount.md](https://github.com/Wolfterro/django-simple-coupons/blob/develop/docs/models/Discount.md)

##### Example:

```python
from django_simple_coupons.models import Coupon

coupon_code = "COUPONTEST01"
coupon = Coupon.objects.get(code=coupon_code)

discount = coupon.get_discount()  # Example: {'value': 50, 'is_percentage': True} 
```