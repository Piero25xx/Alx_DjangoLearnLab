from django.urls import path
from .views import BookList  # Import your view
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
     path('books/', BookList.as_view(), name='book-list'),
     path('', include(router.urls)),

    ]
