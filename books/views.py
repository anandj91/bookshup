from django.http import JsonResponse
from django.db.models import Min

import logging

from books.models import Book, BookAuthor, Author, BookDetails, Genre, AuthorGenre

# Getting logger instance
books_logger = logging.getLogger(__name__)

def categories(request):
	genres = Genre.objects.all()

	response = []
	for genre in genres:
		r = {}
		r['id'] = genre.pk
		r['name'] = genre.name
		response.append(r)

	return JsonResponse(response, safe=False)

def index(request):
	term = request.GET.get('term')
	text = request.GET.get('text')
	limit = request.GET.get('limit')
	offset = request.GET.get('offset')
	'''
		order = ['rating'|'price'|'count']
	'''
	order = request.GET.get('order')

	if limit is None or limit > 20:
		limit = 20
	if offset is None:
		offset = 0
	if order is None:
		order = 'rating'

	books = []

	if text is not None:
		'''
			TODO: need to implement fuzzy search when text param is given
		'''
		books = BookDetails.objects.select_related('book').filter(book__name__icontains=text)\
							.values('book__pk','book__name','book__rating','book__desc',)
	elif term is not None:
		books = BookDetails.objects.select_related('book').filter(book__name__icontains=term)\
							.values('book__pk','book__name',)
	else:
		books = BookDetails.objects.select_related('book')\
							.values('book__pk','book__name','book__rating','book__desc',)
	
	if order == 'count' or order == 'rating':
		order = "-book__" + order
		
	books = books.annotate(price=Min('price')).order_by(order)
	
	response = []

	for book in books:
		r = {}
		r['pk'] = book['book__pk']
		r['name'] = book['book__name']
		bas = BookAuthor.objects.filter(book_id=book['book__pk'])
		if not bas:
			r['authors'] = None
		else:
			r['authors'] = ', '.join([ba.author.name for ba in bas])
		
		if term is not None:
			tr = {}
			tr['label'] = r['name']
			tr['value'] = r
			r = tr
		else:
			r['desc'] = book['book__desc']
			r['rating'] = book['book__rating']
			r['price'] = book['price']

		response.append(r)
	
	return JsonResponse(response, safe=False)