from rest_framework.generics import generics.ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer  # Use BookSerializer to serialize the data

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


