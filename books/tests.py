from django.test import TestCase
from django.core.urlresolvers import reverse

from books.models import Book, Author, Genre, BookAuthor, BookGenre, AuthorGenre, Comments
from login.models import UserDetails
from shop.models import BookDetails


class TestIndexResponse(TestCase):

	def test_initialTest(self):
		g1 = Genre.objects.create(name='test_genre1')
		g2 = Genre.objects.create(name='test_genre2')
		b1 = Book.objects.create(name='test_book1',desc='test desc1',pages=10,edition=1,isbn='isbn1',rating=5,sales=3)
		b2 = Book.objects.create(name='test_book2',desc='test desc2',pages=10,edition=1,isbn='isbn2',rating=4,sales=4)
		b3 = Book.objects.create(name='test_book3',desc='test desc3',pages=10,edition=1,isbn='isbn3',rating=2,sales=5)
		b4 = Book.objects.create(name='test_book4',desc='test desc4',pages=10,edition=1,isbn='isbn4',rating=1,sales=6)
		b5 = Book.objects.create(name='test_book5',desc='test desc5',pages=10,edition=1,isbn='isbn5',rating=3,sales=7)
		a1 = Author.objects.create(name='test_author1',desc='test desc1',born="1991-04-11",died="1991-04-11",gender="m",website="url")
		a2 = Author.objects.create(name='test_author2',desc='test desc2',born="1991-04-11",died="1991-04-11",gender="m",website="url")

		ag1 = AuthorGenre.objects.create(author=a1,genre=g1)
		ag2 = AuthorGenre.objects.create(author=a1,genre=g2)

		ba1 = BookAuthor.objects.create(book=b1,author=a1)
		ba2 = BookAuthor.objects.create(book=b1,author=a2)
		ba3 = BookAuthor.objects.create(book=b2,author=a1)
		ba4 = BookAuthor.objects.create(book=b3,author=a2)
		ba5 = BookAuthor.objects.create(book=b4,author=a1)
		ba6 = BookAuthor.objects.create(book=b5,author=a2)

		ba1 = BookGenre.objects.create(book=b1,genre=g1)
		ba2 = BookGenre.objects.create(book=b1,genre=g2)
		ba3 = BookGenre.objects.create(book=b2,genre=g1)
		ba4 = BookGenre.objects.create(book=b3,genre=g2)
		ba5 = BookGenre.objects.create(book=b4,genre=g1)
		ba6 = BookGenre.objects.create(book=b5,genre=g2)

		ud = UserDetails.objects.create_user_details(username='admin',password='admin',email='anand.indukala@gmail.com')

		bd1 = BookDetails.objects.create(book=b1,price=10,condition='a',owner=ud)
		bd2 = BookDetails.objects.create(book=b1,price=20,condition='b',owner=ud)
		bd3 = BookDetails.objects.create(book=b1,price=30,condition='a',owner=ud)
		bd4 = BookDetails.objects.create(book=b2,price=20,condition='b',owner=ud)
		bd5 = BookDetails.objects.create(book=b3,price=10,condition='a',owner=ud)
		bd6 = BookDetails.objects.create(book=b3,price=25,condition='b',owner=ud)
		bd7 = BookDetails.objects.create(book=b3,price=15,condition='a',owner=ud)
		bd8 = BookDetails.objects.create(book=b3,price=20,condition='b',owner=ud)
		bd9 = BookDetails.objects.create(book=b4,price=10,condition='a',owner=ud)
		bd10 = BookDetails.objects.create(book=b5,price=20,condition='b',owner=ud)

		c1 = Comments.objects.create(book=b1,user=ud,comment='asdfasdfsd')
		c2 = Comments.objects.create(book=b1,user=ud,comment='asdfasdfsddfgfd')

		# testing '/books/'
		response1 = self.client.get(reverse('books:index'))
		self.assertEqual(response1.status_code, 200)
		self.assertContains(response1, "test_book1")
		self.assertContains(response1, "test_book2")

		# testing '/books/?term=not'
		response2 = self.client.get(reverse('books:index'),{'term':'not'})
		self.assertEqual(response2.status_code, 200)
		self.assertContains(response2, "not_test_book1")
		self.assertNotContains(response2, "test_book2")

		# testing '/books/?text=not'
		response3 = self.client.get(reverse('books:index'),{'text':'not'})
		self.assertEqual(response3.status_code, 200)
		self.assertContains(response3, "not_test_book1")
		self.assertNotContains(response3, "test_book2")
