from django.http import JsonResponse
from django.db.models import Min

from books.models import Book, BookAuthor, Author, Genre, AuthorGenre, BookGenre
from shop.models import BookDetails
from login.models import UserDetails

import logging


'''
Getting logger instance 
'''
books_logger = logging.getLogger(__name__)


'''
Get categories
'''
def categories(request):
	genres = Genre.objects.all()

	response = {}
	response['status'] = True
	response['result'] = []

	for genre in genres:
		r = {}
		r['id'] = genre.pk
		r['name'] = genre.name
		response['result'].append(r)

	return JsonResponse(response, safe=False)


'''
Search books
'''
def index(request):
	term = request.GET.get('term')
	text = request.GET.get('text')
	limit = request.GET.get('limit')
	offset = request.GET.get('offset')
	'''
	order = ['rating'|'price'|'sales']
	'''
	order = request.GET.get('order')
	category = request.GET.get('category')

	if limit is None or limit > 20 or limit < 0:
		limit = 20
	if offset is None:
		offset = 0
	if order is None:
		order = 'rating'

	books = None

	'''
	Filtering by search text
	'''
	if text is not None:
		'''
		TODO: need to implement fuzzy search when text param is given
		'''
		books = BookDetails.objects.select_related('book').filter(book__name__icontains=text)
	elif term is not None:
		books = BookDetails.objects.select_related('book').filter(book__name__icontains=term)
	else:
		books = BookDetails.objects.select_related('book')

	'''
	Filtering by category
	'''
	if category is not None:
		books = books.filter(book__genre=category)

	'''
	Picking necessary columns to group the rows by price
	'''
	books = books.values('book__pk','book__name','book__rating','book__desc','book__sales')

	if order == 'sales' or order == 'rating':
		order = "-book__" + order
		
	''' 
	Sorting the result 
	'''
	books = books.annotate(price=Min('price')).order_by(order)[offset:limit+offset]
	
	response = {}
	response['status'] = True
	response['result'] = []

	for book in books:
		r = {}
		r['id'] = book['book__pk']
		r['name'] = book['book__name']

		'''
		Fetch Authors of the book
		'''
		bas = BookAuthor.objects.filter(book_id=book['book__pk'])
		if bas:
			r['authors'] = [ba.author.name for ba in bas]
		
		if term is not None:
			tr = {}
			tr['label'] = r['name']
			tr['value'] = r
			r = tr
		else:
			r['desc'] = book['book__desc']
			r['rating'] = book['book__rating']
			r['sales'] = book['book__sales']
			r['price'] = book['price']

			'''
			Fetch Genres for the book
			'''
			bgs = BookGenre.objects.filter(book_id=book['book__pk'])
			if bgs:
				r['genre'] = [bg.genre.name for bg in bgs]

		response['result'].append(r)
	
	return JsonResponse(response, safe=False)


'''
Details of individual book with id
'''
def book(request, id):
	book = Book.objects.prefetch_related('genre','author').get(pk=id)

	response = {}
	response['status'] = True
	
	r = {}

	r['id'] = book.pk
	r['name'] = book.name
	r['desc'] = book.desc
	r['authors'] = [a.name for a in book.author.all()]
	r['genre'] = [g.name for g in book.genre.all()]
	r['pages'] = book.pages
	r['edition'] = book.edition
	r['isbn'] = book.isbn
	r['rating'] = book.rating
	r['sales'] = book.sales

	response['result'] = r

	return JsonResponse(response, safe=False)


'''
List of sellers of the book with id
'''
def sellers(request, id):
	limit = request.GET.get('limit')
	offset = request.GET.get('offset')
	'''
	order = ['rating'|'price']
	'''
	order = request.GET.get('order')

	if limit is None or limit > 5 or limit < 0:
		limit = 5
	if offset is None:
		offset = 0
	if order is None:
		order = 'price'

	if order == 'rating':
		order = '-owner__rating'

	sellers = BookDetails.objects.filter(book=id).select_related('owner','owner__user')\
							.order_by(order)[offset:limit+offset]

	response = {}
	response['status'] = True
	response['result'] = []

	for seller in sellers:
		r = {}
		r['id'] = seller.pk
		r['owner'] = seller.owner.user.username
		r['rating'] = seller.owner.rating
		r['price'] = seller.price
		r['condition'] = seller.condition

		response['result'].append(r)

	return JsonResponse(response, safe=False)