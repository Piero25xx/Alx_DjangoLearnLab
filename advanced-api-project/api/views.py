from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorListView(generics.ListCreateAPIView):
    """View to list and create authors."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows authenticated users to create

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View to retrieve, update, or delete an author."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can modify

class BookListView(generics.ListCreateAPIView):
    """View to list and create books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['title', 'author__name', 'publication_year']  # Filter by title, author name, and publication year
    search_fields = ['title', 'author__name']  # Search in title and author name
    ordering_fields = ['title', 'publication_year']  # Order by title and publication year
    ordering = ['title']  # Default ordering

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View to retrieve, update, or delete a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can modify

class CreateView(generics.CreateAPIView):
    """View to create a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create

class UpdateView(generics.UpdateAPIView):
    """View to update an existing book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can modify

class DeleteView(generics.DestroyAPIView):
    """View to delete an existing book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete
