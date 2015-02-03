from django.db import models

class Genre(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name;

class Author(models.Model):
	name = models.CharField(max_length=50)
	desc = models.CharField(max_length=1000)
	born = models.DateField()
	died = models.DateField()
	gender = models.CharField(max_length=1)
	website = models.CharField(max_length=100)

	def __str__(self):
		return self.name;

class Book(models.Model):
	name = models.CharField(max_length=100)
	desc = models.CharField(max_length=1000)
	genre = models.ForeignKey(Genre)
	pages = models.IntegerField()
	edition = models.IntegerField(default=1)
	isbn = models.CharField(max_length=50,unique=True)
	rating = models.SmallIntegerField(default=-1)
	count = models.BigIntegerField(default=0)

	def __str__(self):
		return self.name;

class BookAuthor(models.Model):
	book = models.ForeignKey(Book)
	author = models.ForeignKey(Author)

	def __str__(self):
		return self.book.name+" - "+self.author.name;

class AuthorGenre(models.Model):
	author = models.ForeignKey(Author)
	genre = models.ForeignKey(Genre)

	def __str__(self):
		return self.genre.name+" - "+self.author.name;

class BookDetails(models.Model):
	book = models.ForeignKey(Book)
	price = models.FloatField()
	new = models.BooleanField(default=True)
	condition = models.CharField(max_length=1)

	def __str__(self):
		return str(self.book)+" - "+str(self.price);
