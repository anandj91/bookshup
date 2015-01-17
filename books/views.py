from django.shortcuts import render
from django.http import JsonResponse

import logging

# Getting logger instance
books_logger = logging.getLogger(__name__)

def get_categories(request):
	return JsonResponse(
		[
			{'id':1, 'name':'erotic'},
			{'id':2, 'name':'fiction'},
			{'id':3, 'name':'non-fiction'},
		], safe=False)

def search_books(request):
	term = request.GET.get('term')
	return JsonResponse(
			[
      {"label":"test1", "value":{"name":"anand"}},
      {"label":"test4", "value":{"name":"anand2"}},
      {"label":"test6", "value":{"name":"anand3"}},
    ], safe=False)