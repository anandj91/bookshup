from django.http import JsonResponse

from books.models import Book, BookAuthor, Author, Genre, AuthorGenre, BookGenre, Comments
from shop.models import BookDetails, SYN
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

	response = True

	'''
	Register Buy Interest
	'''
	syn = SYN.objects.create(user=user,book=book)

	'''
	Validation
	'''
	if syn is None:
		response = False

	'''
	TODO: Notify the seller through internal notification and e-mail
	'''

	return JsonResponse(response, safe=False)


'''
Want to sell request
'''
def sell(request):
	book = Book.objects.get(request.GET.get('id'))
	owner = request.user
	price = request.GET.get('price')
	condition = request.GET.get('condition')

	response = True

	'''
	Register a new BookDetails entry
	'''
	entry = BookDetails.objects.create(book=book,owner=owner,price=price,condition=condition)

	'''
	Validation
	'''
	if entry is None:
		response = False

	return JsonResponse(response, safe=False)