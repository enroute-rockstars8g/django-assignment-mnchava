from rest_framework import viewsets, permissions
from books.serializers import *

class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = []

class AuthorViewSet(viewsets.ModelViewSet):
	queryset = Author.objects.all().order_by('-name')
	serializer_class = AuthorSerializer
	permission_classes = []

class BooksAuthorsViewSet(viewsets.ModelViewSet):
	queryset = BooksAuthors.objects.all()
	serializer_class = BooksAuthorsSerializer
	permission_classes = []