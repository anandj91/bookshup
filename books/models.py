from django.db import models
from django.contrib.auth.models import User

from login.models import UserDetails


'''
Category/Genre of a Book/Author
'''
class Genre(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name


'''
Author details
'''
class Author(models.Model):
	name = models.CharField(max_length=50)
	desc = models.CharField(max_length=1000)
	born = models.DateField()
	died = models.DateField()
	gender = models.CharField(max_length=1)
	website = models.CharField(max_length=100)
	genre = models.ManyToManyField(Genre, through='AuthorGenre')

	def __str__(self):
		return self.name


'''
Book details
'''
class Book(models.Model):
	name = models.CharField(max_length=100)
	desc = models.CharField(max_length=1000)
	author = models.ManyToManyField(Author, through='BookAuthor')
	genre = models.ManyToManyField(Genre, through='BookGenre')
	pages = models.IntegerField()
	edition = models.IntegerField(default=1)
	isbn = models.CharField(max_length=50, unique=True)
	'''
	rating - 1 to 5
	'''
	rating = models.SmallIntegerField(default=0)
	no_of_ratings = models.BigIntegerField(default=0)
	sales = models.BigIntegerField(default=0)

	def __str__(self):
		return self.name


'''
Mapping between Author and Book
'''
class BookAuthor(models.Model):
	book = models.ForeignKey(Book)
	author = models.ForeignKey(Author)

	def __str__(self):
		return self.book.name+" - "+self.author.name


'''
Mapping between Author and Genre
'''
class AuthorGenre(models.Model):
	author = models.ForeignKey(Author)
	genre = models.ForeignKey(Genre)

	def __str__(self):
		return self.genre.name+" - "+self.author.name


'''
Mapping between Book and Genre
'''
class BookGenre(models.Model):
	book = models.ForeignKey(Book)
	genre = models.ForeignKey(Genre)

	def __str__(self):
		return self.genre.name+" - "+self.book.name


'''
Details about the books posted by users
'''
class BookDetails(models.Model):
	book = models.ForeignKey(Book)
	owner = models.ForeignKey(UserDetails, null=True)
	price = models.FloatField()
	
	'''
	A - New book.
	B - 2nd hand. But as good as new.
	C - 2nd hand. Readable.
	D - 2nd hand. Very bad condition.
	'''
	condition = models.CharField(max_length=1)

	def __str__(self):
		return str(self.book)+" - "+str(self.price)


'''
Comments on a particular book
'''
class Comments(models.Model):
	book = models.ForeignKey(Book)
	user = models.ForeignKey(UserDetails)
	comment = models.CharField(max_length=2000)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.comment
