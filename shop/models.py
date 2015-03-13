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
Manager for SYN
'''
class SYNManager(models.Manager):
	def create_syn(buyer,book):
		if buyer is None or book is None:
			return None

		return create(user=user,book=book)


'''
Request to buy a book from buyer
'''
class SYN(models.Model):
	buyer = models.ForeignKey(UserDetails)
	book = models.ForeignKey(BookDetails)
	syn_ts = models.DateTimeField(auto_now_add=True)

	objects = SYNManager()


'''
Manager for ACK
'''
class ACKManager(models.Manager):
	def create_ack(buyer,seller,book,syn_ts):
		if buyer is None or seller is None or book is None or syn_ts is None:
			return None

		return create(user=user,seller=seller,book=book,syn_ts=syn_ts)


'''
Response from seller to the SYN
'''
class ACK(models.Model):
	buyer = models.ForeignKey(UserDetails, related_name='+')
	seller = models.ForeignKey(UserDetails, related_name='+')
	book = models.ForeignKey(BookDetails)
	syn_ts = models.DateTimeField()
	ack_ts = models.DateTimeField(auto_now_add=True)

	objects = ACKManager()


'''
Manager for SYNACK
'''
class SYNACKManager(models.Manager):
	def create_ack(buyer,seller,book,syn_ts,ack_ts):
		if buyer is None or seller is None or book is None or syn_ts is None or ack_ts is None:
			return None

		return create(user=user,seller=seller,book=book,syn_ts=syn_ts,ack_ts=ack_ts)


'''
Payment from buyer and send the address to seller
'''
class SYNACK(models.Model):
	buyer = models.ForeignKey(UserDetails, related_name='+')
	seller = models.ForeignKey(UserDetails, related_name='+')
	book = models.ForeignKey(BookDetails)
	syn_ts = models.DateTimeField()
	ack_ts = models.DateTimeField()
	synack_ts = models.DateTimeField(auto_now_add=True)
	'''
	Mode of payment - [COD|ONLINE]
	'''
	mode = models.CharField(max_length=10)

	objects = SYNACKManager()

