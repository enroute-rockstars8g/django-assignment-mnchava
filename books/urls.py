from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.BookViewSet)
router.register(r'author', views.AuthorViewSet)
router.register(r'books-author', views.BooksAuthorsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
