from django.db import models

class Author(models.Model):
	name = models.CharField(max_length = 128)
	last_name = models.CharField(max_length = 128, null = True)

class Book(models.Model):
	title = models.CharField(max_length = 256)
	isbn = models.CharField(max_length = 13)
	publish_year = models.SmallIntegerField(default=2000)
	price = models.DecimalField(max_digits = 6, decimal_places = 2)
	created_at = models.DateTimeField(auto_now_add = True, null = True)
	updated_at = models.DateTimeField(auto_now = True,null = True)
	authors = models.ManyToManyField(Author, through='BooksAuthors')

class BooksAuthors(models.Model):
	book = models.ForeignKey(Book, related_name = 'BooksAuthors', on_delete = models.DO_NOTHING)
	author = models.ForeignKey(Author, on_delete = models.DO_NOTHING)