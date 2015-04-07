from django.http import JsonResponse

from books.models import Book, BookAuthor, Author, Genre, AuthorGenre, BookGenre, Comments
from shop.models import BookDetails, SYN, ACK, SYNACK
from login.models import UserDetails

import logging


'''
Getting logger instance 
'''
shop_logger = logging.getLogger(__name__)


'''
Want to buy request
'''
def buy(request):
	book = BookDetails.objects.get(pk=request.GET.get('id'))
	# user = UserDetails.objects.get(user=request.user)
	user = UserDetails.objects.get(user__username='admin')

	response = {}
	response['status'] = False

	'''
	Register Buy Interest
	'''
	syn = SYN.objects.create_syn(buyer=user,book=book)

	'''
	Validation
	'''
	if syn is not None:
		response['status'] = True

	'''
	TODO: Notify the seller through internal notification and e-mail
	'''

	return JsonResponse(response, safe=False)


'''
Acknowledge the buy request
'''
def acknowledgement(request):
	syn = request.GET.get('syn')

	response = {}
	response['status'] = False

	'''
	Register ACK
	'''
	ack = ACK.objects.create_ack(syn_id=syn)

	'''
	Validation
	'''
	if ack is not None:
		response['status'] = True

	'''
	TODO: Notify buyer through internal notification and e-mail
	'''

	return JsonResponse(response, safe=False)


'''
Payment
TODO: Integrate with Online payment gateways
'''
def payment(request):
	ack = request.GET.get('ack')

	response = {}
	response['status'] = False

	'''
	Register SYNACK
	'''
	synack = SYNACK.objects.create_synack(ack_id=ack)

	'''
	Validation
	'''
	if ack is not None:
		response['status'] = True

	'''
	TODO: Notify buyer and seller through internal notification and e-mail
	'''

	return JsonResponse(response, safe=False)


'''
Want to sell request
'''
def sell(request):
	book_id = request.GET.get('id')
	book = Book.objects.get(book_id)
	owner = request.user
	price = request.GET.get('price')
	condition = request.GET.get('condition')

	response = {}
	response['status'] = False

	'''
	Register a new BookDetails entry
	'''
	entry = BookDetails.objects.create(book=book,owner=owner,price=price,condition=condition)

	'''
	Validation
	'''
	if entry is not None:
		response['status'] = True

	return JsonResponse(response, safe=False)