from rest_framework.generics import ListAPIView  # Import ListAPIView from Django REST Framework
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer  # Use BookSerializer to serialize the data
