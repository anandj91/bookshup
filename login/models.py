from django.db import models
from django.contrib.auth.models import User


'''
Address of the user.
'''
class Address(models.Model):
	line1 = models.CharField(max_length=200,default='asfdf')
	line2 = models.CharField(max_length=200,default='asfdf')
	city = models.CharField(max_length=50,default='asfdf')
	state = models.CharField(max_length=50,default='asfdf')
	pin = models.CharField(max_length=10,default='asfdf')
	landmark = models.CharField(max_length=200,default='asfdf')
	phone = models.CharField(max_length=11,default='asfdf')


'''
Manager class for UserDetails.
Has method to create user details object.
'''
class UserDetailsManager(models.Manager):
	def create_user_details(self,username,password,email,
		addr1=None,addr2=None,city=None,state=None,pin=None,landmark=None,phone=None):
		user = User.objects.create_user(username,email,password)
		# if addr1 is None or addr2 is None or city is None or state is None or pin is None or phone is None:
		'''
		TODO: Change this to Address.objects.create()
		'''
		addr = Address()
		addr.save()
		
		'''
		TODO: Change this to UserDetails.objects.create()
		'''
		ud = UserDetails(user=user,address=addr)
		ud.save()
		return ud


'''
Wrapper for user.
Has additional field(s) like address, rating etc.
'''
class UserDetails(models.Model):
	user = models.OneToOneField(User)
	address = models.ForeignKey(Address)
	'''
	rating - 1 to 5
	Rating of the seller.
	'''
	rating = models.SmallIntegerField(default=0)
	no_of_ratings = models.BigIntegerField(default=0)

	objects = UserDetailsManager()
