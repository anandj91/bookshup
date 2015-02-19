from django.http import JsonResponse
from django.db.models import Min

from books.models import Book, BookAuthor, Author, BookDetails, Genre, AuthorGenre

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

	response = []
	for genre in genres:
		r = {}
		r['id'] = genre.pk
		r['name'] = genre.name
		response.append(r)

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
		books = BookDetails.objects.select_related('book').filter(book__name__icontains=text)
	elif term is not None:
		books = BookDetails.objects.select_related('book').filter(book__name__icontains=term)
	else:
		books = BookDetails.objects.select_related('book')

	if category is not None:
		books = books.filter(book__genre=category)

	books = books.values('book__pk','book__name','book__rating','book__desc','book__sales')

	if order == 'sales' or order == 'rating':
		order = "-book__" + order
		
	''' 
	Sorting the result 
	'''
	books = books.annotate(price=Min('price')).order_by(order)[offset:limit+offset]
	
	response = []

	for book in books:
		r = {}
		r['pk'] = book['book__pk']
		r['name'] = book['book__name']

		'''
		Fetch Authors of the book
		'''
		bas = BookAuthor.objects.filter(book_id=book['book__pk'])
		if bas:
			r['authors'] = ', '.join([ba.author.name for ba in bas])
		
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
				r['genre'] = ', '.join([bg.genre.name for bg in bgs])

		response.append(r)
	
	return JsonResponse(response, safe=False)


'''
Details of individual book with id
'''
def book(request, id):
	book = Book.objects.get(pk=id)

	response = {}

	return JsonResponse(response, safe=False)

