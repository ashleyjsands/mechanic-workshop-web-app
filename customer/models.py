# Copyright (c) 2013 Ashley Sands (ajsands.com.au)
from django.db import models
from django.core.validators import RegexValidator

from django_countries.countries import COUNTRIES

from account.models import UserOwnedBase


phone_number_validator = RegexValidator(
	regex=r'^[0-9 \(\)]{8,16}$', message="Phone numbers must consist of numbers and be of 8 to 16 numbers in length"
)

class Customer(UserOwnedBase):
	name = models.CharField(max_length=100)
	address_line_1 = models.CharField(max_length=100, blank=True)
	address_line_2 = models.CharField(max_length=100, blank=True)
	suburb = models.CharField(max_length=50, blank=True)
	city = models.CharField(max_length=50, blank=True)
	post_code = models.CharField(max_length=4, blank=True)
	country = models.CharField(max_length=100, choices=COUNTRIES, default='au')
	home_number = models.CharField(max_length=16, blank=True, validators=[phone_number_validator])
	work_number = models.CharField(max_length=16, blank=True, validators=[phone_number_validator])
	mobile_number = models.CharField(max_length=16, blank=True, validators=[phone_number_validator])

	def __unicode__(self):
		return self.name

