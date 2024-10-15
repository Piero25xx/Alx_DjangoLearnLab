from django.shortcuts import render
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorListView(generics.ListCreateAPIView):
    """View to list and create authors."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View to retrieve, update, or delete an author."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListView(generics.ListCreateAPIView):
    """View to list and create books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View to retrieve, update, or delete a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Additional Views for Create, Update, and Delete
class CreateView(generics.CreateAPIView):
    """View to create an author or book."""
    # Implement logic here if needed (e.g., dynamically handle models)
    pass

class UpdateView(generics.UpdateAPIView):
    """View to update an author or book."""
    # Implement logic here if needed (e.g., dynamically handle models)
    pass

class DeleteView(generics.DestroyAPIView):
    """View to delete an author or book."""
    # Implement logic here if needed (e.g., dynamically handle models)
    pass
