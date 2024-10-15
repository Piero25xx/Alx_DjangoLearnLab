from django.urls import path
from .views import AuthorListView, AuthorDetailView, BookListView, BookDetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', CreateView.as_view(), name='book-create'),  # New create endpoint
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),  # New update endpoint
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='book-delete'),  # New delete endpoint
]