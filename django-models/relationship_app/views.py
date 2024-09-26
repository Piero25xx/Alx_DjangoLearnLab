from django.shortcuts import render

from .models import Book  # Assuming you have a Book model in models.py

from django.views.generic.detail import DetailView

from .models import Library  # Assuming you have a Library model in models.py
def list_books(request):

    books = Book.objects.all()
    
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

