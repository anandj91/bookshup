from django.db import models
from django.contrib.auth.models import User

from login.models import UserDetails
from books.models import Book


'''
Comments on a particular book
'''
class BookComments(models.Model):
	book = models.ForeignKey(Book)
	user = models.ForeignKey(UserDetails)
	comment = models.CharField(max_length=2000)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.comment


'''
Comments on a particular User
'''
class UserComments(models.Model):
	seller = models.ForeignKey(UserDetails,  related_name='+')
	user = models.ForeignKey(UserDetails,  related_name='+')
	comment = models.CharField(max_length=2000)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.comment
