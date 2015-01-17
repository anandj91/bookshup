from django.shortcuts import render
from django.http import JsonResponse

def get_categories(request):
	return JsonResponse(
		[
			{'id':1, 'name':'erotic'},
			{'id':2, 'name':'fiction'},
			{'id':3, 'name':'non-fiction'},
		]
		, safe=False)