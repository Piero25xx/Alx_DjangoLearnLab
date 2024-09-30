from django.urls import path
from .views import list_books
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),  # Add your home view here
    path('books/', views.list_books, name='list_books'),  # FBV for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # CBV for library details
    path('add_book/', views.add_book, name='add_book'),  # Add book view
    path('edit_book/<int:book_id>/', views.change_book, name='change_book'),  # Edit book view
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),  # Delete book view
    path('books/', views.book_list, name='book_list'),
]


