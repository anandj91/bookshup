from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
	line1 = models.CharField(max_length=200,default='asfdf')
	line2 = models.CharField(max_length=200,default='asfdf')
	city = models.CharField(max_length=50,default='asfdf')
	state = models.CharField(max_length=50,default='asfdf')
	pin = models.CharField(max_length=10,default='asfdf')
	landmark = models.CharField(max_length=200,default='asfdf')

class UserDetails(models.Model):
	user = models.OneToOneField(User)
	address = models.ForeignKey(Address)
	phone = models.CharField(max_length=11,default='asfdf')

