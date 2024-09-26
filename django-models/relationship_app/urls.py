from django.urls import path
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # FBV for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # CBV for library details
]

