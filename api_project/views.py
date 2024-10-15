from rest_framework.generics import ListAPIView  # Import ListAPIView from Django REST Framework
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import ExampleModel
from .serializers import ExampleModelSerialize

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieve all Book instances
    serializer_class = BookSerializer  # Use BookSerializer to serialize the data

class ExampleModelViewSet(ModelViewSet):

    """
    Viewset for ExampleModel.

    Permissions:
    - Authenticated users can view and edit their own records.
    - Admin users have full access to all records.
    """

    queryset = ExampleModel.objects.all()
    serializer_class = ExampleModelSerializer
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated userscla
