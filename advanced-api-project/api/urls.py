from django.urls import path
from .views import AuthorList, AuthorDetail, BookList, BookDetail

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('create/', CreateView.as_view(), name='create'),  # Optional
    path('update/<int:pk>/', UpdateView.as_view(), name='update'),  # Optional
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),  # Optional
]