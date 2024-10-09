from rest_framework import serializers
from .models import Book  # Assuming your Book model is in models.py in the same app

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # This will include all fields in the Book model

