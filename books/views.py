from django.http import JsonResponse

import logging

from books.models import Book, BookAuthor, Author, BookDetails

# Getting logger instance
books_logger = logging.getLogger(__name__)

def get_categories(request):
	return JsonResponse(
		[
			{'id':1, 'name':'erotic'},
			{'id':2, 'name':'fiction'},
			{'id':3, 'name':'non-fiction'},
		], safe=False)

def index(request):
	term = request.GET.get('term')
	text = request.GET.get('text')
	limit = request.GET.get('limit')
	offset = request.GET.get('offset')
	order = request.GET.get('order')

	if limit is None:
		limit = 20
	if offset is None:
		offset = 0
	if order is None:
		order = 'rating'

	query_set = None
	if text is not None:
		# TODO: need to implement fuzzy search when text param is given
		query_set = Book.objects.filter(name__icontains=text)
	elif term is not None:
		query_set = Book.objects.filter(name__icontains=term)
	else:
		query_set = Book.objects.all()
		
	query_set = query_set.order_by(order)[offset:limit]
	
	response = []

	for book in query_set:
		r = {}
		r['pk'] = book.pk
		r['name'] = book.name
		bas = BookAuthor.objects.filter(book=book)
		r['authors'] = ', '.join([ba.author.name for ba in bas])

		if text is not None:
			r['desc'] = book.desc
			r['rating'] = book.rating
			r['price'] = BookDetails.objects.filter(book=book).order_by('price')[0].price
		elif term is not None:
			tr = {}
			tr['label'] = r['name']
			tr['value'] = r
			r = tr
		response.append(r)

	# if text is not None:
	# 	for book in query_set:
	# 		r = []
	# 		r['pk'] = book.pk
	# 		r['name'] = book.name
	# 		bas = BookAuthor.objects.get(book=book)
	# 		r['authors'] = ', '.join([author.name for author in bas])
	# 		r['desc'] = book.desc
	# 		r['rating'] = book.rating
	# 		r['price'] = BookDetails.objects.get(book=book).order_by('price')[0].price
	# 		response.append(r)
	# elif term is not None:
	# 	for book in query_set:
	# 		r = []
	# 		r['label'] = book.name
	# 		value['pk'] = book.pk
	# 		value['name'] = book.name
	# 		bas = BookAuthor.objects.get(book=book)
	# 		value['author'] = ', '.join([author.name for author in bas])
	# 		r['value'] = value
	# 		response.append(r)
	
	return JsonResponse(response, safe=False)