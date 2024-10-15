from django.shortcuts import render
from .models import Book  # Assuming you have a Book model in models.py
from django.views.generic.detail import DetailView
from .models import Library  # Assuming you have a Library model in models.py
from django.contrib.auth import views as auth_views  # Import built-in login/logout views
from django.contrib.auth.forms import UserCreationForm  # Import UserCreationForm for registration
from django.contrib.auth import login  # To log in the user after registration
from django.shortcuts import render, redirect  # To render templates and handle redirects
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test
from .models import Book

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

# View to add a book, requires 'can_add_book' permission
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        # Your logic for adding a book
        pass
    return render(request, 'relationship_app/add_book.html')

# View to change a book, requires 'can_change_book' permission
@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Your logic for changing a book
        pass
    return render(request, 'relationship_app/change_book.html', {'book': book})

# View to delete a book, requires 'can_delete_book' permission
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books_list')  # Redirect after deletion
    return render(request, 'relationship_app/delete_book.html', {'book': book})


def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'


# Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member View
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

