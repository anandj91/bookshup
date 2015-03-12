from django.db import models

from books.models import Book
from login.models import UserDetails


'''
Details about the books posted by users
'''
class BookDetails(models.Model):
	book = models.ForeignKey(Book)
	owner = models.ForeignKey(UserDetails, null=True)
	price = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)
	
	'''
	A - New book.
	B - 2nd hand. But as good as new.
	C - 2nd hand. Readable.
	D - 2nd hand. Very bad condition.
	'''
	condition = models.CharField(max_length=1)

	def __str__(self):
		return str(self.book)+" - "+str(self.price)


'''
Interests of users in a book
'''
class BuyInterests(models.Model):
	user = models.ForeignKey(UserDetails)
	book = models.ForeignKey(BookDetails)
	timestamp = models.DateTimeField(auto_now_add=True)
	


