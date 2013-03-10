# Copyright (c) 2013 Ashley Sands (ajsands.com.au)

from django.db import models
from django.contrib.auth.models import User, UserManager


account_types = [
	("trial", "trial"),
	("paid", "paid"),
]

class BillingAccount(models.Model):

	name = models.CharField(max_length=100)
	registered_date = models.DateField()
	type = models.CharField(max_length=100, choices=account_types)

class UserAccount(User):
	objects = UserManager()

	billing_account = models.ForeignKey(BillingAccount)

class UserOwnedBase(models.Model):
	account = models.ForeignKey(BillingAccount) # This field is implied by the created_by field, but it is added here as a shortcut.
	created_by = models.ForeignKey(UserAccount, related_name="%(app_label)s_%(class)s_created_by")
	modified_by = models.ForeignKey(UserAccount, related_name="%(app_label)s_%(class)s_modified_by")

	class Meta:
		abstract = True
