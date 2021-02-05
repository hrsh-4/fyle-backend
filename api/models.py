from django.db import models
from django.urls import reverse

# Create your models here.


class Bank(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return str(self.id) + " " +self.name

class Branch(models.Model):
	ifsc = models.CharField(max_length = 11 ,primary_key = True)
	bank_id = models.PositiveIntegerField()
	branch = models.CharField(max_length = 100)
	address = models.CharField(max_length = 300)
	city = models.CharField(max_length = 100)
	district = models.CharField(max_length = 100)
	state = models.CharField(max_length = 100)
	is_favourite = models.BooleanField(default = False)

	def __str__(self):
		return self.ifsc+ " " +  self.branch
