from django.db import models

from books.models import Book
from login.models import UserDetails


'''
Mode of payment - [COD|ONLINE]
'''
class ModeOfPayment(models.Model):
	mode = models.CharField(max_length=10)
	desc = models.CharField(max_length=200)


'''
Condition of the book
	A - New book.
	B - 2nd hand. But as good as new.
	C - 2nd hand. Readable.
	D - 2nd hand. Bad condition.
'''
class Condition(models.Model):
	condition = models.CharField(max_length=1)
	desc = models.CharField(max_length=200)


'''
Details about the books posted by users
'''
class BookDetails(models.Model):
	book = models.ForeignKey(Book)
	owner = models.ForeignKey(UserDetails, null=True)
	price = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)
	mode = models.ManyToManyField(ModeOfPayment)
	condition = models.CharField(max_length=1)

	def __str__(self):
		return str(self.book)+" - "+str(self.price)


'''
Manager for SYN
'''
class SYNManager(models.Manager):
	def create_syn(buyer,book,mode):
		if buyer is None or book is None or mode is None:
			return None

		'''
		TODO: Add validation
		'''

		result = create(buyer=user,book=book,mode=mode)
		return result


'''
Request to buy a book from buyer
'''
class SYN(models.Model):
	buyer = models.ForeignKey(UserDetails, null=False)
	book = models.ForeignKey(BookDetails, null=False)
	syn_ts = models.DateTimeField(auto_now_add=True)
	mode = models.ForeignKey(ModeOfPayment, null=False)

	objects = SYNManager()

	def __str__(self):
		return str(self.buyer)+" - "+str(self.book)


'''
Manager for ACK
'''
class ACKManager(models.Manager):
	def create_ack(syn_id):
		syn = SYN.objects.get(pk=syn_id).select_related('book')

		if syn is None:
			return None

		'''
		TODO: Add validation
		'''

		result = create(refNo=syn_id,buyer=syn.buyer,seller=syn.book.owner,book=syn.book,syn_ts=syn.syn_ts,mode=syn.mode)
		syn.delete()
		return result


'''
Response from seller to the SYN
'''
class ACK(models.Model):
	refNo = models.CharField(max_length=10)
	buyer = models.ForeignKey(UserDetails, null=False, related_name='+')
	seller = models.ForeignKey(UserDetails, null=False, related_name='+')
	book = models.ForeignKey(BookDetails, null=False)
	syn_ts = models.DateTimeField()
	ack_ts = models.DateTimeField(auto_now_add=True)
	mode = models.ForeignKey(ModeOfPayment, null=False)

	objects = ACKManager()

	def __str__(self):
		return str(self.buyer)+" - "+str(self.seller)+" - "+str(self.book)


'''
Manager for SYNACK
'''
class SYNACKManager(models.Manager):
	def create_synack(ack_id):
		ack = ACK.objects.get(pk=ack_id)

		if ack is None:
			return None
		
		'''
		TODO: Add validation
		'''

		result = create(refNo=ack.refNo,buyer=ack.buyer,seller=ack.seller,book=ack.book,syn_ts=ack.syn_ts,ack_ts=ack.ack_ts,mode=mode)
		ack.delete()
		return result


'''
Payment from buyer and send the address to seller
'''
class SYNACK(models.Model):
	refNo = models.CharField(max_length=10)
	buyer = models.ForeignKey(UserDetails, null=False, related_name='+')
	seller = models.ForeignKey(UserDetails, null=False, related_name='+')
	book = models.ForeignKey(BookDetails, null=False)
	syn_ts = models.DateTimeField()
	ack_ts = models.DateTimeField()
	synack_ts = models.DateTimeField(auto_now_add=True)
	mode = models.ForeignKey(ModeOfPayment, null=False)

	objects = SYNACKManager()

	def __str__(self):
		return str(self.buyer)+" - "+str(self.seller)+" - "+str(self.book)

