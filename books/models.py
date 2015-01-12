from django.db import models

class Genre(models.Model):
	name = models.CharField(max_length=50)
	author = models.ForeignKey(Author)

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
	author = models.ManyToManyField(Author)
	genre = models.ForeignKey(Genre)
	pages = models.IntegerField()
	edition = models.IntegerField()
	isbn = models.CharField(max_length=50)