from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class PhoneBook(models.Model):

	name = models.CharField(max_length=250)
	code = models.PositiveIntegerField(default=312,  validators=[MaxValueValidator(999), MinValueValidator(100)])
	number = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(999999), MinValueValidator(100000)])
	address = models.CharField(max_length=250, null=False)


	def __str__(self):
		return self.name
