from django.shortcuts import render
from django.http import HttpResponse

import logging

# Getting logger instance
home_logger = logging.getLogger(__name__)


def index(request):
	return render(request, 'home/index.html')

def books(request):
	return render(request, 'books/index.html')

def books_search(request):
	return render(request, 'books/search.html')

def books_search_result(request):
	return render(request, 'books/result.html')
