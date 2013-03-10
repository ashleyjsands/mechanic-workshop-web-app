# Copyright (c) 2013 Ashley Sands (ajsands.com.au)
from django.db import models

from django_countries import CountryField
from django_countries.countries import COUNTRIES

from account.models import UserOwnedBase


class Customer(UserOwnedBase):
	name = models.CharField(max_length=100)
	adress_line_1 = models.CharField(max_length=100, blank=True)
	adress_line_2 = models.CharField(max_length=100, blank=True)
	#country = CountryField(default='au')
	country = models.CharField(max_length=100, choices=COUNTRIES, default='au')
	# TODO: add country field.
