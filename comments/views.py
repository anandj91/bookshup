from django.http import JsonResponse

from comments.models import UserComments, BookComments
from login.models import UserDetails

import logging


'''
Getting logger instance 
'''
comments_logger = logging.getLogger(__name__)


'''
Book comment operations
'''
def book(request, id):
	response = comment(request, id, "BOOK")

	return JsonResponse(response, safe=False)


'''
Seller comment operations
'''
def user(request, id):
	response = comment(request, id, "USER")

	return JsonResponse(response, safe=False)


'''
Comment operations
'''
def comment(request, id, model):
	limit = request.GET.get('limit')
	offset = request.GET.get('offset')
	text = request.POST.get('text')

	if limit is None or limit > 20 or limit < 0:
		limit = 20
	if offset is None:
		offset = 0

	response = None

	if text is None:
		response = get_comments(id, model, limit, offset)
	else:
		'''
		TODO: check for user authentication
		'''
		user = UserDetails.objects.get(user=request.user)
		response = set_comments(id, model, user, text)

	return response

'''
Returns the comment on seller or book
'''
def get_comments(ref, model, limit, offset):
	comments = None

	if model is "USER":
		comments = UserComments.objects.select_related('user__user').filter(seller=ref)\
								.order_by('-timestamp')[offset:limit+offset]
	elif model is "BOOK":
		comments = BookComments.objects.select_related('user__user').filter(book=ref)\
							.order_by('-timestamp')[offset:limit+offset]
	
	response = {}

	if comments is None:
		response['status'] = False
	else:
		response['status'] = True
		response['result'] = []
		for comment in comments:
			r = {}
			r['id'] = comment.pk
			r['user'] = comment.user.user.username
			r['comment'] = comment.comment
			r['timestamp'] = comment.timestamp

			response['result'].append(r)

	return response


'''
Adds new comments
'''
def set_comments(ref, model, user, comment):
	comment = None

	if model is "USER":
		comment = UserComments.objects.create(seller=ref, user=user, comment=comment)
	elif model is "BOOK":
		comment = BookComments.objects.create(book=ref, user=user, comment=comment)

	response = {}

	if comment is None:
		response['status'] = False
	else:
		response['status'] = True

	return response
	


