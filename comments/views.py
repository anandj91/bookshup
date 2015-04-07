from django.http import JsonResponse

from comments.models import Comments
from login.models import UserDetails

import logging


'''
Getting logger instance 
'''
books_logger = logging.getLogger(__name__)


'''
List of comments of the book with id
'''
def comments(request, id):
	limit = request.GET.get('limit')
	offset = request.GET.get('offset')

	if limit is None or limit > 5 or limit < 0:
		limit = 5
	if offset is None:
		offset = 0

	comments = Comments.objects.select_related('user__user').filter(book=id)\
							.order_by('timestamp')[offset:limit+offset]

	response = []

	for comment in comments:
		r = {}
		r['id'] = comment.pk
		r['user'] = comment.user.user.username
		r['comment'] = comment.comment
		r['timestamp'] = comment.timestamp

		response.append(r)

	return JsonResponse(response, safe=False)