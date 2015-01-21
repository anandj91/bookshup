from django.test import TestCase

from books import models as books_model

class TestIndexResponse(TestCase):

	def initialTest(self):
		g1 = books_model.Genre.objects.create(name='test_genre1')
		g2 = books_model.Genre.objects.create(name='test_genre2')
		b1 = books_model.Book.objects.create(name='test_book1',desc='test desc1',genre=g1,pages=10,edition=1,isbn='isbn',rating=5,count=3)
		b2 = books_model.Book.objects.create(name='test_book2',desc='test desc2',genre=g2,pages=10,edition=1,isbn='isbn',rating=5,count=3)
		a1 = books_model.Author.objects.create(name='test_author1',desc='test desc1',born="1991-04-11",died="1991-04-11",gender="m",website="url")
		a2 = books_model.Author.objects.create(name='test_author2',desc='test desc2',born="1991-04-11",died="1991-04-11",gender="m",website="url")

		ag1 = books_model.AuthorGenre.objects.create(author=a1,genre=g1)
		ag2 = books_model.AuthorGenre.objects.create(author=a1,genre=g2)

		ba1 = books_model.BookAuthor.objects.create(book=b1,author=a1)
		ba2 = books_model.BookAuthor.objects.create(book=b1,author=a2)

		bd1 = books_model.BookDetails.objects.create(book=b1,price=10,new=True,condition='a')
		bd2 = books_model.BookDetails.objects.create(book=b1,price=20,new=False,condition='b')

		respone = self.client.get('/books/?term=test&')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "test_book1")
		self.assertContains(response, "test_book2")
