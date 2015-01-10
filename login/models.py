from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
	line1 = models.CharField(max_length=200,default='asfdf')
	line2 = models.CharField(max_length=200,default='asfdf')
	city = models.CharField(max_length=50,default='asfdf')
	state = models.CharField(max_length=50,default='asfdf')
	pin = models.CharField(max_length=10,default='asfdf')
	landmark = models.CharField(max_length=200,default='asfdf')
	phone = models.CharField(max_length=11,default='asfdf')

class UserDetailsManager(models.Manager):
	def create_user_details(self,username,password,email,
		addr1=None,addr2=None,city=None,state=None,pin=None,landmark=None,phone=None):
		user = User.objects.create_user(username,email,password)
		# if addr1 is None or addr2 is None or city is None or state is None or pin is None or phone is None:
		addr = Address()
		addr.save()
		
		ud = UserDetails(user=user,address=addr)
		ud.save()
		return ud


class UserDetails(models.Model):
	user = models.OneToOneField(User)
	address = models.ForeignKey(Address)

	objects = UserDetailsManager()
