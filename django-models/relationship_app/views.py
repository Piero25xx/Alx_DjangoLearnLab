from django.shortcuts import render
from .models import Book  # Assuming you have a Book model in models.py
from django.views.generic.detail import DetailView
from .models import Library  # Assuming you have a Library model in models.py
from django.contrib.auth import views as auth_views  # Import built-in login/logout views
from django.contrib.auth.forms import UserCreationForm  # Import UserCreationForm for registration
from django.contrib.auth import login  # To log in the user after registration
from django.shortcuts import render, redirect  # To render templates and handle redirects

def list_books(request):

    books = Book.objects.all()
    
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Home view (optional, to test redirects after login/logout)
def home(request):
    return render(request, 'relationship_app/home.html')

# Custom registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to home page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
