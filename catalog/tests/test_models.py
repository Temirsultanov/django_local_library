import uuid

from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.

from ..models import Author, Genre, Book, BookInstance, Language
class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='3twoUan', summary="Textabout")

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        book=Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length,200)

    def test_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_summary_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('summary').verbose_name
        self.assertEquals(field_label, 'summary')

    def test_summary_max_length(self):
        book=Book.objects.get(id=1)
        max_length = book._meta.get_field('summary').max_length
        self.assertEquals(max_length,1000)

    def test_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEquals(field_label, 'ISBN')

    def test_isbn_max_length(self):
        book=Book.objects.get(id=1)
        max_length = book._meta.get_field('isbn').max_length
        self.assertEquals(max_length, 13)

    def test_language_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('language').verbose_name
        self.assertEquals(field_label, 'language')

    def test_genre_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('genre').verbose_name
        self.assertEquals(field_label, 'genre')

    def test_object_name_is_title(self):
        book=Book.objects.get(id=1)
        expected_object_name = book.title
        self.assertEquals(expected_object_name,str(book))

    def test_get_absolute_url(self):
        book=Book.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(book.get_absolute_url(),'/catalog/book/1')

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_death_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label,'died')

    def test_date_of_birth_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label,'birthed')

    def test_first_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,100)

    def test_last_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_last_name_comma_first_name(self):
        author=Author.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name,str(author))

    def test_get_absolute_url(self):
        author=Author.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(),'/catalog/author/1')

class BookInstanceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        BookInstance.objects.create(imprint="1234567890123", status="o")

    def test_book_label(self):
        bookinstance = BookInstance.objects.get(imprint="1234567890123")
        field_label = bookinstance._meta.get_field('book').verbose_name
        self.assertEquals(field_label,'book')

    def test_borrower_label(self):
        bookinstance = BookInstance.objects.get(imprint="1234567890123")
        field_label = bookinstance._meta.get_field('borrower').verbose_name
        self.assertEquals(field_label, 'borrower')

    def test_imprint_label(self):
        bookinstance = BookInstance.objects.get(imprint="1234567890123")
        field_label = bookinstance._meta.get_field('imprint').verbose_name
        self.assertEquals(field_label, 'imprint')

    def test_imprint_max_length(self):
        bookinstance=BookInstance.objects.get(imprint="1234567890123")
        max_length = bookinstance._meta.get_field('imprint').max_length
        self.assertEquals(max_length, 200)

    def test_due_back_label(self):
        bookinstance = BookInstance.objects.get(imprint="1234567890123")
        field_label = bookinstance._meta.get_field('due_back').verbose_name
        self.assertEquals(field_label, 'due back')

    def test_status_label(self):
        bookinstance = BookInstance.objects.get(imprint="1234567890123")
        field_label = bookinstance._meta.get_field('status').verbose_name
        self.assertEquals(field_label, 'status')

    def test_status_max_length(self):
        bookinstance=BookInstance.objects.get(imprint="1234567890123")
        max_length = bookinstance._meta.get_field('status').max_length
        self.assertEquals(max_length, 1)
