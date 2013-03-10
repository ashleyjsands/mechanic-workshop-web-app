# Copyright (c) 2013 Ashley Sands (ajsands.com.au)
from django.db import models

from account.models import UserOwnedBase


class Customer(UserOwnedBase):
	name = models.CharField(max_length=100)
	adress_line_1 = models.CharField(max_length=100, blank=True)
	adress_line_2 = models.CharField(max_length=100, blank=True)
	# TODO: add country field.
