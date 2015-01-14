from django.db import models

class Genre(models.Model):
	name = models.CharField(max_length=50)

class Author(models.Model):
	name = models.CharField(max_length=50)
	desc = models.CharField(max_length=1000)
	born = models.DateField()
	died = models.DateField()
	gender = models.CharField(max_length=1)
	website = models.CharField(max_length=100)

class Book(models.Model):
	name = models.CharField(max_length=100)
	desc = models.CharField(max_length=1000)
	genre = models.ForeignKey(Genre)
	pages = models.IntegerField()
	edition = models.IntegerField()
	isbn = models.CharField(max_length=50)

class BookAuthor(models.Model):
	book = models.ForeignKey(Book)
	author = models.ForeignKey(Author)

class AuthorGenre(models.Model):
	author = models.ForeignKey(Author)
	genre = models.ForeignKey(Genre)

class BookDetails(models.Model):
	book = models.ForeignKey(Book)
	price = models.FloatField()
	new = models.BooleanField(default=True)
	condition = models.CharField(max_length=1)
