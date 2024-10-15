from django.shortcuts import render
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorList(generics.ListCreateAPIView):
    """API view to list and create authors."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update, or delete an author."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookList(generics.ListCreateAPIView):
    """API view to list and create books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update, or delete a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
