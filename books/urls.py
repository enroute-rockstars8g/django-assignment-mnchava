from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'list', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'books-author', views.BooksAuthorsViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'publishers', views.PublisherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
