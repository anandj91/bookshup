from django.db import models
from django.contrib.auth.models import User

from books.models import BookDetails


'''
Interests of users in a book
'''
class Interests(models.Model):
	user = models.ForeignKey(User)
	bd_id = models.ForeignKey(BookDetails)

