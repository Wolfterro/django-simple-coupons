# Ruleset

Every coupon needs a set of rules to make it valid and useable.
For now, django-simple-coupons use three basic rules:

##### Allowed user rule:

Defines which users are allowed to use the coupon.

![allowed-user-rule](https://github.com/Wolfterro/django-simple-coupons/raw/master/docs/images/allowed-users-rule.png)

##### Max uses rule:

Defines how many uses the coupon should have in general and for each user.

![max-uses-rule](https://github.com/Wolfterro/django-simple-coupons/raw/master/docs/images/max-uses-rule.png)

##### Validity rule:

Defines the expiration date for the coupon and if it's active or not.

![validity-rule](https://github.com/Wolfterro/django-simple-coupons/raw/master/docs/images/validity-rule.png)